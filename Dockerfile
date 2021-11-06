FROM python:3-buster


WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD code .
RUN chmod +x run.sh
ENTRYPOINT ["./run.sh"]
CMD ["source", "dest"]