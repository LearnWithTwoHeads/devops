## Web Servers

Web servers/apps are the bread and butter of applications and what they are comprised of. Again, just like in the last module you have worked with web servers most likely without knowing. If you've ever:

- Did a Google search
- Bought an item from Amazon
- Loaded a twitter feed

You have definitely interacted with web servers. A lot of app development relies on making "requests" to web servers, and getting a "response". That is how the communication goes. So basically to do a Google search, you send the request to Google's web servers with whatever you are trying to search. The response that Google gives you from there web servers is the paginated view of all the results from whatever you searched.

Web servers/apps are almost always written in some programming language (Golang, C++, Java, Python, etc.) and as they run they become processes on the machine, that are bound to a port. In the last module we spun up `nginx`, which is a general web server meant for a lot of different purposes. `Nginx` was written in the C programming language.

We can actually write our own web servers/apps and run them on any machine for the outside world to interact with them. To take a quick detour, you might find that a lot of DevOps engineers do not actually develop code, but rather operate the code, or write code to automate that operation of the code. So in this module we will be doing a _slight_ bit of application development, but not to be alarmed as you do not necessarily need to be super experienced in a programming language right now.

Lets get started!