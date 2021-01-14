FROM python:3.8.7-buster as builder

WORKDIR /usr/src/wheels

COPY requirements.txt ./
RUN pip install wheel && pip wheel -r requirements.txt

FROM python:3.8.7-slim-buster

RUN groupadd -g 61000 app && useradd -g 61000 -l -M -s /bin/false -u 61000 app

WORKDIR /usr/src/wheels
COPY --from=builder /usr/src/wheels /usr/src/wheels

RUN pip install -r requirements.txt -f ./ \
	&& rm -rf /usr/src/wheels \ 
	&& rm -rf /root/.cache/pip/*

WORKDIR /usr/src/app
COPY src/ ./
USER app
CMD [ "python", "app.py" ]
