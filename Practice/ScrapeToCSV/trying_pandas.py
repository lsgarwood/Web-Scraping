import pandas as pd

bid_data = []
for obj in list:
    obj= {
        "bid_data_0" :bid_data[0],
        "bid_data_5" :bid_data[5],
        "bid_data_6" :bid_data[6],
        "bid_data_10" :bid_data[10],
        "bid_data_12" :bid_data[16],
        "bid_data_17" :bid_data[17]
    }
bid_data.append(obj)

bid_data = pd.DataFrame(bid_data)
bid_data.to_csv("file_name.csv", index=True, encoding='utf-8')