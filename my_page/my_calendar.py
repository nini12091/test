import streamlit as st
from datetime import datetime
import pandas as pd

st.title("🌤️ Sky Plan Scheduler")

if "current_page" not in st.session_state:
    st.session_state.current_page = "전체 일정"

menu = ["전체 일정", "plan 추가"]
choice = st.sidebar.selectbox("메뉴", menu, index=menu.index(st.session_state.current_page))

st.session_state.current_page = choice

if "schedule_data" not in st.session_state:
    st.session_state.schedule_data = pd.DataFrame(columns=["Title", "Location", "All Day", "Start Date", "End Date", "Repeat"])

if choice == "plan 추가":

    cols = st.columns([1, 4, 1])
    with cols[2]:
        if st.button("일정 확인", key="go_to_add_plan_button"):
            st.session_state.current_page = "전체 일정"

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
        if st.button("입력 완료", key="add_plan_button"):
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

elif choice == "전체 일정":

    cols = st.columns([1, 4, 1])
    with cols[2]:
        if st.button("일정 추가", key="go_to_view_button"):
            st.session_state.current_page = "plan 추가"

    st.subheader("📖 전체 일정")

    if st.session_state.schedule_data.empty:
        st.info("추가된 일정이 없습니다. 새 일정을 추가하세요.")

    else:
        st.dataframe(st.session_state.schedule_data)
        priority_data = st.session_state.schedule_data[["Title", "priority"]].set_index("Title").sort_values("priority", ascending=False)
        st.write("")
        st.subheader("우선 순위 그래프")
        st.line_chart(priority_data)