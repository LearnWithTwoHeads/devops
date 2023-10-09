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

For the frontend we will actually be using a whole different approach than what we have been doing. For the past 3 modules we have been using a static HTML file combined with some JavaScript that communicated with our backend. Basically, everything as far as rendering of the page was happening on the client side.

We are going to do a server side rendering approach here. This will require us to have another Flask based Python application that will serve templated HTML files back to the client as they request it. Obviously, this work would be done by the developers, our task is to containerize this and run the frontend as a container.

I have put the frontend files in the `resources` directory under `app/frontend`. You can copy that whole directory and paste it under your `app` directory within `ansible-exercise` on your dev instance machine. You can then delete the `index.html` that already exists on there and also delete the `js/` directory which contained the JavaScript.

Now let us write `Dockerfile` to containerize this.

**Step 1:** Write a Dockerfile for the frontend

The Dockerfile will look eerily similar to the backend's `Dockerfile`. So create a `Dockerfile` in the `frontend` directory and place the following contents in there.

```Dockerfile
FROM python:3.10.13-alpine3.18

WORKDIR /app

COPY main.py .
COPY template ./template
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
```

### Running the whole thing

Docker comes with a tool that allows you to run multi-container Docker applications at once, `docker compose`. Basically, you can specify multiple containers in a YAML file along with different parameters, and run the containers as one unit.

I have an example of the `docker-compose.yml` file under `resources/app` for reference if you get lost.

**Step 1:** Create `docker-compose.yml`

Within the dev instance under `ansible-exercise/app` create a file called `docker-compose.yml` and place the following contents within it:

```yaml
version: '3'
services:
  frontend:
    build: ./frontend
    ports:
    - "8000:8000"
    environment:
      BACKEND_URL: "http://backend:8080"
  backend:
    build: ./python
    restart: on-failure
    depends_on:
      database:
        condition: service_healthy
    environment:
      MYSQL_HOST: "database"
  database:
    image: mysql:8.0.32
    healthcheck:
      test: ["CMD-SHELL", 'mysql --database=$$MYSQL_DATABASE --password=$$MYSQL_ROOT_PASSWORD --execute="SELECT count(table_name) > 0 FROM information_schema.tables;" --skip-column-names -B']
      interval: 30s
      timeout: 10s
      retries: 4
    environment:
      MYSQL_ALLOW_EMPTY_PASSWORD: true
      MYSQL_PASSWORD: "password"
      MYSQL_USER: "mysql"
      MYSQL_DATABASE: "mysql"
```

There is a top-level key here called services which defines each service you want to run within the docker compose set up. In this configuration there are three services: `frontend`, `backend`, and `database`.

The `build` section under each service defines where the `Dockerfile` will be located for building. For the frontend, the `Dockerfile` is located within the `frontend` directory. For the backend, the `Dockerfile` is located within the `python` directory. For the database it is a bit different, we use the `image` key because we are going to be using a standard `mysql` image from DockerHub. In this case the image name is `mysql:8.0.32`.

The ports section for the `frontend` container tells Docker which ports to forward to the host, basically for the front end we will be able to access it on port `8000` on the host machine. It works just like the `--publish` flag from `docker run` we learned in the basics lesson.

The `environment` section in the YAML defines the environment variables we want the container to have at runtime. This is important for configuring values we want the application to see.

**Step 2** Run `docker compose`

> Before verifying that everything works, make sure you create a security rule to allow traffic on port 8000 of your dev instance
> machine, we will get rid of this rule soon enough.

Within the same directory where the `docker-compose.yml` file is located, under `ansible-exercise/app` run the following command:

```bash
$ sudo docker compose up --build
```

This will build the necessary Docker images and run the containers all for you, exactly what we expect. If you wait about 30 seconds the services should be ready to go (sometimes MySQL) takes a little bit longer to start.

**Step 3** Access your application

Now if you go on the website and type in the IPv4 DNS for your dev instance machine appended with the `:8000` to specify the port you want to access, you should be able to see the same app we know and love and interact with it as we have been doing.

**Step 4**: Clean up

Once you ar done experimenting, and see that the application works as expected, you can clean up by hitting Ctrl+C on the docker compose, and then running the following command:

```bash
$ sudo docker compose down
```

This commands halts the containers and removes all the network links to it.