import pymongo
import pandas as pd
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH = "aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print("Rows and colums", {df.shape})


# convert dataframe to json so that we can dump these records
df.reset_index(drop=True,inplace=True)
json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])

# insert converted 

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)