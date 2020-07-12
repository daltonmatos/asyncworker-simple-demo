FROM python:3.7-alpine

#Version: 0.1.0

ARG _=""
ENV GIT_COMMIT_HASH=${_}

WORKDIR /tmp
COPY Pipfile.lock /tmp/
COPY Pipfile /tmp/

RUN pip install -U pip==18.1 pipenv==2018.10.13 \
&& apk add --virtual .deps gcc g++ make \
&& pipenv install --system --deploy --ignore-pipfile \
&& apk del --purge .deps

COPY . /opt/app
WORKDIR /opt/app

CMD ["python", "-m", "myproj"]
