# from root:
# docker build . -f weather_api/Dockerfile -t weather_api
# docker run -p 127.0.0.1:50051:50051/tcp weather_api
# docker run --name weather_api -p 50051:50051 -d weather_api

FROM python

RUN mkdir /service

COPY weather_api/ /service/weather_api/
WORKDIR /service/weather_api
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 50051
ENTRYPOINT [ "python", "main.py" ]