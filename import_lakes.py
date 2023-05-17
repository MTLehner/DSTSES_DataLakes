import glob
import json
import numpy as np
import pandas as pd
import datetime

def import_lake(search_string:str):
    x = []
    z = []
    z1 = []
    z2 = []
    z3 = []
    z4 = []
    z5 = []
    z6 = []
    z7 = []
    z8 = []
    z9 = []
    files = glob.glob(search_string)
    for file in files:
        with open(file) as f:
            data = json.load(f)
        time = np.array(data['x'], dtype=np.float32)
        npz = np.array(data['z'], dtype=np.float32)
        npz1 = np.array(data['z1'], dtype=np.float32)
        npz2 = np.array(data['z2'], dtype=np.float32)
        npz3 = np.array(data['z3'], dtype=np.float32)
        npz4 = np.array(data['z4'], dtype=np.float32)
        npz5 = np.array(data['z5'], dtype=np.float32)
        npz6 = np.array(data['z6'], dtype=np.float32)
        npz7 = np.array(data['z7'], dtype=np.float32)
        npz8 = np.array(data['z8'], dtype=np.float32)
        npz9 = np.array(data['z9'], dtype=np.float32)
        x.extend(time.tolist())
        z.extend(np.nanmedian(npz, axis=0).tolist())
        z1.extend(np.nanmedian(npz1, axis=0).tolist())
        z2.extend(np.nanmedian(npz2, axis=0).tolist())
        z3.extend(np.nanmedian(npz3, axis=0).tolist())
        z4.extend(np.nanmedian(npz4, axis=0).tolist())
        z5.extend(np.nanmedian(npz5, axis=0).tolist())
        z6.extend(np.nanmedian(npz6, axis=0).tolist())
        z7.extend(np.nanmedian(npz7, axis=0).tolist())
        z8.extend(np.nanmedian(npz8, axis=0).tolist())
        z9.extend(np.nanmedian(npz9, axis=0).tolist())
        #dates_string = file.split('_')[2]
        #dates.append(datetime.datetime.strptime(dates_string,'%Y-%m-%dT%H:%M:%S.%fZ'))
    df_raw = pd.DataFrame({"x":x,"z":z,"z1":z1,"z2":z2,"z3":z3,"z4":z4,"z5":z5,"z6":z6,"z7":z7,"z8":z8,"z9":z9})
    return df_raw

def import_lake_greifen(search_string=r'./data/lakegreifenctdprofiles_datalakesdownload/*.json'):
    start_time = datetime.datetime.strptime("1970-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    x = []
    z = []
    z1 = []
    z2 = []
    z3 = []
    z4 = []
    z5 = []
    z6 = []
    z7 = []
    z8 = []
    z9 = []
    files = glob.glob(search_string)
    for file in files:
        with open(file) as f:
            data = json.load(f)
        time = np.array(data['x'], dtype=np.float32)
        npz = np.array(data['z'], dtype=np.float32)
        npz1 = np.array(data['z1'], dtype=np.float32)
        npz2 = np.array(data['z2'], dtype=np.float32)
        npz3 = np.array(data['z3'], dtype=np.float32)
        npz4 = np.array(data['z4'], dtype=np.float32)
        npz5 = np.array(data['z5'], dtype=np.float32)
        npz6 = np.array(data['z6'], dtype=np.float32)
        npz7 = np.array(data['z7'], dtype=np.float32)
        npz8 = np.array(data['z8'], dtype=np.float32)
        npz9 = np.array(data['z9'], dtype=np.float32)
        x.extend(time.tolist())
        z.extend(np.nanmedian(npz, axis=0).tolist())
        z1.extend(np.nanmedian(npz1, axis=0).tolist())
        z2.extend(np.nanmedian(npz2, axis=0).tolist())
        z3.extend(np.nanmedian(npz3, axis=0).tolist())
        z4.extend(np.nanmedian(npz4, axis=0).tolist())
        z5.extend(np.nanmedian(npz5, axis=0).tolist())
        z6.extend(np.nanmedian(npz6, axis=0).tolist())
        z7.extend(np.nanmedian(npz7, axis=0).tolist())
        z8.extend(np.nanmedian(npz8, axis=0).tolist())
        z9.extend(np.nanmedian(npz9, axis=0).tolist())
        #dates_string = file.split('_')[2]
        #dates.append(datetime.datetime.strptime(dates_string,'%Y-%m-%dT%H:%M:%S.%fZ'))
    df_raw = pd.DataFrame({"x":x,"z":z,"z1":z1,"z2":z2,"z3":z3,"z4":z4,"z5":z5,"z6":z6,"z7":z7,"z8":z8,"z9":z9})
    df_raw.sort_values(by="x", inplace=True)
    df_raw["date"] = df_raw["x"].apply(lambda x: start_time + datetime.timedelta(seconds=(x)))
    return df_raw
