FROM python:alpine3.7
COPY app /opt/app
WORKDIR /opt/app
RUN pip install -r ./requirements.txt
EXPOSE 3000 8500
CMD ["python", "app.py"]
