# updraft-migrator
Convert urls and database name in updraft.
If you have local changes and want them to be reflected in the staging site, run this script on the *database* backup created by Updraft. 

## Usage: 
If you need to push your local changes to a staging Elementor site, make sure you have Updraft installed then create a full backup. Download all the individual backup files to a folder. In this case, it's `backup/`. 

Run the `renam
```bash
$ ls -l backup/
total 130968
-rw-r--r--@ 1 sudoguest  staff       196 Aug 22 11:45 backup_2019-08-22-1836_Studio_Wild_3e760a95ea6f-others.zip
-rw-r--r--@ 1 sudoguest  staff    684331 Aug 22 14:18 backup_2019-08-22-2115_Studio_Wild_525ff91305dc-db.gz
-rw-r--r--@ 1 sudoguest  staff       196 Aug 22 14:17 backup_2019-08-22-2115_Studio_Wild_525ff91305dc-others.zip
-rw-r--r--@ 1 sudoguest  staff  16907213 Aug 22 14:17 backup_2019-08-22-2115_Studio_Wild_525ff91305dc-plugins.zip
-rw-r--r--@ 1 sudoguest  staff    572848 Aug 22 14:17 backup_2019-08-22-2115_Studio_Wild_525ff91305dc-themes.zip
-rw-r--r--@ 1 sudoguest  staff  48818138 Aug 22 14:17 backup_2019-08-22-2115_Studio_Wild_525ff91305dc-uploads.zip
$ ./rename.py --oldurl http://localhost:8888 --newurl https://studiowild.ten-forward.com --olddb wp_studio_wild --newdb wordpress --filename backup/backup_2019-08-22-2115_Studio_Wild_525ff91305dc-db.gz
Replacing in backup/backup_2019-08-22-2115_Studio_Wild_525ff91305dc-db.gz: 
 - URL: http://localhost:8888 -> https://studiowild.ten-forward.com 
 - DB: wp_studio_wild -> wordpress
-------------------------------------------------------------------
read contents of file
replaced urls and db names
writing swapped contents to old file
```

After you have run this script, you can upload all the updraft backup pieces, in this example found in `backup/`, to staging and restore. 

This can also be used to restore locally from an UpDraft backup done on the staging site, if there are changes you would like to pull down. 

For now, this does mean that we are unable to use remote storage of backups and it must be done manually -_-. We can use this script for some s3 fanciness later if 
running manually is too much of a hassle. 
