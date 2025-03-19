from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

class AzureConnector:
    def __init__(self, account_name, account_key):
        self.account_url = f"https://{account_name}.blob.core.windows.net"
        self.blob_service_client = BlobServiceClient(
            account_url=self.account_url,
            credential=account_key
        )

    def read_parquet(self, container_name, blob_name):
        # 获取 container 和 blob
        container_client = self.blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        
        # 下载 Parquet 文件为二进制流
        download_stream = blob_client.download_blob()
        
        # 直接读取为 DataFrame（依赖 pyarrow 或 fastparquet）
        return pd.read_parquet(io.BytesIO(download_stream.readall()), engine='pyarrow')
