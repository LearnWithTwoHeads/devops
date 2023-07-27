## Load Balancers

### Intro
- Load Balancers
    - A piece of software that sits on top of and has knowledge about different servers in order to route requests to those servers
    - Reverse Proxy vs. Load Balancer: a load balancer is an type of a reverse proxy, and reverse proxy is a generalized form of a load balancer
    - Examples include: nginx (using as a load balancer), HA proxy, etc.
- Problem
    - Your backend receives a lot of traffic and you need to horizontally scale some services there
    - How do you distribute the traffic to all the scaled services fairly?
    - Load balancers help to distribute the traffic
- How do they work?
    - Load balancers have knowledge of the servers they are routing traffic to
    - They use some sort of load balancing algorithm to distribute the traffic as evenly as possible [algorithms](https://kemptechnologies.com/load-balancer/load-balancing-algorithms-techniques)
### Body
- Advantages
    - Centralized control over web traffic: you can add/remove headers and other common logic in one place for all requests if that fits your needs
    - Reliability: Load balancers can avoid routing traffic to servers that are down, and route traffic to active servers
- Concrete examples of Load Balancers
    - Nginx: a general type of web server that can serve static content, but also act as a reverse proxy to send requests to servers on behalf of a client
    - We can make Nginx function like a web server
    - To start nginx on ubuntu EC2 instance, you can first install nginx as a software package, and then issue a `sudo systemctl nginx start` command
    - You should see a basic HTML page talking about nginx if you hit the IP or actual host
- Proxy traffic to services
    - You can provide some config to the `nginx.conf` file that will instruct nginx to proxy traffic to another service listening on a port on the same machine
    - A piece of the config can be replicated to achieve the load balancing effect
    - You can restart nginx to pick up the modified config each time you make edits to the file

### POC/Examples
- Version control some code that can automate this process of copying code files/binaries to multiple EC2 instances and start the web service. Also easily editing nginx configuration for easy load balancing

### Homework
- Spin up two/three EC2 instances and run a web server on one while running nginx on another one. Modify the nginx config to be able to route traffic to the web servers accordingly
