# Olist E-commerce 데이터 분석 프로젝트

브라질 이커머스 플랫폼 [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)의 공개 데이터셋을 활용한
데이터 분석가(Data Analyst) 취업 준비용 SQL/DB 프로젝트입니다.

## 프로젝트 목표
- 실제 서비스에 가까운 다중 테이블 관계형 데이터를 다뤄보며 SQL 분석 역량 강화
- 비즈니스 질문 정의 → SQL 쿼리 작성 → 인사이트 도출 → 시각화까지 전 과정 경험
- 포트폴리오로 활용 가능한 분석 리포트 작성

검증할 가설: **거주 지역에 따라 배송 소요 시간이 다르고, 그것이 리뷰 평점에 영향을 준다.**

## 데이터셋
- 출처: [Kaggle - Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- 원본 CSV 파일은 용량 문제로 저장소에 포함하지 않았습니다. 위 링크에서 다운로드 후
  `archive/` 폴더에 압축을 풀어 사용하세요.
- 구성 (9개 테이블): 고객(customers), 주문(orders), 주문 상세(order_items),
  결제(order_payments), 리뷰(order_reviews), 상품(products), 판매자(sellers),
  지리정보(geolocation), 카테고리명 번역(product_category_name_translation)

## 사용 기술
- **DuckDB**: 로컬 SQL 분석 엔진 (설치 부담 없이 빠르게 시작)
- **SQL**: 모든 집계와 검증은 SQL로 수행하며 pandas로 우회하지 않습니다
- **Python**: 노트북 실행과 시각화

## 노트북

| 노트북 | 내용 |
|---|---|
| [`01_data_exploration`](notebooks/01_data_exploration.ipynb) | 원본 CSV 9개의 컬럼·타입·행 수와 샘플 데이터 확인 |
| [`02_load_tables`](notebooks/02_load_tables.ipynb) | CSV를 DuckDB 파일에 영구 테이블로 적재하고 원본과 행 수 대조 |
| [`03_data_quality`](notebooks/03_data_quality.ipynb) | 테이블 구조와 관계 점검 — 그레인·키 확정, 참조 무결성, 카디널리티, 중복 |

### 03에서 확인한 것

조인해서 집계해도 결과가 틀어지지 않는지를 데이터로 확인했습니다.
컬럼 설명과 ERD는 후보를 세우는 데만 참고하고, 확정은 전부 쿼리 결과로 판단했습니다.

- `order_items` 에는 수량 컬럼이 없습니다. 같은 상품을 여러 개 사면 행이 그 개수만큼
  생기므로, 주문 수량은 `COUNT(*)`, 상품 금액은 `SUM(price)` 로 구해야 합니다.
- 한 주문에 리뷰가 2건 이상 달린 경우가 547건 있습니다. `orders` 에 그대로 조인하면
  리뷰가 달린 주문 98,673건이 99,224행으로 늘어납니다.
- 품목 기록이 없는 주문 775건은 배송된 것이 하나도 없습니다.
  결제까지 마쳤으나 상품을 확보하지 못해 무산된 주문이며, 그중 756건에는 리뷰가 달려 있습니다.
- 같은 도시명이 서로 다른 주에 존재합니다. 도시 4,119개에 `(도시, 주)` 조합은 4,310개이므로,
  도시 단위 집계는 반드시 주와 함께 묶어야 합니다.
- `geolocation` 은 자연 키가 없고 완전 중복 행이 26만 건입니다. 이 프로젝트는 좌표·거리를
  다루지 않고 주·도시는 `customers`·`sellers` 가 자체 보유하므로 사용하지 않습니다.

## 진행 상황
- [x] 데이터셋 준비
- [x] 분석 환경 세팅 (DuckDB)
- [x] 원본 데이터 탐색
- [x] DuckDB 적재 및 행 수 검증
- [x] 데이터 품질 점검 (1) — 테이블 구조와 관계
- [ ] 데이터 품질 점검 (2) — 결측과 분석 표본
- [ ] 가설 검증 — 지역별 배송 소요 시간과 리뷰 평점의 관계
- [ ] 결과 시각화 및 리포트 작성

## 폴더 구조
```
.
├── archive/       # 원본 CSV 데이터 (git 미포함)
├── notebooks/     # 분석 노트북
├── olist.duckdb   # 적재된 분석용 DB (git 미포함)
├── README.md
└── .gitignore
```
