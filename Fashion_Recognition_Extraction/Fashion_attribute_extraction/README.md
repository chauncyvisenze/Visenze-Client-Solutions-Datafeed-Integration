# ViSenze-Fashion-Attribute-Extraction
This python script converts an <ins><a href="https://www.dropbox.com/s/qm7h8fwujnpq15t/example_input.csv?dl=1" download="example_input.csv">input fashion attribute file</ins></a> into a <ins><a href="https://www.dropbox.com/s/6s0bbq2618p1flf/fashion_attribute_example_output.csv?dl=1" download="fashion_attribute_example_output.csv">cleaned csv file</ins></a>. The <i>input fashion attribute file</i> is generated from ViSenze dashboard and contains JSON strings such as the following: 
```bash
[{"objects":[{"tags":[{"tag":"category:others","score":1},{"tag":"product_color:white","score":0.5529177188873291},{"tag":"product_pattern:solid","score":0.9749875068664551}],"box":[]}],"debug_objects":[],"tag_group":"fashion_attributes"},{"objects":[{"tags":[{"tag":"no_text","score":0.992056667804718}],"box":[]}],"debug_objects":[],"tag_group":"image_text"},{"objects":[{"tags":[{"tag":"beach_swim","score":0.9747834205627441}],"box":[]}],"debug_objects":[],"tag_group":"fashion_occasion"},{"objects":[{"tags":[{"tag":"no_model","score":0.9999887347221375}],"box":[]}],"debug_objects":[],"tag_group":"image_human"},{"objects":[{"tags":[{"tag":"no_collage","score":0.956714391708374}],"box":[]}],"debug_objects":[],"tag_group":"image_collage"},{"objects":[{"tags":[{"tag":"bohemian","score":0.5293694734573364}],"box":[]}],"debug_objects":[],"tag_group":"fashion_style"},{"objects":[{"tags":[{"tag":"grey","score":0.9317206740379333}],"box":[]}],"debug_objects":[],"tag_group":"product_color"},{"objects":[{"tags":[{"tag":"no_mosaic","score":0.9979895949363708}],"box":[]}],"debug_objects":[],"tag_group":"image_mosaic"},{"objects":[{"tags":[{"tag":"solid","score":0.9796999096870422}],"box":[]}],"debug_objects":[],"tag_group":"product_pattern"},{"objects":[{"tags":[{"tag":"no_detail","score":0.9998171329498291}],"box":[]}],"debug_objects":[],"tag_group":"image_detail"},{"objects":[],"debug_objects":[],"tag_group":"gender_detect_kid"}]
```
With Fashion_attribute_extraction.py, we are able to:
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
