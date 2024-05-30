import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.title('**채식을 좋아하는 사람을 위한 공간**')

col1, col2 = st.columns([2, 3])

with col1:
    st.subheader('서울시 기준')

with col2:
    st.subheader('채식주의자에 대해')
    if st.checkbox('채식주의자란?', key='checkbox1'):
        st.write('채식주의적 식습관을 가진 사람을 말한다.')
    else:
        st.write(' ')
with col2:
    if st.checkbox('채식주의자 종류는?', key='checkbox2'):
        img111 = Image.open('image111.png')
        st.image(img111)
    else:
        st.write(' ')

# 링크를 포함한 텍스트 추가
st.markdown("[출처](https://data.seoul.go.kr/dataList/OA-2741/S/1/datasetView.do)")

# HTML 파일 경로
file_path = 'seoul.html'

# HTML 파일 내용 읽기
with open(file_path, 'r', encoding='utf-8') as f:
    html_string = f.read()

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
tab1, tab2, tab3, tab4 = st.tabs(['워드클라우드' , '채식 이유', '채식 언급량', '지도'])

with tab1:
    #tab A 를 누르면 표시될 내용
    st.write('채식 관련 단어')
    img1 = Image.open('word.png')
    st.image(img1)
    
with tab2:
    #tab B를 누르면 표시될 내용 
    st.write('채식을 시작하게 된 이유')
    img2 = Image.open('why.png')
    st.image(img2)
  
with tab3:
    #tab B를 누르면 표시될 내용 
    st.write('채식 단어 언급량 상승')
    img3 = Image.open('word2.png')
    st.image(img3)

with tab4:
    # tab B를 누르면 표시될 내용 
    components.html(html_string, height=600)