# -*- coding: utf-8 -*-
import json
from pprint import pprint

data = []
with open('tedtalk.jl') as data_file:  
    for line in data_file:
        data.append(json.loads(line))

pprint(data[1])

with open('dev-v1.1.json') as data_file:  
    data1 = json.load(data_file)
