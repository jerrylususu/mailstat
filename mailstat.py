# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 00:25:34 2019

@author: jerry
"""

import datetime
import json
import eml_parser
import os
import io
import sys

path = "C:/Users/jerry/Desktop/mailexp"

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial

outfile = open("out.txt","w")

split = "$"

files = os.listdir(path)
mails = []
i = 0
for file in files:
    with open(os.path.join(path, file), 'rb') as fhdl:
        raw_email = fhdl.read()
#    print(raw_email)
    try:
        parsed_eml = eml_parser.eml_parser.decode_email_b(raw_email)
        outfile.write(str(parsed_eml["header"]["date"]))
        outfile.write(split)
        if('from' in parsed_eml["header"]):
            outfile.write(parsed_eml["header"]["from"])
            outfile.write(split)
        
        parsed_eml["header"]["subject"] = parsed_eml["header"]["subject"].replace('\xa0', ' ').replace('\ufffd',' ').replace('\u02bc',' ')
        parsed_eml["header"]["subject"] = parsed_eml["header"]["subject"].encode("GBK", 'ignore').decode("GBK")
        outfile.write(parsed_eml["header"]["subject"])
        print(i, parsed_eml["header"]["subject"])
    except IndexError:
        print("ERROR: INDEX ERROR")
    
    outfile.write("\n")
    i = i+1
    
#    print(json.dumps(parsed_eml, default=json_serial))
outfile.close()