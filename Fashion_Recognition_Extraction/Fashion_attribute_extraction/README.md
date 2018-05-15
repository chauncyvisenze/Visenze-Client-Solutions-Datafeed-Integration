# ViSenze-Fashion-Attribute-Extraction
This python script converts an <a href="https://www.dropbox.com/s/qm7h8fwujnpq15t/example_input.csv?dl=0" download="example_input.csv"<ins>input tagging file(csv)</ins>>

scheduled job on Visenze datafeed integration through API /insert method. It does the following: 
1. Clean image urls in the datafeed (.csv) by removing space
2. Validate image urls in the datafeed (.csv) by checking response
3. Batch insert valid image urls for indexing on Visenze dashboard server 

Steps to follow before executing the script
1. Prepare product catalogue files in CSV format, including im_name and im_url (mandatory). The details for the CSV file is below:
http://developers.visenze.com/setup/#Upload-your-datafeed

2. Configure schema fields on Visenze's dashboard (Your Images -> Config) before running the script. The details can be found below: 
http://developers.visenze.com/setup/#Configure-schema-fields

3. Install ViSearch Python SDK
```bash

$ pip install visearch

```

Running the script
```bash

$ python3 ~/dir/Visenze_insert_API.py -i ~/dir/your_datafeed_csv_filename -u your_Visenze_dashboard_admin_Access_Key -p your_Visenze_dashboard_admin_Secret_Key  

```

Scheduling an API /insert cronjob at 10am everyday 
```bash
crontab -e
```
```bash
0 10 * * * python3 ~/dir/Visenze_insert_API.py -i ~/dir/your_datafeed_csv_filename -u your_Visenze_dashboard_admin_Access_Key -p your_Visenze_dashboard_admin_Secret_Key  
```
