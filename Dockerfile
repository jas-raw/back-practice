FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /usr/src/app
COPY ./ /usr/src/app
RUN pip install -r ./requirements.txt

ENTRYPOINT ["uvicorn", "main:app"]
