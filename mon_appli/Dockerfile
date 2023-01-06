FROM alpine
RUN apk update
RUN apk add py3-pip curl
RUN pip3 install flask
COPY app.py /opt/mon_appli/app.py
ENTRYPOINT FLASK_APP=/opt/mon_appli/app.py flask run --host=0.0.0.0