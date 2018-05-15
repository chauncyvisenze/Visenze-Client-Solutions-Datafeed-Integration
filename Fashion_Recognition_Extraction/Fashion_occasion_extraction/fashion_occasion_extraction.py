#!/usr/bin/python3

import json
import pandas as pd
import argparse

# Add flags to the program
parser = argparse.ArgumentParser(description='ViSenze fashion style and occasion extraction')
parser.add_argument('-i','--input_file', type=str, metavar='', help='the input tagging result file path with name in csv format from ViSenze dashboard', required=True)
parser.add_argument('-o','--output_file', type=str, metavar='', help='the output file path with name in csv format', required=True)
args = parser.parse_args()


def parse_style_occasion(input_file,output_file):

    # Read the input tagging result in csv format created from ViSenze dashboard
    df_tagging = pd.read_csv(input_file, skipinitialspace=True, usecols=['tags'])
    df_csv = pd.read_csv(input_file, skipinitialspace=True)

    # Parse the input tagging result in csv format created from Visenze dashboard
    tagging = df_tagging.to_json(orient='records')
    index = 0
    for elmt in json.loads(tagging):
        if elmt['tags'] is not None:
            jd = json.loads(elmt['tags'])
            for idx,val in enumerate(jd):
                if len(val['objects']) > 0 and jd[idx]['tag_group'] == "fashion_occasion":
                    fashion_occasion= val['objects'][0]['tags'][0]['tag']
                    df_tagging.at[index,"fashion_occasion"] = fashion_occasion
                if len(val['objects']) > 0 and jd[idx]['tag_group'] == "fashion_style":
                    fashion_style = val['objects'][0]['tags'][0]['tag']
                    df_tagging.at[index, "fashion_style"] = fashion_style
        index += 1

    # Combine the parsed fashion style and occasion with the input file
    df = pd.concat([df_csv, df_tagging], axis=1)
    df = df.drop('tags',axis=1)

    return df.to_csv(output_file,encoding='utf-8',index=False)

if __name__ == '__main__':
    try:
        parse_style_occasion(args.input_file, args.output_file)
    except Exception:
        print('Please tag your input file using ViSenze dashboard. Ignore if you have already done so.')
