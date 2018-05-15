#!/usr/bin/python3

import json
import pandas as pd
import argparse

# Add flags to the program
parser = argparse.ArgumentParser(description='ViSenze fashion attribute extraction')
parser.add_argument('-i','--input_file', type=str, metavar='', help='the input tagging result file path with name in csv format from ViSenze dashboard', required=True)
parser.add_argument('-o','--output_file', type=str, metavar='', help='the output file path with name in csv format', required=True)
args = parser.parse_args()


def fashion_attribute_extraction(input_file,output_file):

    #Read the input tagging result in csv format created from Visenze dashboard
    df_tagging = pd.read_csv(input_file, skipinitialspace=True, usecols=['tags'])
    df_csv = pd.read_csv(input_file, skipinitialspace=True)

    # Parse the input tagging result in csv format created from Visenze dashboard
    tagging = df_tagging.to_json(orient='records')
    index = 0

    for elmt in json.loads(tagging):
        if elmt['tags'] is not None:
            jd = json.loads(elmt['tags'])
            for idx, val in enumerate(jd):
                if len(val['objects']) > 0 and jd[idx]['tag_group'] == "fashion_attributes":
                    for i in range(len(val['objects'][0]['tags'])):
                        result = val['objects'][0]['tags'][i]['tag'].split(':')
                        key = result[0]
                        value = result[-1]
                        df_tagging.at[index, key] = value
        index += 1

    # Combine the parsed fashion style and occasion with the input file
    df = pd.concat([df_csv, df_tagging], axis=1)
    df = df.drop('tags',axis=1)

    return df.to_csv(output_file,encoding='utf-8',index=False)

if __name__ == '__main__':
    try:
        fashion_attribute_extraction(args.input_file, args.output_file)
    except Exception:
        print('Please tag your input file using ViSenze dashboard. Ignore if you have already done so.')
