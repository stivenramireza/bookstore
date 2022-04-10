FROM python:3.8.12-alpine3.14
WORKDIR /books
ENV MONGO_URI ${MONGO_URI}
COPY requirements.txt .
COPY app.py .
RUN pip install -r requirements.txt
CMD ["waitress-serve", "--call", "app:create_app"]
