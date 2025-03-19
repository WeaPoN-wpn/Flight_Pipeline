import os
import argparse
from src.azure_connector import AzureConnector
from src.data_processor import clean_data, feature_engineering
import pandas as pd

def etl_pipeline(account_name, account_key, container, blob, output_path='./data/processed_data.parquet'):
    connector = AzureConnector(account_name, account_key)
    df_raw = connector.read_parquet(container, blob)

    print(f"成功从 Azure 加载数据，shape: {df_raw.shape}")

    # 数据清洗和特征工程
    df_clean = clean_data(df_raw)
    df_processed = feature_engineering(df_clean)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_processed.to_parquet(output_path)
    print(f"ETL 完成！已保存至 {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Azure ETL Pipeline")
    parser.add_argument("--account_name", required=True, help="Azure storage account name")
    parser.add_argument("--account_key", required=True, help="Azure storage account key")
    parser.add_argument("--container", required=True, help="Azure blob container name")
    parser.add_argument("--blob", required=True, help="Azure blob file name")
    parser.add_argument("--output_path", default="./data/processed_data.parquet", help="Local output file path")

    args = parser.parse_args()

    etl_pipeline(
        account_name=args.account_name,
        account_key=args.account_key,
        container=args.container,
        blob=args.blob,
        output_path=args.output_path
    )