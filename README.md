# CommunityCode-Mobile-PythonStarterProject
Start Writing tests with Continuous Testing Cloud and Python
## Cloning The Sample Project

Clone the sample project from [CommunityCode-Mobile-PythonStarterProject](https://github.com/ExperitestOfficial/CommunityCode-Mobile-PythonStarterProject) repository and navigate to the code directory as shown below:

```bash
git clone https://github.com/ExperitestOfficial/CommunityCode-Mobile-PythonStarterProject
cd CommunityCode-Mobile-PythonStarterProject
```


## Setting Up Authentication

To set up authentication, update the following parameters in [cloud.properties](cloud.properties):
* url - Url for the cloud the test would run in. For example, https://company.experitest.com/
* accessKey -  Personal authentication. See [Obtaining Access Key](https://docs.experitest.com/pages/viewpage.action?pageId=52593435) to learn how to obtain an access key.

## Running Tests

If this is the first time running the tests, set up dependencies with
```bash
pip install -r requirements.txt
```
To run all tests in this project, execute to following command line: 

```bash
python -m unittest test
```

## Upload Application to the Cloud

The example tests in this project use a demo application.
To upload your own application to cloud:
1. Log in to the cloud using a browser.
2. In the left menu click Applications.
3. Click Upload.
4. Click the application file to upload.

In your tests, change *com.experitest.ExperiBank* (and activity if needed) in desired capabilities for your application, in the following lines:

* For Android:
```
self.dc['appPackage'] = 'com.experitest.ExperiBank'
self.dc['appActivity'] = '.LoginActivity'
```
* For iOS:
```
self.dc['app'] = 'cloud:com.experitest.ExperiBank'
self.dc['bundleId'] = 'com.experitest.ExperiBank'
```
for more ways to upload your application to the cloud, [see here](https://docs.experitest.com/display/TE/Native+Applications+Testing).

## Desired Capabilities

Continuous Cloud Testing expands Appium's capabilities and allows better control over the device and test.
In these examples we use the desired capabilities to set the test name and choose devices to run on, as well as set the application as shown above.
See [Capabilities in Appium Based Tests](https://docs.experitest.com/display/TE/Capabilties+in+Appium+Based+Tests) to learn how to customize the desired capabilities for your tests.

## Documentation
To find out more about Continuous Cloud Testing usage, features, and best practices, visit our online [documentation](https://docs.experitest.com/display/TE/Test+Execution+Home) 

## Support
If you encounter an issue that is not covered here or in our online documentation, contact us at [support@digital.ai](mailto:support@digital.ai).