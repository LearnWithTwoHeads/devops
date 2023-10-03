## What's Next?

We have used Ansible to do some pretty cool things. The best part of this is that everything we need for remembering how a machine is provisioned, we can now reference from the Ansible playbooks.

There is a slight problem here though, that is probably not the most obvious. That is when we shut down these machines, and specifically the Ansible control node, we will lose all of the playbook content which we need for the reproducibility and provisioning things on machines. Also, anybody with the private key to the Ansible control machine could technically just log into that machine and start making edits to the playbooks, and that could prove to be costly, since these playbooks are running against machines that are running important services. How can we solve these issues?

[Git](https://git-scm.com/) to the rescue! Without explaning much detail here, Git is the ubiquitous solution for making collaborative edits to files, and having those edits version controlled, and tracked.

Lets get into it in the next module.