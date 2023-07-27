# Automation

If you ever find yourself doing something well-defined over and over again, that thing is probably a candidate for some sort of automation.

Usually, the best practice is to get a manual process working for whatever you are doing. In the previous lesson, the manual process was using `rsync` command to sync files from one machine to another machine. The command looked like this:

```bash
$ rsync -rav -e "ssh -i {PRIVATE_KEY}" --exclude "**/venv" app/ ubuntu@{Public IPv4 address}:/home/ubuntu/app
```

This is a pretty lengthy command to remember, and the fact of the matter is that if you wanted to make changes onto any file which we have synced to another machine, you would have to perform this command over and over again (not fun).

You could write a bash script, have that piece of code live on some machine, so you do not have to remember the command. But what about other things like: installing software, performing upgrades, etc. You probably would not want to write bash scripts for each one of these tasks...

Luckily, there exists tool(s) that abstracts away a lot of that burden from you as an engineer, and we will talk about just one of those tools: Ansible.

## Ansible
Ansible is a highly configurable tool that is able to run any set of commands on target hosts. You can think about it like any thing you have done on your machine via `ssh` could be a great candidate to be configured to run with Ansible.

Ansible works by providing it a set of hosts or [inventory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html) somehow, and configuration to log onto those hosts (private key, user information, etc). You can then write configuration for [Ansible playbook(s)](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html). These playbooks will run the configured commands on the hosts, based on whatever you specify.

The commands are abstracted away via [Ansible modules](https://docs.ansible.com/ansible/2.9/user_guide/modules.html). Basically, you can select a module and provide configuration for whatever you want it to do. For example, the [shell](https://docs.ansible.com/ansible/2.9/modules/shell_module.html#shell-module) module allows you to specify a `cmd`. That command can be whatever you can run on a shell (`ls`, `mkdir`, `ss`, etc). There are a lot of modules that allow you to provide your configuration, and allow the command to run with that configuration.

For `rsync`, there is a module to run that command. The module is [this](https://docs.ansible.com/ansible/latest/collections/ansible/posix/synchronize_module.html). Now we will get started to write some Ansible configuration to use `rsync` to copy the necessary files onto the EC2 instance.


**Step 1:**

Install Ansible.

```bash
$ pip install ansible
```

You have to make sure that `python` exists in your environment and that `pip` is installed, as Ansible is a `python` library at its heart.

**Step 2:**

Create an Ansible directory under the `/etc` folder, and create a file called `ansible.cfg` with the following contents in it. So you 

```bash
$ mkdir -p /etc/ansible
```

Now create a file in that directory called `ansible.cfg`, and put the following contents in there.

```
[defaults]
host_key_checking = False
```

This will allow us to bypass the host key checking prompt, which happens every time you ssh from another machine to that Linux EC2 instance.

**Step 3:**

Copy the `hosts.txt` file from this directory onto your machine and replace the Public IPv4 DNS, or Public IP Address with the values for your EC2 instance. Also, specify the path to your private key where it says `ansible_ssh_private_key`.

**Step 4:**

Copy the `playbook.yml` file from this directory onto your machine, preferably in the same place where you have copied the `hosts.txt` file.

**Step 5:**

Run the Ansible playbook.

```bash
$ ansible-playbook -i hosts.txt playbook.yml
```

You should run this command in the same directory that the `hosts.txt` and `playbook.yml` live. If they live in different directories, you can specify the location of those directories instead.

**Step 6:**

Verify that the files where successfully copied onto the EC2 Linux machine. You can `ssh` into the machine yourself and see if the magic did happen. If you see the `app/` folder in the EC2 instance, you did it! 🎉

## Other automation

A big thing Ansible is also used for is server provisioning. Previously for installing software onto a machine, we were `ssh`ing into the machine and installing the software via `apt` package manager. The less and less we can `ssh` into the machine for anything the better. Luckily, Ansible has a built-in module for using the `apt` package manager [here](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html). You can specify which package you want to install via the configuration, and run the playbook.

You can imagine a scenario where you would need to copy files from a host onto a Linux machine, install the necessary packages/runtimes to run the software needed. This can be achieved by configuring an Ansible playbook to do all of the following. The good thing about Ansible playbooks is that they are idempotent, meaning that you can run them over and over again, and the result will stay the same.

**Bonus:** Lets set up our Ansible playbook to do just that in order:
1. Copy the necessary files onto the remote machine
2. Install `python` onto the machine


## What's next?

You can imagine a scenario where multiple people are working on the same project. There can be 10s, 100s of developers wanted to contribute features and bug fixes onto a codebase. How can we allow this to happen seamlessly?

Right now, since you are the only one in charge of the three-tier web application we do not have to worry about other people making edits to the code. However, once your application becomes large and you have a team of developers in charge of the application it can become tough with the codebase living on one machine, and even tougher to manage edits to the codebase.

Thankfully, there is a solution to this, `Git`! We will learn about `git` in the next module.
