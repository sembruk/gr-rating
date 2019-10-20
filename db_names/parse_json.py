#!/usr/bin/env python3

import json

with open('names.json') as input_file:
    gender_dict = {'m': 0, 'f': 1}
    y = {}
    for l in input_file:
        x = json.loads(l)
        if x.get('text') is not None:
            if x.get('gender') is not None:
                if gender_dict.get(x['gender']) is not None:
                    y[x['text']] = gender_dict[x['gender']]
    output_file_content = json.dumps(y, ensure_ascii=False, sort_keys=True)
    with open('out.jsom', 'w') as output_file:
        output_file.write(output_file_content)



