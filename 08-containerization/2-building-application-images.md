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

Environment variables are a great way to do this. Since we are not Software Developers, we are going to just provide the code for you to source an environment variable. You can reference this in the `resources` section.
