# 분류 모델 웹앱 만들기

import streamlit as st
import joblib

# 1. 기계학습 모델 파일 로드
model = joblib.load('linear_regression_model.pkl') 

# 2. 모델 설명
st.title('청소년 알코올 소비량 예측')
col1, col2, col3 = st.columns(3)      
with col1:
    st.subheader('모델 설명 ')
    st.write(' - 기계학습 알고리즘 : 선형 회귀 ')
    st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
    st.write(' - 훈련 데이터 : 278건')
    st.write(' - 테스트 데이터 : 118건')
    st.write(' - 모델 정확도 : 0.028349301794619475')

# 3. 데이터시각화
with col2:
    st.subheader('데이터시각화1')
    st.image('다운로드.png')
with col3:
    st.subheader('데이터시각화2')
    st.image('______1_.png')

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 다음을 입력하세요.. 인공지능이 당신의 알코올 소비량을 알려드립니다!')

# 나이 입력
a = st.number_input('나이 입력', min_value=1, value=1)

# 성별 입력 (M은 0, F는 1로 처리)
b = st.selectbox('성별 입력 (남성:M, 여성:F)', ['M', 'F'])

# 성별을 0 (남성) 또는 1 (여성)로 변환
b = 0 if b == 'M' else 1

# 알코올 소비량 예측 버튼
if st.button('알코올 소비량 예측'):
    input_data = [[a, b]]  # 나이와 성별을 모델에 맞게 2D 배열로 입력
    p = model.predict(input_data)  # 예측값 반환
    st.write(f'인공지능의 예측 알코올 소비량은: {p[0]:.2f}')

st.subheader('*사용 목적 용도 외에는 사용하지 않는다*')
