# Visenze-Client-Solutions-Datafeed-Integration
This script creates a scheduled job on Visenze datafeed integration through FTP method. It supports two modes: 
1. FULL (Default):the contents of this file will be used to fully replace your current image database.
2. INCREMENT:the contents of the datafeed file will be used to append new entries or update existing entries. If a delete file is provided, batch remove based on the data in the delete file will be performed after the successful index of the datafeed.

Steps to follow before executing the script
1. Create three folders: your_upload_folder_name, your_backup_folder_name, your_ftp_folder_name;
2. Put the csv files (UTF-8 formatting) to be uploaded into your_upload_folder_name and follow the naming convention below:
```bash

FULL (Default) mode
Name your csv files as admin_access_key.csv. For Example: 83b3a2dc6cf4b0966575250b26449770.csv

```

```bash

INCREMENT mode
Name your csv files as admin_access_key_INCREMENT.csv. For Example: 83b3a2dc6cf4b0966575250b26449770_INCREMENT.csv
Name your batch remove files as admin_access_key_DELETE.csv (optional). For Example: 83b3a2dc6cf4b0966575250b26449770_DELETE.csv(optional)
```
3. Install ncftp
```bash

$ sudo apt-get install ncftp

```

Running the script
```bash

$ bash ~/dir/ftp_sample.sh --upload ~/dir/your_upload_folder_name --backup ~/dir/your_backup_folder_name --ftp ~/dir/your_ftp_folder_name --username XXX --password XXX --ftp_address XXX 

```

Scheduling FTP task at 10am everyday 
```bash
crontab -e
```
```bash
0 10 * * * bash ~/dir/ftp_sample.sh --upload ~/dir/your_upload_folder_name --backup ~/dir/your_backup_folder_name --ftp ~/dir/your_ftp_folder_name --username XXX --password XXX --ftp_address XXX 
```
