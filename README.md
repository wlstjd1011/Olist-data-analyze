# Olist E-commerce 데이터 분석 프로젝트

브라질 이커머스 플랫폼 [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)의 공개 데이터셋을 활용한
데이터 분석가(Data Analyst) 취업 준비용 SQL/DB 프로젝트입니다.

## 프로젝트 목표
- 실제 서비스에 가까운 다중 테이블 관계형 데이터를 다뤄보며 SQL 분석 역량 강화
- 비즈니스 질문 정의 → SQL 쿼리 작성 → 인사이트 도출 → 시각화까지 전 과정 경험
- 포트폴리오로 활용 가능한 분석 리포트 작성

## 데이터셋
- 출처: [Kaggle - Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- 원본 CSV 파일은 용량 문제로 저장소에 포함하지 않았습니다. 위 링크에서 다운로드 후
  `archive/` 폴더에 압축을 풀어 사용하세요.
- 구성 (9개 테이블): 고객(customers), 주문(orders), 주문 상세(order_items),
  결제(order_payments), 리뷰(order_reviews), 상품(products), 판매자(sellers),
  지리정보(geolocation), 카테고리명 번역(product_category_name_translation)

## 사용 기술
- **DuckDB**: 로컬 SQL 분석 엔진 (설치 부담 없이 빠르게 시작)
- **Python**: 데이터 적재 및 분석 스크립트

## 진행 상황
- [x] 데이터셋 준비
- [x] 분석 환경 세팅 (DuckDB)
- [ ] 스키마 설계 / ERD 작성
- [ ] 데이터 적재
- [ ] 비즈니스 질문 정의 및 SQL 분석
- [ ] 결과 시각화 및 리포트 작성

## 폴더 구조
```
.
├── archive/    # 원본 CSV 데이터 (git 미포함)
├── README.md
└── .gitignore
```
