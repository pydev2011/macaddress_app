# MacAddress App!
This is a small script to demonstrate the REST API implementation for **https://macaddress.io/**
This script implements the above API and gives you the information about that IP address.

## How to run

Run >> `'python macaddress.py'`
It will ask to enter a valid IP address. If you don't know any, you can use `'44:38:39:ff:ef:57'`
This will print the Company name and Company address related to that IP address.

## Docker Setup

There is a minimum setup for this script in `'Dockerfile'`. Which is the demonstration of how we can setup the Dockerfile for an application. Below is a little description of Docker commands:
-   `FROM`  Tells Docker which image you base your image on (in the example, Python 3.7).
-   `COPY`  Moves the application into the container image.
-   `WORKDIR` Sets the working directory.
-   `RUN`  Tells Docker which additional commands to execute.
-   `EXPOSE` Exposes a port that is used by app.
-   `CMD`  Tells Docker to execute the command when the image loads.

In this example, you don't have to setup the Docker.

## Exception Handling

In the script **macaddress.py**, you will see a small representation of exception handling when you are working on a live script/task/app.
In addition, we can add **Logging** for steps/failures.

## Security

When developing REST API, one must pay attention to security aspects from the beginning. 
There are a lot of methods available for the same. Some of them are Token based authentication/authorization, Session, IP Whitelisting, OAuth2 etc.
Below I explained a few security guidelines when developing and testing REST APIs.

### 1. Authorization
 `Protect HTTP Methods`
 `Whitelist Allowable Methods`
 `Protect Privileged Actions and Sensitive Resource Collections`
 `Protect Against Cross-site Request Forgery`
 `Insecure Direct Object References`

### 2. Input Validation
 `URL Validations`
 `Secure Parsing`
 `Strong Typing`
 `Validate Incoming Content-types`
 `Validate Response Types`

### 3. Output Encoding
 `Security Headers`
 `JSON Encoding`
 `XML Encoding`

### 4. Cryptography
 `Data in Transit`
 `Data in Storage`
 `Message Integrity`
 
### 5. HTTP Status Codes
 