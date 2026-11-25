import streamlit as st

# 建立文字輸入框，並將輸入結果存入 name 變數
name = st.text_input("請輸入姓名")

# 判斷是否有輸入內容
if name:
    st.write(f"你好，{name}！")


# 定義選項清單
option = ["國文", "英文", "數學"]
# 建立下拉選單
subject = st.selectbox("請選擇科目", option)
st.write(f"你選擇的科目是：{subject}")


mode = st.radio("分析方式", ["高於門檻", "低於門檻"])
if mode:
    st.write(f"你選擇的分析方式是: {mode}")
threshold = st.slider("分數門檻", min_value=0, max_value=100, value=60)
if threshold >= 60:
    st.write(f"你設定的分數門檻是: {threshold}")
    st.balloons()
else:
    st.write(f"你設定的分數門檻是: {threshold}")
    st.snow()
st.write(f"你設定的分數門檻是: {threshold}")
snow_only = st.checkbox("只顯示符合條件的學生", value=True)
if snow_only:
    st.write("啟動及格篩選模式，只顯示符合條件的學生")
    bonus = st.number_input("請輸入加分數", min_value=0, max_value=100, value=0)
