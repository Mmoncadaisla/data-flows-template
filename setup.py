from setuptools import setup, find_packages

setup(
    name="data-flows",
    version="0.0.1",
    description="Data flows template",
    url="https://github.com/Mmoncadaisla/data-flows",
    author="Mmoncadaisla",
    author_email="mmoncadaisla@gmail.com",
    license="BSD 2-clause",
    packages=find_packages(),
    install_requires=[
        "prefect==2.7.5",
        "prefect-gcp==0.2.1",
        "prefect-dask==0.2.2",
    ],
    classifiers=[],
)
