FROM prefecthq/prefect:2.7.6-python3.11

COPY ./requirements.txt .
COPY ./setup.py .

RUN pip install --upgrade pip setuptools --no-cache-dir
RUN pip install --trusted-host pypi.python.org --no-cache-dir .
