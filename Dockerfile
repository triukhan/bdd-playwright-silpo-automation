FROM mcr.microsoft.com/playwright/python:latest
LABEL maintainer="danylotriukhan@gmail.com"

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN playwright install

CMD ["pytest", "tests", "--alluredir=allure-results", "-v"]