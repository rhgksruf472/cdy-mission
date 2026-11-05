# 베이스 이미지: 웹 서버(nginx)가 이미 들어 있는 가벼운 버전(alpine)을 가져온다
FROM nginx:alpine

# 이미지에 이름표(메타데이터)를 붙인다 (이미지 안의 동작은 안 바뀜)
LABEL org.opencontainers.image.title="my-custom-nginx"

# 환경 변수 하나를 추가한다 (컨테이너 안에서 APP_ENV=dev 로 보임)
ENV APP_ENV=dev

# 내 컴퓨터의 site/ 폴더 파일을 nginx가 웹페이지를 찾는 위치로 복사한다 (기본 페이지를 내 것으로 교체)
COPY site/ /usr/share/nginx/html/
