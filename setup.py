import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'rb') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-easy-uploader',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple Django app to uploader',
    long_description=README.decode(),
    url='https://torina.top/main/293/',
    author='toritoritorina',
    author_email='toritoritorina@gmail.com',
)