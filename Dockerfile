FROM python:3.10-slim


# System setup
RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install -y --no-install-recommends \
    git \
    ssh-client \
    software-properties-common \
    make \
    build-essential


RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

# Env vars
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV DAGSTER_HOME=/opt/dagster/dagster_home/

# Copy our code and workspace to /usr/src/app
COPY kelihi_dbt /opt/dagster/app/kelihi_dbt
# Copy requirements.txt to /usr/src
COPY requirements.txt /opt/dagster/app/requirements.txt

# Install dependencie
RUN pip install --upgrade pip
RUN pip install -r /opt/dagster/app/requirements.txt


WORKDIR /opt/dagster/app/kelihi_dbt/kelihi_dagster

EXPOSE 3000

ENTRYPOINT ["dagster", "dev", "-h", "0.0.0.0", "-p", "3000"]