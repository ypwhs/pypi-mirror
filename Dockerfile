FROM python:3.6-slim-stretch
WORKDIR /app
RUN python -m pip --no-cache-dir install --upgrade \
    -i https://mirrors.aliyun.com/pypi/simple/ \
    bandersnatch
ENV INTERVAL 3600
ENV CMD "bandersnatch -c bandersnatch.conf mirror"
COPY . .
CMD ["python", "/app/runner.py"]
