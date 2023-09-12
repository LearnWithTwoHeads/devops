## Outside Requests

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