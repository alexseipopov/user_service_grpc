from setuptools import setup, find_packages

setup(
    name='user_service_grpc',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "grpcio",
        "grpcio-tools"
    ],
)