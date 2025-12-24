from dotenv import load_dotenv
load_dotenv()          

import boto3
import os

s3_client = boto3.client('s3')
bucket_name = 'amdari-retailio-bucket'

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "data")

datasets = {
    "products": os.path.join(data_dir, "products.csv"),
    "sales":    os.path.join(data_dir, "sales.csv")
}

for name, path in datasets.items():
    if os.path.exists(path):
        with open(path, 'rb') as f:
            s3_client.upload_fileobj(f, bucket_name, f"raw/{name}/{os.path.basename(path)}")
        print(f"Uploaded {name}.csv")
    else:
        print(f"Missing: {path}")