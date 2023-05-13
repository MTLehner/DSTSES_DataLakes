import glob
import json
import numpy as np
import pandas as pd
import datetime

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

def import_lake_LeXplore(search_string=r'./data/léxplorectdprofiles_datalakesdownload/*.json'):
    start_time = "11.11.2019 10:49:00"
    start_time = datetime.datetime.strptime(start_time, "%d.%m.%Y %H:%M:%S")
    M = [] # | Time | time | seconds since 1970-01-01 00:00:00 | Time 
    y = [] #| Water Pressure | Press | dbar | "Water pressure" is the pressure that exists in the medium  water. It includes the pressure due to overlying water, air and any other medium that may be present.  
    x = [] #| Water Temperature | Temp | degC | Lake water temperature is the in situ temperature of the lake water. To specify the depth at which the temperature applies use a vertical coordinate variable or scalar coordinate variable. There are standard names for lake_surface_temperature, lake_surface_skin_temperature, lake_surface_subskin_temperature and lake_surface_foundation_temperature which can be used to describe data located at the specified surfaces. 
    x1 = [] #| Conductivity | Cond | mS/cm | Electrical conductivity (EC) estimates the amount of total dissolved salts (TDS), or the total amount of dissolved ions in the water. 
    x2 = [] #| Chlorophyll A | Chl_A | g/l | 'Mass concentration' means mass per unit volume and is used in the construction mass_concentration_of_X_in_Y, where X is a material constituent of Y. A chemical or biological species denoted by X may be described by a single term such as 'nitrogen' or a phrase such as 'nox_expressed_as_nitrogen'. Chlorophylls are the green pigments found in most plants, algae and cyanobacteria; their presence is essential for photosynthesis to take place. There are several different forms of chlorophyll that occur naturally. All contain a chlorin ring (chemical formula C20H16N4) which gives the green pigment and a side chain whose structure varies. The naturally occurring forms of chlorophyll contain between 35 and 55 carbon atoms. Chlorophyll-a is the most commonly occurring form of natural chlorophyll. The chemical formula of chlorophyll-a is C55H72O5N4Mg. 
    x3 = [] #| Turbidity | Turb | FTU | Turbidity is a dimensionless quantity which is expressed in NTU (Nephelometric Turbidity Units). Turbidity expressed in NTU is the proportion of white light scattered back to a transceiver by the particulate load in a body of water, represented on an arbitrary scale referenced against measurements made in the laboratory on aqueous suspensions of formazine beads. 
    x4 = [] #| pH | pH |  | A figure expressing the acidity or alkalinity of a solution on a logarithmic scale on which 7 is neutral, lower values are more acid and higher values more alkaline. The pH is equal to −log10 c, where c is the hydrogen ion concentration in moles per litre. 
    x5 = [] #| Oxygen Saturation | sat | % | Fractional saturation is the ratio of some measure of concentration to the saturated value of the same quantity. 
    x6 = [] #| Dissolved Oxygen | DO_mg | mg/l | Dissolved oxygen refers to the level of free, non-compound oxygen present in water or other liquids. 
    x8 = [] #| Binary Error Mask | Press_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x9 = [] #| Binary Error Mask | Temp_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x10 = [] #| Binary Error Mask | Cond_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x12 = [] #| Binary Error Mask | Turb_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x13 = [] #| Binary Error Mask | pH_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x14 = [] #| Binary Error Mask | sat_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x15 = [] #| Binary Error Mask | DO_mg_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x21 = [] #| Binary Error Mask | rho_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x16 = [] #| Density | rho | kg/m3 | Density, mass of a unit volume of a material substance. The formula for density is d = M/V, where d is density, M is mass, and V is volume. Density is commonly expressed in units of grams per cubic centimetre. 
    y1 = [] #| Depth | depth | m | Depth is the vertical distance below the surface. 
    x17 = [] #| Potential Temperature | pt | degC | The potential temperature of a parcel of fluid at pressure {\displaystyle P}P is the temperature that the parcel would attain if adiabatically brought to a standard reference pressure {\displaystyle P_{0}}P_{{0}}, usually 1,000 hPa (1,000 mb).  
    x18 = [] #| Potential Density | prho | kg/m3 | The potential density of a fluid parcel at pressure {\displaystyle P}P is the density that the parcel would acquire if adiabatically brought to a reference pressure {\displaystyle P_{0}}P_{{0}}, often 1 bar (100 kPa).  
    x19 = [] #| Thorpe Displacements | thorpe | m | TBD 
    x20 = [] #| Salinity | SALIN | null | Salinity is the saltiness or amount of salt dissolved in a body of water, called saline water. 
    x7 = [] #| Binary Error Mask | time_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x11 = [] #| Binary Error Mask | Chl_A_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x22 = [] #| Binary Error Mask | depth_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x23 = [] #| Binary Error Mask | pt_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x24 = [] #| Binary Error Mask | prho_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x25 = [] #| Binary Error Mask | thorpe_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    x26 = [] #| Binary Error Mask | SALIN_qual | 0 = nothing to report, 1 = more investigation | data_binary_mask has 1 where condition X is met, 0 elsewhere. 0 = high quality, 1 = low quality.  
    files = glob.glob(search_string)
    for file in files:
        with open(file) as f:
            data = json.load(f)
            M.extend(np.array(data['M'], dtype=np.float32).tolist())
            y.extend(np.array(data['y'], dtype=np.float32).tolist())
            x.extend(np.array(data['x'], dtype=np.float32).tolist())
            x1.extend(np.array(data['x1'], dtype=np.float32).tolist())
            x2.extend(np.array(data['x2'], dtype=np.float32).tolist())
            x3.extend(np.array(data['x3'], dtype=np.float32).tolist())
            x4.extend(np.array(data['x4'], dtype=np.float32).tolist())
            x5.extend(np.array(data['x5'], dtype=np.float32).tolist())
            x6.extend(np.array(data['x6'], dtype=np.float32).tolist())
            x8.extend(np.array(data['x8'], dtype=np.float32).tolist())
            x9.extend(np.array(data['x9'], dtype=np.float32).tolist())
            x10.extend(np.array(data['x10'], dtype=np.float32).tolist())
            x12.extend(np.array(data['x12'], dtype=np.float32).tolist())
            x13.extend(np.array(data['x13'], dtype=np.float32).tolist())
            x14.extend(np.array(data['x14'], dtype=np.float32).tolist())
            x15.extend(np.array(data['x15'], dtype=np.float32).tolist())
            x21.extend(np.array(data['x21'], dtype=np.float32).tolist())
            x16.extend(np.array(data['x16'], dtype=np.float32).tolist())
            y1.extend(np.array(data['y1'], dtype=np.float32).tolist())
            x17.extend(np.array(data['x17'], dtype=np.float32).tolist())
            x18.extend(np.array(data['x18'], dtype=np.float32).tolist())
            x19.extend(np.array(data['x19'], dtype=np.float32).tolist())
            x20.extend(np.array(data['x20'], dtype=np.float32).tolist())
            x7.extend(np.array(data['x7'], dtype=np.float32).tolist())
            x11.extend(np.array(data['x11'], dtype=np.float32).tolist())
            x22.extend(np.array(data['x22'], dtype=np.float32).tolist())
            x23.extend(np.array(data['x23'], dtype=np.float32).tolist())
            x24.extend(np.array(data['x24'], dtype=np.float32).tolist())
            x25.extend(np.array(data['x25'], dtype=np.float32).tolist())
            x26.extend(np.array(data['x26'], dtype=np.float32).tolist())
    df_raw = pd.DataFrame({'M': M, 'y': y, 'x': x, 'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'x5': x5, 'x6': x6, 'x8': x8, 'x9': x9, 'x10': x10, 'x12': x12, 'x13': x13, 'x14': x14, 'x15': x15, 'x21': x21, 'x16': x16, 'y1': y1, 'x17': x17, 'x18': x18, 'x19': x19, 'x20': x20, 'x7': x7, 'x11': x11, 'x22': x22, 'x23': x23, 'x24': x24, 'x25': x25, 'x26': x26})
    df_raw.sort_values(by="M", inplace=True)
    lowest_m = df_raw['M'].min()
    df_raw["date"] = df_raw["M"].apply(lambda x: start_time + datetime.timedelta(seconds=(x - lowest_m)))
    return df_raw


def import_lake_zug(search_string=r'./data/lakezugctdprofiles_datalakesdownload/*.json'):
    start_time = "1970-01-01 00:00:00"
    start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    M = [] #| Time | time | seconds since 1970-01-01 00:00:00 | Time 
    y = [] #| Water Pressure | Press | dbar | "Water pressure" is the pressure that exists in the medium  water. It includes the pressure due to overlying water, air and any other medium that may be present.  
    x1 = [] #| Conductivity | Cond | mS/cm | Electrical conductivity (EC) estimates the amount of total dissolved salts (TDS), or the total amount of dissolved ions in the water. 
    x2 = [] #| Chlorophyll A | Chl_A | null | 'Mass concentration' means mass per unit volume and is used in the construction mass_concentration_of_X_in_Y, where X is a material constituent of Y. A chemical or biological species denoted by X may be described by a single term such as 'nitrogen' or a phrase such as 'nox_expressed_as_nitrogen'. Chlorophylls are the green pigments found in most plants, algae and cyanobacteria; their presence is essential for photosynthesis to take place. There are several different forms of chlorophyll that occur naturally. All contain a chlorin ring (chemical formula C20H16N4) which gives the green pigment and a side chain whose structure varies. The naturally occurring forms of chlorophyll contain between 35 and 55 carbon atoms. Chlorophyll-a is the most commonly occurring form of natural chlorophyll. The chemical formula of chlorophyll-a is C55H72O5N4Mg. 
    x3 = [] #| Turbidity | Turb | FTU | Turbidity is a dimensionless quantity which is expressed in NTU (Nephelometric Turbidity Units). Turbidity expressed in NTU is the proportion of white light scattered back to a transceiver by the particulate load in a body of water, represented on an arbitrary scale referenced against measurements made in the laboratory on aqueous suspensions of formazine beads. 
    x4 = [] #| pH | pH |  | A figure expressing the acidity or alkalinity of a solution on a logarithmic scale on which 7 is neutral, lower values are more acid and higher values more alkaline. The pH is equal to −log10 c, where c is the hydrogen ion concentration in moles per litre. 
    x5 = [] #| Oxygen Saturation | sat | % | Fractional saturation is the ratio of some measure of concentration to the saturated value of the same quantity. 
    x6 = [] #| Dissolved Oxygen | DO_mg | mg/l | Dissolved oxygen refers to the level of free, non-compound oxygen present in water or other liquids. 
    x7 = [] #| Salinity | SALIN | PSU | Salinity is the saltiness or amount of salt dissolved in a body of water, called saline water. 
    x = [] #| Water temperature | Temp | °C | Lake water temperature is the in situ temperature of the lake water. To specify the depth at which the temperature applies use a vertical coordinate variable or scalar coordinate variable. There are standard names for lake_surface_temperature, lake_surface_skin_temperature, lake_surface_subskin_temperature and lake_surface_foundation_temperature which can be used to describe data located at the specified surfaces. 
    files = glob.glob(search_string)
    for file in files:
        with open(file) as f:
            data = json.load(f)
            M.extend(np.array(data['M'], dtype=np.float32).tolist())
            y.extend(np.array(data['y'], dtype=np.float32).tolist())
            x.extend(np.array(data['x'], dtype=np.float32).tolist())
            x1.extend(np.array(data['x1'], dtype=np.float32).tolist())
            x2.extend(np.array(data['x2'], dtype=np.float32).tolist())
            x3.extend(np.array(data['x3'], dtype=np.float32).tolist())
            x4.extend(np.array(data['x4'], dtype=np.float32).tolist())
            x5.extend(np.array(data['x5'], dtype=np.float32).tolist())
            x6.extend(np.array(data['x6'], dtype=np.float32).tolist())
            x7.extend(np.array(data['x7'], dtype=np.float32).tolist())
    df_raw = pd.DataFrame({'M': M, 'y': y, 'x': x, 'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'x5': x5, 'x6': x6, 'x7': x7})
    df_raw.sort_values(by="M", inplace=True)
    df_raw["date"] = df_raw["M"].apply(lambda x: start_time + datetime.timedelta(seconds=(x)))
    return df_raw