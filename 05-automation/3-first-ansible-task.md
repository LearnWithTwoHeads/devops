## Getting Ansible running

In this section, we will experiment with running Ansible to execute some tasks. Here you will learn the setup and the structure of files for a decent Ansible setup.

### Setup Ansible control node/machine

To execute tasks with Ansible on other machines, we have to have a machine that has Ansible installed/configured to execute tasks against other machines. To do this we have to spin up another EC2 instance. This lesson also builds upon the previous lessons, so hopefully you still have your other 3 machines up and running for the front end, back end, and database.

Let us walk through the steps:

**Step 1:** Provision Ansible control machine

Just like you have provisioned other EC2 instances you will provision another one for setting up Ansible.

> You can configure the security groups of all 4 machines to be appropriate. Essentially, the three machines other than the Ansible control node should only be accepting traffic on the `ssh` port from the Ansible machine. This is for ?maximum security.
> We will do a more general overview of AWS later, but if you configure your machines to be in the same subnet, you can use the private IP address
> for one machine communicating with another.

**Step 2:** Install Ansible

Just as we have installed other packages on the machine with `apt`, we will use the same tool to install Ansible.

```bash
$ sudo apt update
```

Update the package index if necessary.

```bash
$ sudo apt install software-properties-common
```

This was referenced in the [Ansible documentation](https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html#installing-ansible-on-ubuntu), but this package provides an abstraction over the `apt` repositories.


```bash
$ sudo apt install ansible
```

Install Ansible.

```bash
$ ansible --help
```

If you get a help menu, you are good to go. If you do not and the command failed, try to Google around to understand the mistake, or uninstall and install again.

**Step 3:** Setup global Ansible configuration

First let us create a directory in the Ansible control machine to organize ourselves.

```$
$ mkdir ansible-exercise1
```

In this directory we will create a file called `ansible.cfg`. What this file will do is set up some global Ansible configuration, we will be using it for one purpose right now and that is to bypass the host key checking when you `ssh` onto a machine. This is because since Ansible is a tool that we want to run as an automated one, we do not want to encounter confirmation messages, or answer to prompts during the running of commands.

Create this file in the `ansible-exerise1` directory and put the following contents in it:

```
[defaults]
host_key_checking = False
```

**Step 4:** Set up inventory file

We want to group our inventory file by the categories of servers we will be remotely accessing.

There are many ways to [set up an inventory file for Ansible](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html), but we will use the `ini` file format for our purposes. In the same `ansible-exercise1` directory, create a file called `inventory` and store the following contents in it.

```ini
[frontend]
{FRONTEND_IP_ADDRESS} ansible_user=ubuntu ansible_ssh_private_key_file=privkey.pem

[backend]
{BACKEND_IP_ADDRESS} ansible_user=ubuntu ansible_ssh_private_key_file=privkey.pem

[database]
{DATABASE_IP_ADDRESS} ansible_user=ubuntu ansible_ssh_private_key_file=privkey.pem
```

You want to replace the all the `*_IP_ADDRESS` with the actual IP Addresses of the respective machines. This is the general setup for the inventory file, and Ansible will be able to access these machines over `ssh` to perform the tasks once we run the tasks.

**Step 5:** Copy private key into Ansible host

Since once of the best practices is to use `ssh` with a private key it is no different for Ansible. All three machines, backend, frontend, database, should be configured to be accessed with the same private key the Ansible machine is accessed with. Knowing this fact, copy the private key and create a file called `privkey.pem` in the same directory `ansible-exercise1`, and paste the copied private key into that file.

The `privkey.pem` will have broad permissions at first so you have to modify the permissions of it as we have done before.

**Step 6:** Run an ad-hoc Ansible task

Now let us actually run an Ansible task! We will be running this task in what Ansible calls [ad-hoc mode](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html). You can think about this as a one liner Ansible playbooks, which we will talk about relatively soon.

We will use the `ping` module to run a task. What this will do is basically see if there is basic connectivity from the Ansible control machine to the other machines specified in the inventory file.

```bash
$ ansible all -i inventory -m ping
```

This command tells Ansible to use all the hosts specified in your inventory file. You can also use the actual group name instead of `all`. The group names in this case will be one of the three: `frontend`, `backend`, or `database`.

You should see output similar to the following:

```
3.131.141.50 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
3.144.70.135 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
3.144.186.45 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

The IP Addresses on the left are the IP Addresses of the frontend, backend, and database machines. Ansible shows that the command resulted in a success. It was able to communicate with the target machines, and sent back a `pong` response.

You now have Ansible set up in a way to do a variety of things. We have used it in this section to "ping" the target machines essentially. In the next section we will start writing and running some Ansible playbooks for the target machines.