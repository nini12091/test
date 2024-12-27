import streamlit as st
from datetime import datetime
import pandas as pd

cols = st.columns([1, 4, 1])
with cols[2]:
    if st.button("일정 확인", key="go_to_add_plan_button"):
        st.session_state.current_page = "plan 보기"

    st.subheader("📅 일정 추가")

    title = st.text_input("Title", placeholder="제목을 입력하세요")
    location = st.text_input("Location", placeholder="장소를 입력하세요")
    all_day = st.checkbox("All Day", key="all_day_checkbox")
    start_date = st.date_input("Start Date", datetime.now(), key="start_date_input")
    end_date = st.date_input("End Date", datetime.now(), key="end_date_input")
    repeat_options = ['안 함', '매일', '매주', '2주마다', '매월', '매년', '사용자화']
    repeat = st.selectbox("반복", repeat_options, key="repeat_selectbox")
    impact = st.number_input("중요도", step=1, format="%d", placeholder="숫자로 입력 (1~)")

    cols = st.columns([1, 4, 1])
    with cols[2]:
        if st.button("일정 추가", key="add_plan_button"):
            if title and location:
                new_data = pd.DataFrame({
                    "Title": [title],
                    "Location": [location],
                    "All Day": [all_day],
                    "Start Date": [start_date],
                    "End Date": [end_date],
                    "Repeat": [repeat],
                    "priority": [impact]
                })

                st.session_state.schedule_data = pd.concat(
                    [st.session_state.schedule_data, new_data],
                    ignore_index=True
                )
                st.success(f"일정 '{title}'이(가) 추가되었습니다!")
            else:
                st.error("제목과 장소를 입력하세요!")