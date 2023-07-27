# Real World Applications

As you browse around on applications on a daily basis, what is visual to you is the user interface. For Twitter it is usually the tweets feed. For instagram it is usually the home feed, so on and so forth.

What is not seen is everything else called the "backend" which usually comprises of some applications/services and a storage layer (database), and this actually makes up a huge chunk of a platform.

What I like to equate this to is an iceberg:

<img src="../static/images/iceberg-underwater.png" width="90%" height="30%" />

You can always see the top of an iceberg which in this case is the front end, but what you do not see is the backend (rest of the iceberg underwater), a huge part of the applications identity.

## Getting started running a real application

The backend can be pretty ambiguous and we will talk about different backend architecture methodologies. In this case we will focus on what is called [monolithic architecture](https://en.wikipedia.org/wiki/Monolithic_application). Essentially, there will be one big single process that will run our application on the backend.

Usually, the application on the backend connects to a database that we choose. For this module, we will choose a very simple to use database called [sqlite](https://www.sqlite.org/index.html).

So you can imagine an architecture like the following:


A user interacts with the front end which will communicate with a backend application, and that will communicate with a database if need be, to return information back to the front end to consume and use.

For example, if you refresh your Twitter feed, you send a request to Twitter's application service, and it will fetch new tweets if need be from the database, and return the data all the way back to you as a user to see.

### Example Application

Under the `app/` directory you will see a series of files and folders. Let's look at these individually:

- `index.html`: static html web page (`html` is the markup language of the internet)
- `js/`: contains the JavaScript code to enable interactivity with the `html` content
- `python/`: contains the backend application code that the `html` interacts with through the `js/` interactivity files

With all of these files, it makes up a fully-featured web application with all of the three tiers we have mentioned above (frontend, backend application, and storage).

So the app works like this:

// insert GIF of adding names and the names displaying

It is simple. You basically add a name and the name displays on the left side of the browser. What is happening underneath the hood is that you input some text into the `html` text box. When you press the `Add` button, the JavaScript code will take that text and send a request to the python backend which handles the request and stores that text into the database (SQLite). You can see the power of the database (persistence) if you close and open the web page. The data we've added is still there, because when the page loads the front end makes a request through the JavaScript code to the python backend to retrieve all of the names from the database and display it on the web page.

### How to run this application?

We will need to copy these files into our EC2 Linux instance. The command to do that looks like the following:

(You should run this in the directory wherever you store the `app/` directory in)
```bash
$ rsync -rav -e "ssh -i {PRIVATE_KEY}" --exclude "**/venv" app/ ubuntu@{Public IPv4 address}:/home/ubuntu/app
```

The `rsync` command is a pretty powerful one and you can read more about it [here](https://www.hostinger.com/tutorials/how-to-use-rsync#:~:text=The%20Linux%20rsync%20command%20transfers,command%20to%20improve%20their%20productivity.). Basically, it will copy the whole `app/` directory into the Linux instance. It does this over `ssh`.

You can then `ssh` into you Linux instance, and edit the `app/js/app.js` file. Wherever it says `${IP_ADDRESS}` you want to remove that and put the IP Address or Public IPv4 DNS name of your Linux instance (this will be different for everybody). Now your application is fully configured and ready to be ran.

Before you run do run anything though, let us revisit the in/outbound rules for your instance. You want to make sure you open up ports `8000`, and `8080` for inbound traffic to the internet. This is because the web server that will serve your HTML content will run on port `8000`, and the python backend server will run on port `8080`. You can revisit the networking module on how to open up in/outbound traffic to a port on your machine.

#### Running the `python` backend server

We have already seen how to do this in the previous module but lets revisit.

**Step 1:**

Change directory into `/app/python`, and install the packages with the `pip` python package installer.

```bash
$ pip install -r requirements.txt
```

**Step 2:**

Run the `python` backend by doing:

```bash
$ python3 main.py &
```

After these steps the `python` backend should be up and running on port `8080`.

#### Running the HTML web server

**Step 1:**

Change directory to `app/`, and run the `http` server for serving the html web content.

```bash
$ python3 -m http.server
```

This will run your front end on an http web server a common practice for serving front end applications.

#### Accessing the page from outside the machine

If you now go on a browser on your Mac or Windows machine and type in the Public IPv4 address of your instance appended with `:8000` to specify which port you want to hit on the Linux instance, you should see the web page to add your name.

You can then use it just as you see the GIF above, voila!

**Bonus:** try putting your html web server behind `nginx` so you do not have to specify the `:8000` port value after the Public IPv4 DNS name.)

## Three Tier Web Architecture

Right now all the components of our three tier web application are running on one machine, which is the Linux instance that we have spun up. This is actually BAD practice, you can read about some reasoning [here](https://www.baeldung.com/cs/deploy-database-web-server). Some quick reasons for this include:

- Decreased flexible scalability: since every tier is running on one machine you can not scale those tiers independently
- Decreased security: usually someone having access to your database/storage is bad, they can run queries against it and even worse delete data
- Decreased reliability: your whole application is a single point of failure. If the machine that is running your three tier application is turned off, the whole application goes with it

How we alleviate these issues is to run the separate tiers of the three tier web application on different machines or groups of machines. We can then have different policies/configuration for these machines that address the weaknesses of each tier. For instance, for the storage/database tier we can make sure that only a few IP addresses or DNS can access the instance that is running it, or we can give more resources: CPU, memory to the backend application tier since it will be the tier that will be dealing with the most computation. Separating out these tiers gives us that advantage to specify the needs of whatever we are dealing with.

**Bonus:** Separate out the applications on different instances. To do this you need to initialize two different EC2 instances, and run the html web server on once instance, the python backend/storage on another instance. This is not true three tier since the database SQLite, but you can still see the benefit. You will then need to speicify the in/outbound rules specific for the instances:

- The instance running the front end can **only** talk to the instance running the backend/storage
- Everybody can talk to the front end instance (open it up to the internet)

## What's next?

For the past two lessons we have been ssh'ing into our instance and editing files directly (`python` files). What happens when we want to add new features to our application, do we have to ssh onto the instance every time we want to make changes? Editing files directly on machines is a recipe for disaster, we are humans and are liable for making some mistakes. Generally, you woul dwant another copmuter to automate this process of moving files back and forth between your machine, or installing software on your machine, etc.

In the next module, we will learn about how to automate a process like this so we do not have to ssh directly onto our machine. Specifically, we will be learning about [Ansible](https://www.ansible.com/).
