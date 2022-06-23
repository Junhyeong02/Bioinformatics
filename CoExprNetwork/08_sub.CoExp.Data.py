import sys
import os
import numpy as np
import pandas as pd

ID_modules = sys.argv[1]  # ../06.CoExpNetwork/Bac/ID_colors.txt
ID_color = sys.argv[2]    # ../06.CoExpNetwork/Bac/moduleColors.txt
ID_data = sys.argv[3]     # ../06.CoExpNetwork/Bac/Bac.tissue.TPM.txt

df_id_module = pd.read_csv(ID_modules, sep = "\t", header = None)
df_order_color = pd.read_csv(ID_color, sep = "\t", header = None)

df_id_module.dropna(inplace = True)
df_order_color.dropna(inplace = True)

df_merged = pd.merge(df_id_module, df_order_color, how = "inner", left_index = True, right_index = True)
df_merged.columns = ["ID", "num", "order", "color"]

se_temp = df_merged.groupby("num")["color"].unique()

df_temp = pd.DataFrame(se_temp, columns = ["color"])
df_temp.to_csv(os.path.join(os.path.dirname(ID_modules), "Num_Module.txt"), sep = "\t")

df_merged.drop(["num", "order"], axis = 1, inplace = True)
df_merged.to_csv(os.path.join(os.path.dirname(ID_modules), "GeneID_Color.txt"), sep = "\t", index = False)

df_data = pd.read_csv(ID_data, sep = "\t")
color_list = list(set(df_merged["color"]))

if not os.path.exists(os.path.join(os.path.dirname(ID_modules), "Module")):
    os.mkdir(os.path.join(os.path.dirname(ID_modules), "Module"))

for color in color_list:
    se_c_ID = df_merged[df_merged["color"] == color]["ID"]
    df_temp2 = df_data[df_data["GeneID"].isin(se_c_ID)]

    df_temp2.to_csv(os.path.join(os.path.dirname(ID_modules), "Module", "ME" + color + ".txt"), sep = "\t", index = False)




