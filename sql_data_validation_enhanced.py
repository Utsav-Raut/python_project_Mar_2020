import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import math
path_to_excel = "/home/boom/Downloads/data.xlsx"

dw_prd_sku_table = "DW_PRD_SKU"
item_dim_table = "ITEM_DIM"
dw_prd_sku_col_sheet_name = "dw_prd_sku_cols"
dim_item_col_sheet_name = "item_dim_cols"

df_dw_prd_sku = pd.read_excel(path_to_excel, sheet_name='DW_PRD_SKU')
print(len(df_dw_prd_sku.columns))
df_dw_prd_sku.fillna("Null Value", inplace=True)
no_of_sku_data_rows = df_dw_prd_sku[df_dw_prd_sku.columns[0]].count()
print(no_of_sku_data_rows)

df_item_dim = pd.read_excel(path_to_excel, sheet_name='Item_Dim')
df_item_dim.fillna("Null Value", inplace=True)
no_of_item_data_rows = df_item_dim[df_item_dim.columns[0]].count()
print(no_of_item_data_rows)

df_mapping = pd.read_excel(path_to_excel, sheet_name='mapping')
def create_mapping_dict(df):
    mapping_dict = {}

    for i in range(0, df_mapping["DW_PRD_SKU"].count()):
        if(type(df_mapping["ITEM_DIM"][i]) == float):
            continue
        else:
            sku_key = df_mapping["DW_PRD_SKU"][i].strip()
            item_key = df_mapping["ITEM_DIM"][i].strip()
            mapping_dict[sku_key] = item_key
    return mapping_dict
mapping_dict = create_mapping_dict(df_mapping)

def check_for_mismatches(key1, val1, key2, val2):
    if val1 != val2:
        return "mismatch"
    else:
        return "match"
def evaluate_result(mapping_dict, dict_sku, dict_item):
    for key in mapping_dict:
        sku_key = key
        item_key = mapping_dict[key]
        try:
            if sku_key in dict_sku and item_key in dict_item:
                result = check_for_mismatches(sku_key, str(dict_sku[sku_key]), item_key, str(dict_item[item_key]))
                if result == "mismatch":
                    f=open("/home/boom/Documents/mismatch.csv", "a+")
                    f.write(sku_key + "=" + str(dict_sku[sku_key]) + " , " + item_key + "=" + str(dict_item[item_key]+"\r"))
                    f.close()
#                     print(sku_key + "=" + str(dict_sku[sku_key]) + " , " + item_key + "=" + str(dict_item[item_key]))

        except KeyError as e:
            print("*****")
            print("Key:" + str(e) + " is not present/defined.")
            print("*****")
            
if no_of_sku_data_rows == no_of_item_data_rows:
    for i in range(0, no_of_sku_data_rows):
        dict_sku = {}
        dict_item = {}
        for sku_col in df_dw_prd_sku.columns:
            dict_sku[sku_col] = str(df_dw_prd_sku[sku_col][i])
#         print(dict_sku)
        for item_col in df_item_dim.columns:
            dict_item[item_col] = str(df_item_dim[item_col][i])
#         print(dict_item)        
        evaluate_result(mapping_dict, dict_sku, dict_item)

