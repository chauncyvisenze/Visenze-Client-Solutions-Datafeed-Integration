#!/usr/bin/python3

from visearch import client
import csv
import urllib.request
import urllib.parse
import argparse

#Add flags to the program
parser = argparse.ArgumentParser(description='Visenze datafeed API integration')
parser.add_argument('-i','--input', type=str, metavar='', help='the input datafeed in csv format', required=True)
parser.add_argument('-u','--access_key', type=str, metavar='', help='the access key in our Visenze dashboard', required=True)
parser.add_argument('-p','--secret_key', type=str, metavar='', help='the secret key in our Visenze dashboard', required=True)
args = parser.parse_args()

#Validate image urls
def validate_url(im_url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/55.0.2883.75 Safari/537.36'}
        req = urllib.request.Request(url=im_url,headers=headers)
        response = urllib.request.urlopen(req).getcode()
        if response == 200:
            return im_url
    except Exception:
        return False

#Clean image urls
def clean_url(url):
    im_url = url.strip()
    return im_url.replace(" ", "%20")

#Read csv files by batch - every 100 lines
def batch_reader(reader):
    rows = [None] * 100
    for idx, row in enumerate(reader):
        rows[idx % 100] = row
        if (idx % 100 == 99):
            yield rows
            rows = [None] * 100
    yield list(filter(lambda x:x, rows))


#Call Visenze /insert API to index datafeed
def Visenze_datafeed_insert(input,access_key,secret_key):
    with open(input, 'r',encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        good_images = 0
        bad_images = 0
        api = client.ViSearchAPI(access_key, secret_key)
        for rows in batch_reader(reader):
            rows = [{header[idx]:value for idx, value in enumerate(row)} for row in rows]
            for row in rows:
                row['im_url'] = clean_url(row['im_url'])
                row['im_url'] = validate_url(row['im_url'])
            rows_insert = list(filter(lambda x:x['im_url'],rows))
            good_images += len(rows_insert)
            bad_images += len(rows)-len(rows_insert)
            if len(rows_insert)>0:
                response = api.insert(rows_insert)
                print("The number of images inserted:",good_images, "The number of bad images:",bad_images)
                print(response)

if __name__ == '__main__':
    Visenze_datafeed_insert(args.input,args.access_key,args.secret_key)








