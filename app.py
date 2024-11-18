# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model.pkl') 

# 2. 모델 설명
st.title('청소년 알코올 소비량 예측')
col1, col2 = st.columns( 2 )      
with col1:
      st.subheader('모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 선형 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 훈련    데이터 : 278건')
      st.write(' - 테스트 데이터 : 118건')
      st.write(' - 모델 정확도 : 0.028349301794619475')

# 3. 데이터시각화
with col2:
      st.subheader('데이터시각화1')
      st.image('다운로드.png' )

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 다음을 입력하세요.. 인공지능이 당신의 알코올 소비량을 알려드립니다! ')

a = st.number_input(' 나이 입력 ', value=0)      #초기값은 0
b = st.selectbox('공지확인 입력(확인한다:0, 확인하지않는다:1', [0,1])
                                                            # 사용자가  0,1 중에 선택

if st.button('알코올 소비량 예측'):            # 사용자가 '점수예측' 버튼을 누르면
        input_data = [[a,b]]     # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다
        st.write('인공지능의 예측 알코올 소비량은', p)
