# 🚌 부산 지하철 역별 이용객 수 지도 분석 앱

Streamlit과 Folium을 활용하여 부산 지하철 역별 이용객 수를 데이터 시각화하고 지도로 보여주는 웹 애플리케이션입니다.

---

## 📌 주요 기능
1. **CSV 데이터 업로드 및 조회**
   - `busan_subway.csv` 파일을 업로드하여 전체 데이터 프레임을 확인할 수 있습니다.
2. **이용객 수 상위 5개 역 표기**
   - 현재 선택된 호선 중 이용객 수가 가장 많은 상위 5개 역을 별도 표로 안내합니다.
3. **호선 필터링 (Multiselect)**
   - 1호선~4호선 중 원하는 호선만 선택하여 지도 및 표에 필터링된 결과를 확인할 수 있습니다.
4. **대화형 지도 시각화 (Folium)**
   - **원 크기**: 이용객 수의 제곱근($\sqrt{\text{이용객수}}$)에 비례하여 마커 반지름이 설정됩니다.
   - **호선별 색상**: 
     - 1호선: 주황 (Orange)
     - 2호선: 초록 (Green)
     - 3호선: 갈색 (Brown)
     - 4호선: 파랑 (Blue)
   - **인터랙션**:
     - 마우스 호버(Hover): 역명 표시
     - 마우스 클릭(Click): 해당 역의 상세 이용객 수 팝업 출력

---

## 📁 파일 구성
- `app.py`: Streamlit 메인 실행 파이썬 코드
- `requirements.txt`: 프로젝트 실행에 필요한 패키지 목록
- `README.md`: 프로젝트 설명서

---

## 🛠️ 실행 방법

### 1. 레포지토리 클론 및 이동
```bash
git clone <GitHub-Repository-URL>
cd <Repository-Name>
```

### 2. 가상환경 설정 및 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. Streamlit 앱 실행
```bash
streamlit run app.py
```