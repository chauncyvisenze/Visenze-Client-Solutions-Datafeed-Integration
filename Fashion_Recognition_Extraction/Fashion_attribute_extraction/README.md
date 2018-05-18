# ViSenze-Fashion-Attribute-Extraction
This python script converts an <ins><a href="https://www.dropbox.com/s/qm7h8fwujnpq15t/example_input.csv?dl=1" download="example_input.csv">input fashion attribute file</ins></a> into a <ins><a href="https://www.dropbox.com/s/6s0bbq2618p1flf/fashion_attribute_example_output.csv?dl=1" download="fashion_attribute_example_output.csv">cleaned csv file</ins></a> It does the following: 
1. Read the input tagging file in csv format created from Visenze dashboard
2. Extract fashion attributes from the input tagging file
3. Combine the original datafeed with extracted fashion attributes and output the master file in csv format 

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
