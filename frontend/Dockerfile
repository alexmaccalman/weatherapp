# from root:
# docker build . -f frontend/Dockerfile -t frontend
# docker run -p 127.0.0.1:5000:5000/tcp frontend
# docker run --name frontend -p 5000:5000 -d frontend
FROM python

RUN mkdir /service
COPY frontend/ /service/frontend/
WORKDIR /service/frontend
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt


EXPOSE 5000
ENV FLASK_APP=server.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]