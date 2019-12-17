###
# Env Targets
###
LOCAL_NAMES='127.0.0.1 apy.local express.local'

configure:
	grep -qxF ${LOCAL_NAMES} /etc/hosts || echo '${LOCAL_NAMES}' >> /etc/hosts

###
# Docker Targets
###
build-all:
	make build-apy; make build-nginx

rm-all:
	make rm-apy; make rm-apy

build-apy:
	docker build -t apy app/ -f app/docker/python.Dockerfile

rm-apy:
	docker image rm apy

build-nginx:
	docker build -t nginx_amplify nginx -f nginx/docker/nginx.Dockerfile

rm-apy:
	docker image rm nginx_amplify

###
# Compose Targets
###
compose: docker-compose.yml
	docker-compose up --detach --build

decompose: docker-compose.yml
	docker-compose down --volumes

debug:
	docker-compose up --force-recreate --always-recreate-deps --build --abort-on-container-exit

clean-build:
	make clean; make compose

clean:
	make decompose; make rm-all

restart:
	docker-compose restart --timeout 0

###
# App Targets
###
gncn:
	 cd app/ && gunicorn -w 4 --bind 0.0.0.0:5000 run:app

dep:
	cd app/ && pipreqs --print && pip3 install -r requirements.txt

###
# Test Targets
###
nm:
	newman run test/newman/apy.postman_collection.json -e test/newman/apy.postman_environment.json

curl:
	curl -w "@test/curl/curl-format.txt" -o /dev/null -s "http://localhost/?m=message" && curl -w "@test/curl/curl-format.txt" -o /dev/null -s "http://apy.local/?m=message"

ab:
	ab -n 10000 -c 1000 -r "http://apy.local/?m=message"