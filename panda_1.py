import pandas as pd
from urllib.parse import urlencode

def case_counts(district):
    url_data_gov_hk_get = "https://api.data.gov.hk/v1/historical-archive/get-file"
    url_building_csv = "http://www.chp.gov.hk/files/misc/building_list_eng.csv"
    time = "20200801-1204"

    url_building = (url_data_gov_hk_get + "?" + urlencode({"url": url_building_csv, "time": time}))
    df_building = pd.read_csv(url_building)
    df_district = df_building.loc[(df_building["District"] == district)]
    district_build = df_district[['District', 'Related probable/confirmed cases']]
    list = []
    
    for index, row in district_build.iterrows():
        x = row["Related probable/confirmed cases"].split(",")
        for i in x:
            __ = i.strip()
            if __ in list:
                pass
            else:
                list.append(__)

    return len(list)

print(case_counts("Kwai Tsing"))