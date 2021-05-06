FROM python:3

RUN apt update && apt install nano
# install the flask 
RUN pip install flask

# install the psycopg
RUN pip install psycopg2

WORKDIR /app

ADD . /app

#COPY requirements.txt /app/requirements.txt

#RUN pip install -r requirements.txt

EXPOSE 5431

# CMD ["flask"]

ENTRYPOINT ["python", "main.py"]


# docker build -t ubuntu_py3.6 .
# docker run -it --rm --add-host="localhost:192.168.1.9" -p 5000:5000 --name demo ubuntu_py3.6 bash