FROM python:3.9

RUN mkdir /tweetapp
WORKDIR /tweetapp

COPY ./requirements.txt ./requirements.txt
#EXPOSE 8000
RUN pip install --no-cache-dir --upgrade -r /tweetapp/requirements.txt

COPY ./app /tweetapp/app

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
