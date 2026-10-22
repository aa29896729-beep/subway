import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import math

# 1. 호선별 지정 색상 딕셔너리 (1호선: 주황, 2호선: 초록, 3호선: 갈색, 4호선: 파랑)
LINE_COLORS = {
    "1호선": "orange",
    "2호선": "green",
    "3호선": "brown",
    "4호선": "blue"
}

# 2. 앱 제목 설정
st.title("🚌 부산 지하철 역별 이용객 수 지도 분석")

# 3. CSV 파일 업로드 기능
uploaded_file = st.file_uploader("busan_subway.csv 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # 업로드한 CSV 파일 읽기
    df = pd.read_csv(uploaded_file)

    # [호선 필터] multiselect로 조회할 호선 선택 (기본값: 전체 호선 선택)
    available_lines = list(df['호선'].unique())
    selected_lines = st.multiselect("조회할 호선을 선택하세요", options=available_lines, default=available_lines)

    # 선택된 호선의 데이터만 필터링
    filtered_df = df[df['호선'].isin(selected_lines)]

    # ① 전체 데이터 표 출력
    st.subheader("📊 지하철 데이터 목록")
    st.dataframe(filtered_df)

    # [표] 이용객 수 상위 5개 역 표 출력
    st.subheader("🏆 이용객 수 상위 5개 역")
    top5_df = filtered_df.sort_values(by='이용객수', ascending=False).head(5)
    st.dataframe(top5_df[['호선', '역명', '이용객수']])

    st.subheader("🗺️ 지하철 역별 이용객 지도")

    # 지도 초기화 (부산 중심 좌표)
    m = folium.Map(location=[35.1795543, 129.0756416], zoom_start=11)

    # 필터링된 데이터(filtered_df) 기준으로 지도에 마커 추가
    for index, row in filtered_df.iterrows():
        # [색상] 해당 역의 호선에 맞는 색상 가져오기 (지정되지 않은 호선은 기본값 'gray')
        line_color = LINE_COLORS.get(row['호선'], 'gray')

        # ② 원 면적이 이용객수에 비례하도록 반지름 계산
        radius_size = math.sqrt(row['이용객수']) * 0.05

        # ②, ③ 지도 마커 생성 (색상 적용, Hover: 역명, Click: 이용객 수)
        folium.CircleMarker(
            location=[row['위도'], row['경도']],
            radius=radius_size,
            color=line_color,  # 테두리 색상
            fill=True,
            fill_color=line_color,  # 채우기 색상
            fill_opacity=0.5,
            tooltip=f"[{row['호선']}] {row['역명']}",  # ③ 마우스 Hover 시 표시
            popup=f"{row['역명']}역 이용객 수: {row['이용객수']:,}명"  # ③ 클릭 시 표시
        ).add_to(m)

    # Streamlit 화면에 지도 출력
    st_folium(m, width=700, height=500)

else:
    st.info("좌측 상단에서 'busan_subway.csv' 파일을 업로드해 주세요.")