## Python "Hello World"

We will develop a Python web application and run it on the Linux server and see how we can interact with it from the outside world.

**Step 1:**
Create a directory called `python` on your machine, from the `/home/ubuntu` directory.

```bash
$ mkdir python
```

**Step 2:**
Create/Edit a file called `main.py` and put the following text inside there:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # Important for the app to point to locahost here
    app.run(host="0.0.0.0", port=8080)
```

This is `python` code that will basically return the text "Hello World!" if you make a request to the "/" endpoint of this web server.


**Step 3:**

Install the dependencies for this python web app.

```bash
$ pip install flask
```

`pip` is a python package installer, and in this step it is installing a python library called `flask` which is needed for our application to run successfully. If you look at the top line of the python file there is the line

```python
from flask import Flask
```


**Step 4:**
Run the web application in the background.

```bash
$ python3 main.py &
```

This command basically runs the code that we've written in `main.py`. Python is an interpreted language and has a runtime that will try to understand and execute the instructions that you have given to it by way of the `main.py` file.


**Step 5:**
Make a request to the web app and get the response.

```bash
$ curl localhost:8080/
```

As you execute this command this should spit back out to you "Hello World!". We have basically made a request to the webserver that is running on the port `8080`.

`curl` is basically a tool for communicating with web servers, making requests to the web servers and waiting for a response.

The `localhost` text is basically referring to "this local computer". If you actually view the file `/etc/hosts` you can see where the word `localhost` comes from.

```bash
$ cat /etc/hosts
```

There should be a line that has the following content.

```bash
127.0.0.1 localhost
```

`127.0.0.1` for a Linux machine is an IP address that refers to "this local computer", and the `/etc/hosts` file is basically giving an alias name to that IP address. So basically if you would have done:

```bash
$ curl 127.0.0.1:8080/
```

It would have given you the same output. Furthermore, you can actually edit this file as the superuser.

```bash
$ sudo nano /etc/hosts
```

and type in another alias for `127.0.0.1` just below the localhost alias, something like:

```bash
127.0.0.1 localhost
127.0.0.1 abena
```

Now if you make a request like so:

```bash
$ curl abena:8080/
```

You should get the same response as you did `localhost`. You can think of the `/etc/hosts` file as a local DNS server on your machine, mapping host names to IP addresses. Your machine will try and resolve IP address from this file first before it resolves host on a DNS server provided by an ISP.