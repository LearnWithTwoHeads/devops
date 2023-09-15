### Load Balancer (`nginx`)

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

By default, `nginx` will [round robin](https://www.nginx.com/resources/glossary/round-robin-load-balancing/#:~:text=What%20Is%20Round%2DRobin%20Load,to%20each%20server%20in%20turn.) the requests it receives to the hosts specified in the `upstream backend` block. Basically, the first request into `nginx` will go to the first server you configure, second request will go to the second server you configure, so on and so forth. You can do some quick back of the envelope math to figure out what server the nth request will go to.

There are actually a lot of different algorithms that you can use for load balancing requests to different servers. [These](https://www.nginx.com/faq/what-are-the-load-balancing-algorithms-supported/) are the different types of algorithms that you can use.

We will talk a lot more about load balancers in future tutorials, but for now just know that `nginx` can be configured to act as one.