import streamlit as st
import pandas as pd

st.title('게임 캐릭터의 인지도')

data = pd.DataFrame({
    '캐릭터': ['전사','법사','힐러','탱커','랜덤'],
    '선택횟수': [120, 95, 123, 20, 80],
    '승률 (%)': [52, 13, 60, 49, 90],
    "인지도 (%)": [25, 20, 30, 13, 24]
})

st.dataframe(data, use_container_width=True)
# edited_data = st.data_editor(data)
# st.write(edited_data)

st.bar_chart(data.set_index('캐릭터')['선택횟수'])
st.line_chart(data.set_index('캐릭터')['승률 (%)'])
fig = data.plot.pie(
    y='인지도 (%)',
    labels=data['캐릭터'],
    autopct='%1.1f%%',
    figsize=(6, 6),
    legend=False,
    title="캐릭터 별 인지도"
).get_figure()
st.pyplot(fig)