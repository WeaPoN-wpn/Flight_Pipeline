import streamlit as st
from src.inference import load_model_and_predict

st.title("✈️ 航班延误预测系统")
st.write("请填写以下信息，预测航班到达延误（分钟）")

user_input = {
    "CRSDepHour": st.number_input("计划起飞小时（0-23）", 0, 23),
    "CRSArrHour": st.number_input("计划到达小时（0-23）", 0, 23),
    "Airline": st.number_input("航空公司编码（数字编码）"),
    "Origin": st.number_input("起飞机场编码（数字编码）"),
    "Dest": st.number_input("到达机场编码（数字编码）"),
    "DepDelay": st.number_input("起飞延误时间（分钟）"),
    "TaxiOut": st.number_input("滑行时间（分钟）")
}

model_type = st.selectbox("选择模型", ["linear", "other models, but not implemented yet"])

if st.button("预测"):
    result = load_model_and_predict(model_type, user_input)
    st.success(f"预测到达延误时间：{result:.2f} 分钟")