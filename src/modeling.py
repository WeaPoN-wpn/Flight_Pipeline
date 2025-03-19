import os
import pandas as pd
import joblib
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from src import model_registry
import argparse

MODEL_DIR = './models'

def train_and_save(data_path):
    print(f"加载数据：{data_path}")
    df = pd.read_parquet(data_path)

    features = ['CRSDepHour', 'CRSArrHour', 'Airline', 'Origin', 'Dest', 'DepDelay', 'TaxiOut']
    target = 'ArrDelayMinutes'

    X, y = df[features], df[target]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # linear regression for testing
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    try:
        from sklearn.metrics import root_mean_squared_error
        rmse = root_mean_squared_error(y_test, y_pred)
    except ImportError:
        rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)
    print(f"Linear Regression 训练完成 | RMSE: {rmse:.2f}, R2: {r2:.4f}")

    os.makedirs(MODEL_DIR, exist_ok=True)
    model_file = os.path.join(MODEL_DIR, f"linear_model.joblib")
    scaler_file = os.path.join(MODEL_DIR, f"linear_scaler.joblib")
    joblib.dump(model, model_file)
    joblib.dump(scaler, scaler_file)

    model_registry.register_model(
        model_name="linear_model",
        model_type="linear",
        metrics={"rmse": rmse, "r2": r2},
        path=model_file
    )
    print(f"Linear Regression 模型已保存为 {model_file}")

def main():
    parser = argparse.ArgumentParser(description="Linear Regression 模型训练")
    parser.add_argument('--data_path', default='./data/processed_data.parquet', help='数据文件路径')
    args = parser.parse_args()

    if not os.path.exists(args.data_path):
        print(f"找不到数据文件 {args.data_path}，请先运行 ETL")
        return

    train_and_save(args.data_path)

if __name__ == "__main__":
    main()
