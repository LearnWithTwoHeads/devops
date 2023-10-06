## Docker Basics

Understanding Docker and its basics is to your advantage as a DevOps Engineer. I would even argue you should understand Docker at an intermediate/advanced level because running containerized application is the way a lot of software runs nowadays. This section will go over the basics to get you productive with using Docker.

### Installing Docker

The Docker website provides instructions on how to get started installing Docker. You can find them [here](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository). Lets `ssh` into our dev instance machine and repeat these steps to get what we need in order to use Docker.

**Step 1:** Run the commands one by one or in bash script to set up Docker's apt repository

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

**Step 2:** Install Docker components

```bash
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

**Step 3:** Verify Docker installation

```bash
$ sudo docker --version
```

If you get some output similar to the following, you should be good to go:

```
Docker version 24.0.6, build ed223bc
```

### Containerizing Python 'hello world'

We are going to revisit the `hello world` Python example from the web servers module, and try to run it within a container rather than straight on the EC2 Virtual Machine.

Lets create a folder on the dev instance machine called `docker` and get started.

**Step 1:** Create a directory called `python` under `docker` and create `main.py` file

Place these contents in the `main.py` file:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # Important for the app to point to localhost here
    app.run(host="0.0.0.0", port=8080)
```

**Step 2:** Write a `Dockerfile` for image build instructions

A `Dockerfile` is a file that allows you to specify how you want an image built. As we discussed in the previous section you can build your own images and host them in different places. `Dockerfile`s have a unique syntax and you can refer to that syntax [here](https://docs.docker.com/engine/reference/builder/). This is a huge document but we will write a basic `Dockerfile` for this `python` app since it does not need much.

Create a file called `Dockerfile` in the `python` directory and place the following contents in it.

```Dockerfile
FROM python:3.10.13-alpine3.18

WORKDIR /app

COPY main.py .

RUN pip install flask

EXPOSE 8080

CMD ["python", "main.py"]
```

Lets break this down line by line...

The `FROM` instruction tells Docker to base this new image off of the `python:3.10.13-alpine3.18` image. I chose this image to base it off of because it matched the Python version on the Ubuntu EC2 machine (it is important to try and use similar versions).

The `WORKDIR` instruction sets the current working directory for subsequent instructions. It will create the directory if it does not already exist.

The `COPY` instruction basically copies files or directories from your host onto this image. So in this example I am copying `main.py` into my Docker image.

The `RUN` instruction tells Docker to run this specific command. The command should exist in the base image. In this case `pip` is already installed in the base image so it works out perfectly.

The `EXPOSE` instruction basically tells Docker that when the container based on the image gets ran it will listen on this port (8080).

The `CMD` instruction defines the default executable of a Docker image. So basically when the container is ran it will be started with the command you specify here. This can be overridden if you are building images from base images.

**Step 3:** Build Docker image

Now that we have the instructions for how to build a Docker image, we are actually going to do so.

The command to do it is the following:

```bash
$ sudo docker build --tag python-hello-world .
```

The `--tag` option basically tells Docker to tag the finished built image with the string that you specify, in this case `python-hello-world`. The `.` after the tag name tells the `docker build` command where the Dockerfile is located.

As you execute this command you should see a lot of output. The output here is showing each layer of the docker build. It should complete successfully, but if it does not you can follow up in the Discord with any questions and concerns.

**Step 4:** Run a `docker` container based on the image

Now that we have successfully built the image, we can run a docker container based on the iamge that will be managed by the Docker daemon.

The command to this is the following:

```bash
$ sudo docker run --name hello-world --detach --publish 8080:8080 python-hello-world:latest
```

This command takes an image name, which in this case is `python-hello-world:latest`. The `docker build` command tags images as latest by default if a tag does not provide a version.

The `--name` flag gives the container a unique name, the `--detach` flag will run the container in the background, and the `--publish` tag will publish the containers ports onto the host, basically to allow you to make TCP/HTTP requests to the port on your host and proxy that request to the actual container.

If the command was successful, you should see some unique string as output. This is a unique string that identifies the running container.

**Step 5:** cURL the endpoint

We can now make an HTTP request to the localhost URL pointed at port `8080`.

```bash
$ curl localhost:8080
```

You should see `Hello World!` as output from the request. This indicates that the container is running successfully. The nice part about it is that containers are isolated from the host from a network perspective. The Docker daemon even assigns each container its own IP Address. The containers do however share resources such as CPU, and memory with the host and that is something to keep in mind.

Now that we have gotten the basics of building a Docker image with a basic Python application, let us explore doing the same for all of our components in the application we have been looking at for the past three modules.