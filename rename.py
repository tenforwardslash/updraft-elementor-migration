#!/usr/bin/env python3
import gzip
import argparse

description = """Convert urls and database name in updraft to accomodate for elementor being lame in their media attachments.
If you have local changes and want them to be reflected in the staging site, run this script on the *database* backup created by Updraft. 
Example: 
   ./rename.py --oldurl http://localhost:8888 --newurl https://studiowild.ten-forward.com --olddb wp_studio_wild --newdb wordpress --filename backup/backup_2019-08-22-2115_Studio_Wild_525ff91305dc-db.gz

After you have run this script, you can upload all the updraft backup pieces to staging and restore. 

This can also be used to restore locally from an UpDraft backup done on the staging site, if there are changes you would like to pull down. 

For now, this does mean that we are unable to use remote storage of backups and it must be done manually -_-. We can use this script for some s3 fanciness later if 
running manually is too much of a hassle. 
"""

parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--oldurl', type=str, help='Old site url to swap out in db backup', required=True)
parser.add_argument('--newurl', type=str, help='New site url to use in db backup', required=True)
parser.add_argument('--olddb', type=str, help='Old database name', default='wordpress')
parser.add_argument('--newdb', type=str, help='New database name', default='wordpress')
parser.add_argument('--filename', type=str, help='UpDraft backup file name', required=True)
parser.add_argument('--backup', help='Save unreplaced to .bak file', action='store_true')
args = parser.parse_args()

escaped_old_url = args.oldurl.replace("/", "\\\/")
escaped_new_url = args.newurl.replace("/", "\\\/")

print("Replacing in {0.filename}: \n - URL: {0.oldurl} -> {0.newurl} \n - Escaped URL: {1} -> {2} \n - DB: {0.olddb} -> {0.newdb}".format(args, escaped_old_url, escaped_new_url))
print("-------------------------------------------------------------------")


with gzip.open(args.filename, 'rb') as f:
	db_contents = f.read()

print("read contents of file")

# replace urls, includeing the weird http:\\/\\/localhost:8888 escaped version
url_replaced = db_contents.replace(args.oldurl.encode(), args.newurl.encode())
escaped_replaced = url_replaced.replace(escaped_old_url.encode(), escaped_new_url.encode())

# replace db name
replaced = escaped_replaced.replace(b'`' + args.olddb.encode() + b'`', b'`' + args.newdb.encode() + b'`')

print("replaced urls and db names")

if args.backup:
	backup_f = args.filename + '.bak'
	print('writing old db contents to ' + backup_f)
	with gzip.open(backup_f, 'wb') as f: 
		f.write(db_contents)

print("writing swapped contents to old file")
with gzip.open(args.filename, 'wb') as f: 
	f.write(replaced)