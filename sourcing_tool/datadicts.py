"""
Use IPEDS xls files to find verbose (human-readable) names for each column in
each table and write out models with verbose names to new_models.py
"""
import xlrd
import os
import re

os.chdir("IPEDS_Data")

col_dict = {}

for file_name in os.listdir():
    if file_name.endswith(".xls"):
        workbook = xlrd.open_workbook(file_name)
        worksheet = workbook.sheet_by_name('varlist')
        headers = worksheet.row_values(0)
        varname = headers.index('varname')
        varTitle = headers.index('varTitle')
        varnames = worksheet.col_values(varname, start_rowx=1)
        varTitles = worksheet.col_values(varTitle, start_rowx=1)
        table_dict = dict(zip(varnames, varTitles))
        
        # checking for multiple values for each key
        new_keys = set(table_dict.keys())
        curr_keys = set(col_dict.keys())
        for key in new_keys.intersection(curr_keys):
            # print("old value:" + col_dict[key])
            # print("new value:" + table_dict[key])
            table_dict[key] = col_dict[key]
        
        # add to full dictionary
        col_dict.update(table_dict)

os.chdir('../..')
os.chdir("universities")
new_models = ''

with open('models.py') as mod:
    models = mod.read().splitlines()
    word = "db_column='"
    for ix, line in enumerate(models):
        if word in line:
            # find db_column value
            db_column = re.findall(r"'(.*?)'",line)
            db_column = db_column[0]
            # add "verbose name" arg for each field with value 
            # from col_dict
            verb_name = col_dict.get(db_column)
            # don't add verbose names for Nonetypes
            if verb_name != None: 
                # split each line where the ")" occurs --> EOL
                split_line = re.split('[)]', line)
                # grab the first string from split, and add the verbose name
                # parameter 
                new_line = split_line[0] + ', verbose_name="' \
                        + verb_name.lower() + '")'
                # replace the old line with the new line in the same
                # location within models
                models[ix] = new_line
    string = "\n"
    new_models = string.join(models)
    
with open('new_models.py', 'w') as mod:
    mod.write(new_models)
