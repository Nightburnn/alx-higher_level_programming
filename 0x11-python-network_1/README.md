## Python Networking 1
This project focuses on using python libraries:
1. urllib 
2. requests

### Python Networking with urllib
The urllib package is a collection of modules that enables you to make HTTP and FTP requests in Python. It provides a simple way to interact with web services and retrieve information from the web.

### Installation
urllib is included in Python's standard library, so no installation is necessary. You can simply import it into your Python script.
```python
import urllib.request
```

#### Making HTTP Requests
To make an HTTP request with urllib, you can use the urllib.request.urlopen() method. This method takes a URL as an argument and returns a file-like object representing the response from the server.
```python
import urllib.request

url = "https://www.example.com/"
response = urllib.request.urlopen(url)

print(response.read())
```
This code will send a GET request to the specified URL and print the response content. Note that the response object is a file-like object, so you can read its contents using methods like read().

You can also add headers to the request by passing an additional headers parameter to urlopen(). For example, to set the User-Agent header to Mozilla/5.0, you can do:
```python
import urllib.request

url = "https://www.example.com/"
headers = {"User-Agent": "Mozilla/5.0"}

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)

print(response.read())
```

This code will send a GET request to the specified URL with the User-Agent header set to Mozilla/5.0.

#### Making FTP Requests
To make an FTP request with urllib, you can use the urllib.request.urlopen() method with an FTP URL. For example, to list the contents of an FTP directory, you can do:
```python
import urllib.request

url = "ftp://ftp.example.com/"
response = urllib.request.urlopen(url)

print(response.read())
```
### conclusion
urllib is a powerful Python package that allows you to easily make HTTP and FTP requests in Python. By following the examples in this guide, you can get started with using urllib to retrieve data from the web in your Python scripts.
