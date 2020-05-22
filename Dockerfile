FROM lambci/lambda:build-python3.8

WORKDIR /app/

ADD ./ ./

RUN docker/deploy-web.sh

EXPOSE 80

ENTRYPOINT ["docker/run-web.sh"]
