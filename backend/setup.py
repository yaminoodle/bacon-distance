from setuptools import setup, find_packages

setup(
    name="bacon_dist_backend",
    version="1.0",
    description="A backend with an API to calculate 'Bacon Distance'.",
    author="Binyamin Wieder",
    packages=find_packages(),
    install_requires=["polars", "fastapi[standard]"],
)
