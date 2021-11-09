import lasio
import numpy as np
import os
import pandas as pd

src_folder = r"D:\WVU Masters Research 2020\NNE_Boggess-1H_FOWL4_SMF-CF_P10"
target_folder = r"H:\Output CSV"
stages = os.listdir(target_folder)
stage_folder = os.path.join(target_folder, 'Stage 03')
stage_folder_path = os.path.join(target_folder, stage_folder)

#for stage in stages:
    #utput_folder = os.path.join(target_folder, stage)
    #if not os.path.exists(output_folder):
        #os.mkdir(output_folder)
    #print(stage)
    #for file in os.listdir(os.path.join(src_folder, stage)):
        #las = lasio.read(os.path.join(src_folder, stage, file))
        #csv = las.to_csv(os.path.join(target_folder, stage, file))
        #print(file)



#las = lasio.read(os.path.join(folder, file))
#csv = las.to_csv(os.path.join(folder2, file2))

big_data = pd.DataFrame()

#df = pd.read_csv(os.path.join(stage_folder_path, "NNE_Boggess-1H_FOWL4_SMF-CF_P10_RMS_190809040559.las"))
#df.dropna(axis = 0, inplace=True)
#df.drop(["RMS", "RMS.1", "RMS.2"], axis = 1, inplace = True)
#print(df)

for file in os.listdir(stage_folder_path):
    df = pd.DataFrame()
    df = pd.read_csv(os.path.join(stage_folder_path, file))
    df.dropna(axis=0, inplace=True)
    df.drop(["RMS", "RMS.1", "RMS.2"], axis=1, inplace=True)
    big_data.append(df)
