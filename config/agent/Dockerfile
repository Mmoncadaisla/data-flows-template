FROM prefecthq/prefect:2.7.6-python3.11

COPY requirements.txt .
COPY setup.py .

RUN pip install --upgrade pip setuptools --no-cache-dir
RUN pip install --trusted-host pypi.python.org --no-cache-dir .

ARG PREFECT_API_KEY
ENV PREFECT_API_KEY=$PREFECT_API_KEY

ARG PREFECT_API_URL
ENV PREFECT_API_URL=$PREFECT_API_URL

ENV PYTHONUNBUFFERED True

COPY dataflows/flows/ /opt/prefect/flows/

RUN prefect block register -m prefect_gcp

ENTRYPOINT ["prefect", "agent", "start", "-q", "default"]
