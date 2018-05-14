#!/usr/bin/env bash
#full mode

#Example folder names
#dir_upload="csv_to_upload"
#dir_backup="csv_backup"
#dir_ftp="ftpuploadtest"

#Example FTP credentials (get from Visenze dashboard)
#username="chauncyyin"
#password="########################"
#ftp_address="###.visenze.com"


#Generate long flags

while [[ $# -gt 0 ]]
do
	key="$1"

	case $key in
		-l|--upload)
			args[0]="$2"
			shift
			shift
			;;
		-b|--backup)
			args[1]="$2"
			shift
			shift
			;;
		-f|--ftp)
			args[2]="$2"
			shift
			shift
			;;
		-f|--username)
			args[3]="$2"
			shift
			shift
			;;
		-f|--password)
			args[4]="$2"
			shift
			shift
			;;
		-f|--ftp_address)
			args[5]="$2"
			shift
			shift
			;;

		*)
			echo "WRONG ARUGMENT!"
			shift
			shift
			;;
	esac
done


#Backup the .csv files into the folder named "csv_backup" from the "csv_to_upload" folder. 

rsync -a --include='*.csv' --exclude='*' "${args[0]}/" "${args[1]}/"


#Send the files to the ftp server according to the instructions: http://developers.visenze.com/setup/#FTP-upload
for f in "${args[0]}"/*.csv; do
	filename=$(basename $f)
 	gzip -k "${args[0]}/$filename"
  	mv "${args[0]}/$filename" "${args[0]}/$filename.txt"
 	mv "${args[0]}/$filename.gz" ${args[2]}
 	mv "${args[0]}/$filename.txt" ${args[2]}
 	ncftpput -R -v -u ${args[3]} -p ${args[4]} ${args[5]} / ${args[2]}/*
 	rm ${args[2]}/*
done
