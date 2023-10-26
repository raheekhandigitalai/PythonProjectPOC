# Community Code - Mobile - Python Starter Project
This project demonstrates how to write tests for Continuous Testing Cloud using Python. Once cloned and set up properly, it runs as is.

## Setting Up the Sample Project


1. Set up authentication by updating access key in [cloud.properties](cloud.properties):
    * accessKey -  Personal authentication. See [Obtaining Access Key](https://docs.experitest.com/pages/viewpage.action?pageId=52593435) to learn how to obtain an access key.
1. Make sure that Python 3 is installed on your machine
1. Setup local environment with dependencies
```bash
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Running Tests
To run iOS Native Test in this project, run this on the command line: 

```bash
python3 -m unittest test/native_demo/test_ios_native_demo.py
```

To run Android Native Test in this project, run this on the command line:

```bash
python3 -m unittest test/native_demo/test_android_native_demo.py
```
