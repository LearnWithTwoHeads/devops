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