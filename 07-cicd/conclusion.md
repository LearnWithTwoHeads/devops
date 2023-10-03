## What's Next?

This module was a fun one. The end result was an workflow that deployed an application to live servers, exposed out to our users. But before that, we implemented some processes that tested the application for potential errors, and we did that all using the power of CI/CD.

Up until now we have used virtual machines to do all of our development, and running our applications. Although this works fine, there is one thing that is not as intuitive that is a downside here.

Usually, when one is using a virtual machine, they would like to use it for more use cases then just running an basic application. They might want to use it as an actual computer as they would a Mac, or Windows Machine they bought from the store. Essentially, we could be wasting a lot of resources by using a fully-functional virtual machine to run one service potentially. Cost can become an issue at scale, since virtual machines do have a limit for being free on AWS.

The general solution to this problem is [containerization](https://www.netscaler.com/articles/what-is-containerization#:~:text=Containerization%20is%20a%20form%20of,packaged%20and%20portable%20computing%20environment.). It allows you as a DevOps Engineer and operator of an application to provide another layer of isolation from component to component of your application.

There is much more detail to go over here, but we will dive into all of this in the next module.