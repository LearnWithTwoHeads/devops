# Web Servers/Apps

Web servers/apps are the bread and butter of applications and what they are comprised of. Again, just like in the last lesson you have worked with web servers most likely without knowing. If you've ever:

- Did a Google search
- Bought an item from Amazon
- Loaded a twitter feed

You have definitely interacted with web servers. A lot of app development relies on making "requests" to web servers, and getting a "response". That is how the communication goes. So basically to do a Google search, you send the request to Google's web servers with whatever you are trying to search. The response that Google gives you from there web servers is the paginated view of all the results from whatever you searched.

Web servers/apps are almost always written in some programming language (Golang, C++, Java, Python, etc.) and as they run they become processes on the machine. In the last module we spun up `nginx`, which is a general web server meant for a lot of different purposes. `Nginx` was written in the C programming language.

We can actually write our own web servers/apps and run them on any machine for the outside world to interact with them. To take a quick detour, you might find that a lot of DevOps engineers do not actually develop code, but rather operate the code, or write code to automate that operation of the code. So in this module we will be doing a _slight_ bit of application development, but not to be alarmed as you do not necessarily need to be super experienced in a programming language right now.

Lets get started!

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

### Make a request from the outside world

We have made requests to the running web server on the machine itself. The machine can communicate with itself no problem, but what if we want to make that same request and get the same response from outside the machine how would we make that happen?

If you remember, our machine is behind a Public IPv4 DNS, which is basically a way for the public (those outside the machine) to communicate with our machine.

So from outside the machine lets try the following:

```bash
$ curl -v {Public IPv4 DNS}:8080/
```

You should see this command hang indefinitely with the output:

```
*   Trying {IP_ADDRESS}:8080...
```

The {IP_ADDRESS} here will vary for everybody. The reason why this is happening is network related. Basically, your outside machine can properly communicate with the Linux instance, but it can not access the port `8080`. So how can we get it to access that port `8080`?

If you go to the Amazon EC2 instance page, and click on your instance you should see a tab on the bottom center of the page that says `Security`. From there, you should see the dropdown `Inbound Rules`, which basically lists out what traffic is allowed inbound onto the machine. There is currently no entry for anything accessing the port `8080`, so we can add that.

You can add this by clicking on the `launch-wizard` under security groups which will direct you to another page. On this page, if you click on the `Inbound Rules` tab on the bottom center, you can `Edit inbound rules` from there, and add a `Custom TCP` rule with the port `8080`. You can either allow traffic from anywhere or from just your IP address which identifies your outside computer to the Linux machine. It is much safer to allow just your IP address as inbound traffic, however you must remember that if you switch Wi-Fi's/internet connection, your IP address will change.

So now if you `curl` the Public IPv4 DNS for your Linux instance, you should see the output "Hello World!".

We have successfully communicated with our Linux instance from the outside world!

This is great and all, but usually when we type in `www.google.com` we do not specify the port number, why is that? Well the port number is actually implicit here and depends on the protocol `http` or `https`. For `http` the port is `80`, and for `https` the port is `443`. So essentially if you type in `https://www.google.com`, you want to communicate with google's servers on the port `443`. If you type in an address without `http` instead of `https` you are attempting to communicate with the servers on port `80`.

Well you can change the port number in the `main.py` file and run `python3 main.py &` again. You will get some permission denied error running this and that is because the port numbers 1 to 1023 are [restricted](https://www.geeksforgeeks.org/bind-port-number-less-1024-non-root-access/) for `root` user access only. As we've learned in the past you can just run the aforementioned command with `sudo` to bypass that error:

```bash
$ sudo python3 main.py &
```

And now if you run the `curl` command hitting the Public IPv4 DNS without specifying the port, you should see the "Hello World!" message output back to you just as we've seen it work previously.

This however ["bad practice"](https://serverfault.com/questions/413108/is-it-bad-practice-to-run-a-web-application-server-directly-on-port-80-443) because you can run into all sorts of performance and security problems. So what usually happens is to run a high performance off-the-shelf web server on port `80` like `nginx` like we've used before or [tomcat](https://tomcat.apache.org/) server, and proxy the requests from these high performance web servers to your own server running on a different port.

Proxying means sending a request on the behalf on something else. So in this case the request will be sent from `nginx` to the python web server on the behalf of the outside world requesting to our Linux machine.

Let's learn how to do that.

## Reverse Proxying

We learned how to start `nginx` as a process in the last lesson so you should have `nginx` already installed on your machine. So let's run `nginx` again.

```bash
$ sudo nginx
```

(By default `nginx` runs on port `80` which is why we need to execute it with `sudo`.)

Remember how we've talked about how `nginx` is a general web server but can be used as a reverse proxy, we are going to see how to configure it like so.

`nginx` comes with a lot of ways to be configured, and one of the pieces of configuration lies in the file `/etc/nginx/nginx.conf`. We are able to edit this file for our own purposes so we can see the reverse proxy in action. Let's edit this file:

```bash
$ sudo nano /etc/nginx/nginx.conf
```

This has a load of details, most of which aren't very important right now but we will make edits to this file for the reverse proxy action.

Nested under the `http` block you want to put the following configuration:

```nginx
http {
    server {
        listen 80;

        location / {
            proxy_pass http://localhost:8080;
        }
    }
    ...
}
```

Also, you want to disable `nginx` serving the default page that we've seen before. You can put a `#` symbol to comment out this piece of configuration towards the bottom of the `http` block:

```nginx
# include /etc/nginx/sites-enabled/*;
```

What you are basically telling `nginx` to do is "hey intercept all requests that come into this machine on port `80`, and route that request to the server running on port `8080`, and return the response back through the `nginx` web server.

The flow looks like this:

<img src="../static/images/reverse-proxy-action.png" width="90%" height="30%" />

So now if you make the same `curl` request from your outside machine, you should see "Hello World!" print out to your screen. You might need to restart your `nginx` server, so it can pick up this new configuration:

```bash
$ sudo nginx -s reload
```

`nginx` is very cool because it acts as that security and central layer for requests that get into our system. It has configurable behavior for proxying these requests, adding metadata to the requests in the form of `http` headers, and some other security configurations.

The other cool thing about `nginx` is since it can be used as a reverse proxy, it can naturally be used as a [load balancer](https://www.f5.com/glossary/load-balancer#:~:text=A%20load%20balancer%20is%20a,users)%20and%20reliability%20of%20applications.) as well. Load balancers are a type of reverse proxy that distributes network traffic to multiple different servers.

Why is that important?

Well, if you can imagine an app like Twitter, very popular and heavily used by millions of users across the world, there is no way Twitter can support that kind of traffic on one server or our case ubuntu instance. There is a logical limit of how many concurrent requests a single machine can support, and that is based on the network card in the hardware + code runtime limits (Python runtime in our case) + CPU processing speed, and a lot of other factors.

Since all this traffic can not be served from one machine, it is important for Twitter to distribute this traffic across multiple machines to meet traffic demands, and this is where load balancers are particularly useful.

### `nginx` as a Load Balancer

Making `nginx` act as a simple load balancer looks like the following configuration below. Essentially, you specify a `upstream` block which you can name anything (in this case we name it `backend`), then you put the different servers you want to proxy to, we only have one entry in this block. You can specify multiple entries to give that load balancing effect.

```nginx
http {
    upstream backend {
        server 127.0.0.1:8080;
        ...
    }

    server {
        listen 80;

        location / {
            proxy_pass http://backend;
        }
    }
}
```

You can keep on defining these `server` blocks for the different hosts you want to reverse proxy to. By default, `nginx` will [round robin](https://www.nginx.com/resources/glossary/round-robin-load-balancing/#:~:text=What%20Is%20Round%2DRobin%20Load,to%20each%20server%20in%20turn.) the reverse proxying the different hosts. Basically, the first request into `nginx` will go to the first server you configure, second request will go to the second server you configure, so on and so forth.

There are actually a lot of different algorithms that you can use for load balancing requests to different servers. [These](https://www.nginx.com/faq/what-are-the-load-balancing-algorithms-supported/) are the different types of algorithms that you can use.

## What's next?

In this module, we basically ran a python web application that returns a simple "Hello World!" back to the requesting client. This unforunately is not a real world example only something that we've toyed with to learn the basics of reverse proxying and load balancing.

What happens if we add state, and other components to an application. This is more real world, because an app like Twitter will have multiple components just like that. A database to store tweets, user data, an application that will communicate with the database, and a user interface (mobile app, or website).

How does managing all these componenets look and feel like? This is what we will explore in the next module.
