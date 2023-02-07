# 내 방 어디? v1(~2023.02.01)
[내 방 어디? 링크](https://seungkyu37-project2-app-3b4qng.streamlit.app/)
![screensh](img/홈페이지.png)

## 목적
계약일 기준 2022년 1월 1일부터 2023년 1월 30일까지의 **서울시 전/월세 실거래 데이터 기반 검색** 및 **전세 시세 예측** 웹 개발

## 주요 기능
- 홈페이지
    - 실거래 현황(최신순)
    - 월세 실거래 수 지역 순위(top10)
    - 전세 실거래 수 지역 순위(top10)
- 전월세 검색페이지
    - 해당구, 해당동, 전/월세 구분 검색
    - 보증금, 월세, 임대면적 슬라이더 검색
- 전세 예측페이지
    - 지역 선택 후 날짜에 따른 보증금 막대그래프로 시각화
- 건의사항페이지
    - 게시판 작성자, 이메일, 제목, 내용 저장을 위한 db 구축
    - 문의 내용 작성칸 구축
    - 게시판 목록 구현

## 설치 방법
### Windows
+ 버전 확인 
    - vscode : 1.74.1
    - python : 3.9.13
    - 라이브러리 :  pandas (1.5.3), numpy (1.24.1), plotly (5.13.0), matplotlib (3.6.3), streamlit (1.17.0), streamlit-option-menu (0.3.2), geopandas (0.12.2), google-cloud-bigquery(3.5.0), pandas-gbq(0.19.1), pydeck(0.8.0), yfinance(0.2.9), stqdm(0.0.5), prophet(1.1.2), seaborn(0.12.2)

+ 주요 라이브러리 설치
    - `pip install numpy, pandas, plotly, matplotlib, streamlit, streamlit-option-menu, geopandas, google-cloud-bigquery, pandas-gbq, pydeck, yfinance, stqdm, prophet, seaborn

# 내방 어디? v2(2023.02.02~)

## 주요 기능 업데이트 내용
- 홈페이지
    - 전세 월평균, 월세 월평균 추이 꺾은선그래프 <span style="color:blue">시각화</span>
    - 월세, 전세 실거래 수 지역 순위 막대그래프 <span style="color:blue">시각화</span>
    
- 전월세 검색페이지
    - 전/월세 구분 검색 중 모두 검색할 수 있도록 <span style="color:blue">추가</span>
    - 보증금, 월세, 임대면적 최소/최대값 정해줄 수 있도록 <span style="color:blue">추가</span>
    - 보증금, 월세, 임대면적 최소/최대값과 슬라이더값 <span style="color:blue">동기화</span>

- 전세 예측페이지
    - 날짜 선택 후 지역구별 평균 실거래가 지도 <span style="color:blue">시각화</span>

- 건의사항페이지
    - 처리 상태 <span style="color:blue">추가</span>
    - 빈칸 입력시 에러메시지 <span style="color:blue">추가</span>
    - 관리자 기능
        - 처리 상태 변경 기능 <span style="color:blue">추가</span>
    - 검색 기능
        - 제목, 작성자명, 내용에 같은 내용 검색 기능 <span style="color:blue">추가</span>

# 내방 어디? v3(2023.02.07~)

## 주요 기능 업데이트 내용
- 홈페이지
    - 전세 월평균, 월세 월평균 추이 꺾은선그래프 <span style="color:red">삭제</span>
    - 월세, 전세 실거래 수 지역 순위 막대그래프 <span style="color:red">삭제</span>

- 전세 예측페이지
    - 전세 월평균, 월세 월평균 추이 꺾은선그래프 <span style="color:blue">시각화</span>
    - 월세, 전세 실거래 수 지역 순위 막대그래프 <span style="color:blue">시각화</span>
    - 날짜 선택 후 지역구별 평균 실거래가 지도 <span style="color:blue">시각화</span>
    - 원하는 구 선택 후 전세 예측 모델 <span style="color:blue">추가</span>