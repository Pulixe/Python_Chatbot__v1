FROM python:3.8.10-slim


# File Author / Maintainer
LABEL maintainer="francisco.pulice@outlook.com"

WORKDIR /opt/ia/api/v1/BOT

RUN pip install --upgrade tensorflow

COPY . /opt/ia/api/v1/BOT/
RUN pip install -r req.txt
ENV NLTK_DATA /nltk_data/
ADD . $NLTK_DATA

#EXPOSE 8080

ENTRYPOINT python main.py
