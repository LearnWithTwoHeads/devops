## Ansible

[Ansible](https://www.ansible.com/) is at its heart a **very** general purpose automation tool. The word very is emphasized on purpose because people over the years have used Ansible for a variety of use cases. Use cases such as: infrastructure provisioning, infrastructure configuration, application configuration, running applications, service orchestration, etc.

There does exists other tools that might be more suited for some of the above use cases, for instance [Terraform](https://www.terraform.io/) (which we will learn in a later module), which excels at infrastructure configuration, and provisioning in ways where it might be harder for Ansible. However, the general idea is that with Ansible, the sky is the limit for what you can do automation-wise.

### How does Ansible work?

Ansible provides a simple interface for `ssh'ing` and running things on target machines that we previously had to do manually. It is as simple as that. Whenever we use the word "interface" you should think about _details being abstracted away for my own good_. That is exactly what how Ansible should be talked about.

It would be tough for us to constantly remember all the details of how to ssh onto a machine and perform a variety of tasks by remembering all of the Linux commands, flags, and options. Well Ansible has us covered in that regard. Lets talk about some general Ansible concepts.

#### Inventory

An [inventory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html) is basically file that specifies a categorized list of instances you would like Ansible to connect to. Up until now, we have just been `ssh'ing` into our machines via the command line, but instead of doing that, we can provide the configuration parameters for ssh into a file which will become that inventory that Ansible will use.

An inventory could look like this:

```ini
[webservers]
1.1.1.1 ansible_user=ubuntu ansible_ssh_private_key_file=privkey.pem
2.2.2.2 ansible_user=ubuntu ansible_ssh_private_key_file=privkey.pem
```

In this case you have one category or group (webservers), and you specify a list of parameters. The webservers group has two instances it would like Ansible to connect to.

The first instance's IP address is `1.1.1.1` and it would like to log into that machine with the user `ubuntu` using the private key in the file `privkey.pem`.

The regular command for that ssh-wise would be.

```bash
$ ssh -i privkey.pem ubuntu@1.1.1.1
```

However, if we specify this in our inventory file Ansible will also be able to connect to it.

#### Modules

There are a variety of what Ansible calls [modules](https://docs.ansible.com/ansible/2.8/modules/modules_by_category.html) that provide interfaces for different types of automation that fits whatever use case you have. For instance, a basic command to create a file named `foo.txt` is:

```bash
$ touch foo.txt
```

This will work on almost any Linux machine. In Ansible, there exists a module called [file](https://docs.ansible.com/ansible/2.8/modules/file_module.html#file-module) which allows you to create a file, change permissions of a file, etc.

The link that `file` points to might seem like a bunch of gibberish to you now, but it will all come together in the next section.

#### Playbooks

A [playbook](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html) is a collection of tasks you would like Ansible to perform on target machines. A playbook is comprised of configuration that will make use of what you specify in your inventory file, and whatever modules you choose to use.

Essentially, Ansible will run those automations specified on the modules upon the groups in your inventory file. You have to power to configure which things should run on what.

The playbooks which make use of modules are all written in a configuration language called [YAML](https://yaml.org/), which we will talk about in the next section.