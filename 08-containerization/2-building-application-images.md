## Building Application Images

For the app that we know and love, let us build docker images for each component. We will do this from the database layer upwards to the frontend, following the order we have been utilizing.

We will be writing our `Dockerfile`s in the separate directories that contain each of the different components.

### Database

This layer is actually the easiest of them all. We actually do not need to build a `Dockerfile` for MySQL, as one already exists on the Docker Hub remote registry!

We will be using this image `mysql:8.1.0`.

### Backend

We will be writing a `Dockerfile` for the backend in the `python` directory under `ansible-exercise/app`. This will be eerily similar to the `Dockerfile` we wrote for the `Hello World` app in the previous section.

**Step 1:** Modify the Python app to take in a `host` environment variable rather than hardcode

Right now the `host` for a database connection is hardcoded to an IP Address. We want to make this configurable rather than a static value.

Environment variables are a great way to do this. Since we are not Software Developers, we are going to just provide the code for you to source an environment variable. You can reference this in the `resources` directory under `app/python/main.py`.

The main line to look at here is:

```python
host = os.environ.get("MYSQL_HOST")
```

This basically is looking for an environment variable called `MYSQL_HOST` which we will provide once we run the docker image in a container.

**Step 2:** Write a Dockerfile for the backend

Within the `app/python` directory on your dev instance, create a file called Dockerfile as we have done before and put in the following content.

```Dockerfile
FROM python:3.10.13-alpine3.18

WORKDIR /app

COPY *.py .
COPY requirements.txt .
COPY names.sql .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]
```

**Step 3:** Build the Docker image for the backend

As we have done before in the previous section we will build the docker image for the backend. We will title this docker image as `python-backend`.

Execute the following command within the same directory that the backend Dockerfile is located.

```bash
$ sudo docker build -t python-backend .
```

### Frontend

For the frontend we will put the Dockerfile under the `ansible-exercise/app` directory.

We will also modify some things within the `app/js/app.js` file to make the correct request to the specified backend. In the `resources/app/js` directory, copy the `app.js` file and replace it with the `app.js` that you have already.

**Step 1:** Write a Dockerfile for the frontend

