FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install requests cachetools fastapi uvicorn
COPY . /app
EXPOSE 5000
CMD [ "python", "main.py" ]