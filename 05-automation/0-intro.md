## Automation

Up until now, there has been a lot of movement between our host machine and a provisioned EC2 instance. Whether that instance was a front end host, back end host, or database host. Basically, we manually provisioned a lot of things upon the different EC2 instances which pertained to the function of the processes running on that instance.

For instance, on the database server we did a variety of things manually:
1. Installed MySQL server using `apt`
2. Created a user on the MySQL server and granted it permissions
3. Created a database on the MySQL server which the backend will use

This seems fine enough, and actually can work well if you are a small team who manages a limited amount of servers. It can become a problem with scale though, why is that?

Well, if you look at the list of what we did for MySQL to get it ready to use, this is nothing compared to the amount of steps you would need to provision some other services on a machine. If you want to replicate that same process of provisioning on multiple machines, how is one going to remember all the steps needed to do that? Or how is one going to remember if there needs to be configuration necessary for doing the steps?

These are one of the few reasons why automation is important. You should leave it up to machines to do the heavy lifting for tasks that make sense. The MySQL provisioning is a fantastic example of something that can benefit from automation. We would not want a human doing that short 3 step list over and over, because humans are liable to make mistakes, and we want to minimize that as much as possible.

There exists several tools, and practices to allow for seemless automation to take place. For the next two lessons we are going about some ubiquitous tools that help with that.

Lets dive into the first tool: `Ansible`.