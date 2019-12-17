FROM nginx:1.16.1

LABEL maintainer="ElDiabloRojo <holdens.uk@googlemail.com>"
LABEL nginx_version="1.16.1"
LABEL version="1.6"
LABEL description="Nginx & Amplify docker image for apy."

# Install the NGINX Amplify Agent
RUN apt-get update \
    && apt-get install -qqy curl python apt-transport-https apt-utils gnupg1 procps \
    && echo 'deb https://packages.amplify.nginx.com/debian/ stretch amplify-agent' > /etc/apt/sources.list.d/nginx-amplify.list \
    && curl -fs https://nginx.org/keys/nginx_signing.key | apt-key add - > /dev/null 2>&1 \
    && apt-get update \
    && apt-get install -qqy nginx-amplify-agent \
    && apt-get purge -qqy curl apt-transport-https apt-utils gnupg1 \
    && rm -rf /etc/apt/sources.list.d/nginx-amplify.list \
    && rm -rf /var/lib/apt/lists/*

# Keep the nginx logs inside the container
RUN touch /var/log/nginx/access.log \
    && touch /var/log/nginx/error.log \
    && chown nginx /var/log/nginx/*log \
    && chmod 644 /var/log/nginx/*log

# Copy nginx stub_status config
COPY conf.d/stub_status.conf /etc/nginx/conf.d

ENV API_KEY 1ec221f0b8ef2ae20728a6d2e46319a6

ENV AMPLIFY_IMAGENAME apy

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]