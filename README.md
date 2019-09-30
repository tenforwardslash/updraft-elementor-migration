# updraft-migrator
Convert urls and database name in updraft.
If you have local changes and want them to be reflected in the staging site, run this script on the *database* backup created by Updraft. 

## Usage: 
Make sure you have Updraft installed then create a full backup. Download all the individual backup files to a folder. In this case, it's `backup/`. 

Run the `rename.py` script. For this example, the WordPress site is MyWordpress, and we are migrating from a production backup at https://my-wordpress.com to a local instance at http://localhost:8888. The production database is `zsdfa38snz`, while the local database is `wp_my_wordpress`. 

```bash
$ ls -l backup/
total 130968
-rw-r--r--@ 1 sudoguest  staff       196 Aug 22 11:45 backup_2019-08-22-1836_MyWordpress_3e760a95ea6f-others.zip
-rw-r--r--@ 1 sudoguest  staff    684331 Aug 22 14:18 backup_2019-08-22-2115_MyWordpress_525ff91305dc-db.gz
-rw-r--r--@ 1 sudoguest  staff       196 Aug 22 14:17 backup_2019-08-22-2115_MyWordpress_525ff91305dc-others.zip
-rw-r--r--@ 1 sudoguest  staff  16907213 Aug 22 14:17 backup_2019-08-22-2115_MyWordpress_525ff91305dc-plugins.zip
-rw-r--r--@ 1 sudoguest  staff    572848 Aug 22 14:17 backup_2019-08-22-2115_MyWordpress_525ff91305dc-themes.zip
-rw-r--r--@ 1 sudoguest  staff  48818138 Aug 22 14:17 backup_2019-08-22-2115_MyWordpress_525ff91305dc-uploads.zip
$ ./rename.py --oldurl https://my-wordpress.com --newurl http://localhost:8888 --olddb zsdfa38snz --newdb wp_my_wordpress --filename backup/backup_2019-08-22-2115_MyWordpress_525ff91305dc-db.gz
Replacing in backup/backup_2019-08-22-2115_MyWordpress_525ff91305dc-db.gz: 
 - URL: https://my-wordpress.com -> http://localhost:8888 
 - DB: zsdfa38snz -> wp_my_wordpress
-------------------------------------------------------------------
read contents of file
replaced urls and db names
writing swapped contents to old file
```

After you have run this script, you can upload all the updraft backup pieces, in this example found in `backup/`, to your site and restore. 

If this script is used to restore from a remote site, you can place all the backups in `your-wordpress-install/wp-content/updraft` and directly run the rename script from there. You will then be able to rescan local storage from the UpDraft admin screen without having to upload any files. 
