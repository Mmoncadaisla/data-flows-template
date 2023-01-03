from setuptools import setup, find_packages


def get_version():
    _version = {}
    with open("data-flows/_version.py") as fp:
        exec(fp.read(), _version)
    return _version["__version__"]


setup(
    name="data-flows",
    version=get_version(),
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
