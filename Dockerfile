FROM phiwal/py3.5-tensorflow-opencv
MAINTAINER DataBox <p.yadav@acm.org>

ADD .  /cam

WORKDIR /cam

RUN echo "Hello User!"

RUN pip3 install -r ./requirements.txt

EXPOSE 5000

#LABEL databox.type="driver"

ENTRYPOINT ["python3"]
CMD ["-u", "camreader.py" ]
