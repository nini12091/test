import streamlit as st

pages = {
    "Home": [
        st.Page("my_page.py", title="sky_blog"),
    ],
    "일정": [
        st.Page("my_calendar.py", title="sky_calendar"),
    ]
}

pg = st.navigation(pages)
pg.run()