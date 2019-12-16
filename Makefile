###
# Dev Targets
###

LOCAL_NAMES='127.0.0.1 apy.local express.local'

configure:
	grep -qxF ${LOCAL_NAMES} /etc/hosts || echo '${LOCAL_NAMES}' >> /etc/hosts

###
# Docker Targets
###
build:
	docker build -t apy_web . -f python.Dockerfile

rm:
	docker image rm apy_apy

###
# Compose Targets
###
compose: docker-compose.yml
	docker-compose up --detach --always-recreate-deps --build

decompose: docker-compose.yml
	docker-compose down

debug:
	make decompose; make rm; docker-compose up --force-recreate --always-recreate-deps --build --abort-on-container-exit

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
newman:
	newman run test/newman/apy.postman_collection.json -e test/newman/apy.postman_environment.json

curl:
	curl -w "@test/curl/curl-format.txt" -o /dev/null -s "http://localhost/?m=message" && curl -w "@test/curl/curl-format.txt" -o /dev/null -s "http://apy.local/?m=message"

ab:
	ab -n 10000 -c 1000 -r "http://apy.local/?m=message"