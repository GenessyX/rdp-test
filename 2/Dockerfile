FROM python

WORKDIR /src/app

COPY . /src/app

RUN apt-get update -y
RUN apt-get install libpcap-dev -y
RUN pip install -r requirements.txt

CMD [ "python", "interceptor.py" ]