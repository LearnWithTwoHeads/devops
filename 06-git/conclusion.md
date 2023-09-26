## What's next?

We have learned a lot in this module about Git. We have learned about how useful it can be as far as providing a nice developer experience around making edits to a codebase, referencing old snapshots of a codebase, and being able to download a codebase from anywhere once it exists on a Git host, GitHub in our case.

In the end, we still actually had to `ssh` onto the Ansible control machine and run the playbook ourselves. As I have stated before, the more we can avoid `ssh'ing` onto machines that control or run our application the better. We can prevent human error and a whole lot of other issues.

Knowing this, how can we automate the process of running Ansible playbooks and other things without having to `ssh` onto the control machine manually?

Also, as you begin to distribute the code, and allow multiple people to be able to contribute to a single repository, how do you decrease the risk of developers introducing bugs and defects into the codebase in an efficient way? In the end, we are all humans and errors will inevitably happen, the goal is to try and limit that as much as possible from happening.

The answer to both of these questions is an important process in Software Development called CI/CD.

CI/CD stands for Continuous Integration and Continous Deployment. It allows for a process of validating code/configuration in a variety of ways, and also distributing that same code/configuation in an automated way.

We will dive into the weeds of CI/CD in the next module!