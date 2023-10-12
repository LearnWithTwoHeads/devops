## Docker Volumes

In the previous section, we ran all components of our application as Docker containers, and this works really well for both the frontend and backend components, but what about the database?

Well, a database is a layer within an application that is almost certain to maintain some kind of state. By state, we mean information or data that is stored and meant to be used later by one or more processes. In this case, the database stores the overall state of the names that we enter into the application so we can reference it later.

Right now you can run `sudo docker compose up`, and run the application fine, but what happens once you tear down the containers and try and run it again? The state that we have stored previously becomse lost, and the reason being that it is local to the docker container rather than the host computer. This can present a big prolem because docker containers are meant to be ephemeral at times within environments and actually could be torn down or restarted at any time, so how do we compensate for that?

[Docker volumes](https://docs.docker.com/storage/volumes/) solve this problem, and is actually the preferred mechanism for presisting data generated from Docker containers. This can and will be useful for the database layer where we run MySQL.

Lets see that in action.


### Mounting volume for database

To do this we will make some edits to our `docker-compose.yml` file. There is a field called `volumes` that you can specify for each container. You will need some knowledge to understand where the application that is running in the Docker container will store its data to. Once you figure this out, you can specify that location and mount a location on your host to bind to that location on your container.

Based on the Docker documentation for MySQL, it seems as though once it is ran within a container, it will store its data in the location `/var/lib/mysql`.

Knowing this, we can also specify a location on our host where data from the container will be persisted to. We will use the location `/tmp/mysql` for now. Lets get started.

**Step 1:** Modify `docker-compose.yml` to include volume mounting

Modify your `docker-compose.yml` file to include the following content:

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
    volumes:
      - /tmp/mysql:/var/lib/mysql
    environment:
      MYSQL_ALLOW_EMPTY_PASSWORD: true
      MYSQL_PASSWORD: "password"
      MYSQL_USER: "mysql"
      MYSQL_DATABASE: "mysql"
```

The line that is different here is the `volumes` key under the `database` service. We added the `/tmp/mysql:/var/lib/mysql` as one of the values for the volume. Basically, the value to the left of the colon will specify the location on the host you want to mount as a volume, and the value of the right specifies the location within the container that data will be written to.

**Step 2:** Run `docker compose up`, add some data, spin containers down, then run `docker compose up` again

We can now try the same experiment to see if data will be persisted.

If everything works, you should see the same names you have entered the first time show up the second time you run `docker compose up`.

### Wrapping up

Always try to understand the nature of the application you are running. You want to not only understand which different packages or softwares are needed to make your application work as advertised, but also if your application will generate any data of which might need to be persisted outside of the container to be referenced later.

There will be a lot of scenarios where the aforementioned will happen, enabling you to use Docker volumes as necessary.