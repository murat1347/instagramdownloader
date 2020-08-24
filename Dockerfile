FROM rcarmo/alpine-python:3.5

RUN pip install youtube_dl

RUN pip install BeautifulSoup4

RUN pip install --upgrade autopep8

RUN pip install Django

RUN apk add --update --no-cache wget ffmpeg 

ADD insta.py /

ADD index.html /

CMD ["python", "-u","insta.py","index.html"]
