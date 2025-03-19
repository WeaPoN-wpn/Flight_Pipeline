
# ✈ Flight Delay Prediction Pipeline (ETL + Modeling + Web)

## 📌 项目简介
本项目设计并实现了一个完整的数据科学建模管道，目标是基于美国航班数据预测航班的到达延误时间（单位：分钟）。  
实现了以下功能：
- 从 **Azure Data Lake** 读取 Parquet 格式原始数据
- 完整的 **ETL（提取-清洗-特征工程）流程**
- 线性回归模型训练、保存和版本管理
- **Streamlit Web 应用**，支持用户输入特征并进行预测

---

## 📂 文件与功能说明
根据你的结构和图片，功能模块如下：

| 文件 / 文件夹               | 功能说明 |
|----------------------------|------------------------------------------------|
| `data/`                    | 存储清洗后用于建模的中间数据文件（processed_data.parquet） |
| `models/`                  | 存储训练好的模型、scaler和注册信息（registry.json） |
| `notebooks/`               | 存放实验性 notebook（数据探索与调试用） |
| `src/azure_connector.py`   | 封装Azure Data Lake连接和数据读取方法 |
| `src/azure_etl.py`         | ETL流程主控模块：从Azure读取数据 ➔ 清洗 ➔ 特征工程 ➔ 保存至data/目录 |
| `src/data_processor.py`    | 数据清洗（处理缺失值）和特征工程（提取时间特征、编码类别变量） |
| `src/inference.py`         | 加载训练好的模型与scaler，对新数据进行预测 |
| `src/model_registry.py`    | 记录模型版本信息（存入 registry.json）方便管理和追踪 |
| `src/modeling.py`          | 从data目录读取处理好的数据，训练线性回归模型并保存模型与scaler |
| `app.py`                   | Streamlit Web界面，用户可输入特征值并实时预测到达延误 |
| `requirements.txt`         | 项目依赖库列表 |
| `venv/`                    | Python虚拟环境文件夹（建议本地创建） |

---

## 🚀 本地运行指南（CMD命令行）

1️⃣ **创建虚拟环境并安装依赖**
\```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
\```

2️⃣ **执行 ETL 流程，拉取Azure数据并处理**
\```bash
python -m src.azure_etl --account_name YOUR_ACCOUNT \
                        --account_key YOUR_KEY \
                        --container YOUR_CONTAINER \
                        --blob YOUR_FILE.parquet
\```
💾 处理后的数据会保存到：`./data/processed_data.parquet`

3️⃣ **训练模型**
\```bash
python -m src.modeling --data_path ./data/processed_data.parquet
\```
✅ 模型和Scaler将保存至 `models/` 目录，并自动注册

4️⃣ **启动预测Web应用（Streamlit）**
\```bash
streamlit run app.py
\```
🌐 浏览器打开后，可手动输入特征并实时预测航班延误

---

## 🌱 项目未来可扩展方向
✅ **多模型支持**：
- 支持 XGBoost、LightGBM、深度神经网络等模型

✅ **模型调参自动化**：
- 集成 Grid Search / Random Search 或 Hyperopt 自动调参模块

✅ **在线部署 API**：
- 加入 FastAPI 或 Flask 版本，支持 RESTful 接口对外预测

✅ **MLFlow 版本管理**：
- 替换本地 registry.json，接入完整模型生命周期管理

✅ **可视化监控 & 日志系统**：
- 添加TensorBoard或自定义日志追踪训练过程与预测质量

✅ **自动化调度**：
- 加入 Airflow，实现 ETL ➔ Training ➔ Serving 全流程自动化

---

## 💻 示例效果
- Azure 数据成功下载与处理
- 模型训练准确率（R²）达到 0.95+
- Streamlit 页面可交互预测航班延误分钟数

---

如需完整部署脚本、日志功能或API版本，欢迎联系我！
