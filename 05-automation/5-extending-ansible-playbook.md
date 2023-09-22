## Extending Ansible Playbook

In the previous section we wrote and executed our first Ansible playbook against the frontend machine. We will now look into doing the same for the other two tiers and provision what we need to there.

### Getting the backend machine ready

As we have done before, Before getting started let us copy the directory on the Ansible control machine to another directory called `ansible-exercise3`.

```bash
$ cp -r ansible-exercise2 ansible-exercise3
```

The directory should contain `frontend.yml`, lets change this to `fe-be.yml`.

```bash
$ mv frontend.yml fe-be.yml
```

Let us add the configuration now to configure both the backend and frontend with the necessary things that it needs.

**Step 1:** Modify the playbook

There were a couple things that the backend machine needs to be able to run the Python application smoothly. Besides copying the necessary python files into the target machine, we also need to install `pip`, and then install the requirements from `requirements.txt`.

Let us see how an Ansible playbook will look with this in mind, and extend the current YAML file `fe-be.yml`. Under the existing configuration, place the following content.

```yaml
- name: Set up backend
  hosts: backend
  become: true

  tasks:
    - name: Copy python files from `app` directory
      ansible.posix.synchronize:
        src: ./app/python
        dest: /home/ubuntu
        rsync_opts:
          - "--exclude=**/venv"
          - "--chown=ubuntu:ubuntu"
    - name: Update package index
      ansible.builtin.apt:
        update_cache: yes
    - name: Install pip
      ansible.builtin.apt:
        name: python3-pip
        state: present
    - name: Install requirements with pip
      ansible.builtin.shell:
        chdir: /home/ubuntu/python
        cmd: |
          pip3 install -r requirements.txt
```

The name of each task should be descriptive enough for understanding of what is happening for each task. The first task uses the synchronize module again to sync files from the Ansible control node to the backend machine. The second task uses the `apt` module to update the package index to include more repositories we can install packages from, which we have learned before. The third task uses the `apt` module to install pip on the target machine, this will install `pip3`, which we have been using earlier. The fourth task uses the `shell` module, very versatile. The shell module allows you to run whatever you want that you can execute in the shell of the target machine.

The complete file `fe-be.yml` should look like the following now:

```yaml
---
- name: Copy app files to frontend
  hosts: frontend
  become: true

  tasks:
    - name: Copy app files to frontend machine
      ansible.posix.synchronize:
        src: ./app
        dest: /home/ubuntu
        rsync_opts:
          - "--exclude=**/python"
          - "--chown=ubuntu:ubuntu"

- name: Provision backend machine
  hosts: backend
  become: true

  tasks:
    - name: Copy python files from `app` directory
      ansible.posix.synchronize:
        src: ./app/python
        dest: /home/ubuntu
        rsync_opts:
          - "--exclude=**/venv"
          - "--chown=ubuntu:ubuntu"
    - name: Update package index
      ansible.builtin.apt:
        update_cache: yes
    - name: Install pip
      ansible.builtin.apt:
        name: python3-pip
        state: present
    - name: Install requirements with pip
      ansible.builtin.shell:
        chdir: /home/ubuntu/python
        cmd: |
          pip3 install -r requirements.txt
```

You can run the playbook with the following command:

```bash
$ ansible-playbook -i inventory -l backend fe-be.yml
```

We use the `-l` flag with the `backend` argument here because we just want to target the `backend` group, which according to our inventory file has one host in there. It wouldn't necessary matter if you left this flag out, but we just wanted to examine changes occuring on a particular group.

Now the output of the playbook depends on if you already have some of the things installed on the target machine already, but if you get a mixture of things `changed`, and things `ok`, you should be good to go. You can always `ssh` into the target machine to confirm if everything happened as you intended it to.

### Getting the database ready

Getting the database ready will be one of the more fun group of Ansible tasks we will run. We will try and replicate adding user, provisioning MySQL from scratch.

Lets get started.

Copy the `ansible-exercise3` into a new directory `ansible-exercise4`, and once again rename the file `fe-be.yml` to `fe-be-db.yml`.

Lets modify this file and place the following content underneath. We will explain what everything means shortly afterwards.

**Step 1:** Modify the playbook to include database tasks

```yaml
- name: Set up database
  hosts: database
  become: true

  tasks:
    - name: Update package index
      ansible.builtin.apt:
        update_cache: yes
    - name: Install MySQL
      ansible.builtin.apt:
        name: mysql-server
        state: present
    - name: Install pip
      ansible.builtin.apt:
        name: python3-pip
        state: present
    - name: Install dependencies for mysqlclient
      ansible.builtin.apt:
        name:
          - python3-dev
          - default-libmysqlclient-dev
          - build-essential
        state: present
    - name: Install mysqlclient with pip
      ansible.builtin.shell:
        cmd: |
          pip3 install mysqlclient
    - name: Create database user and grant appropriate priveleges
      community.mysql.mysql_user:
        name: mysql
        password: password
        host: "%"
        priv: "*.*:ALL"
        state: present
```

This is all that we need to set up the database and have it ready for usage by the backend machine. As you can see we make a lot of use of the `apt` module to install different dependencies needed for accessing the database.

The module that is peculiar here is the `community.mysql.mysql_user` module. Notice that this does not fit within the common namespace of `ansible.builtin.*`. This means that this module was built by external developers, or members of the Ansible community. Now this module should come by default by just installing Ansible but in case it does not work, you can install it via:

```bash
$ ansible-galaxy collection install community.mysql
```

The final playbook should look like the following:

```yaml
---
- name: Copy app files to frontend
  hosts: frontend
  become: true

  tasks:
    - name: Copy app files to frontend machine
      ansible.posix.synchronize:
        src: ./app
        dest: /home/ubuntu
        rsync_opts:
          - "--exclude=**/python"
          - "--chown=ubuntu:ubuntu"
- name: Provision backend machine
  hosts: backend
  become: true

  tasks:
    - name: Copy python files from app directory
      ansible.posix.synchronize:
        src: ./app/python
        dest: /home/ubuntu
        rsync_opts:
          - "--exclude=**/venv"
          - "--chown=ubuntu:ubuntu"
    - name: Update package index
      ansible.builtin.apt:
        update_cache: yes
    - name: Install pip
      ansible.builtin.apt:
        name: python3-pip
        state: present
    - name: Install requirements with pip
      ansible.builtin.shell:
        chdir: /home/ubuntu/python
        cmd: |
          pip3 install -r requirements.txt
- name: Set up database
  hosts: database
  become: true

  tasks:
    - name: Update package index
      ansible.builtin.apt:
        update_cache: yes
    - name: Install MySQL
      ansible.builtin.apt:
        name: mysql-server
        state: present
    - name: Install pip
      ansible.builtin.apt:
        name: python3-pip
        state: present
    - name: Install dependencies for mysqlclient
      ansible.builtin.apt:
        name:
          - python3-dev
          - default-libmysqlclient-dev
          - build-essential
        state: present
    - name: Install mysqlclient with pip
      ansible.builtin.shell:
        cmd: |
          pip3 install mysqlclient
    - name: Create database user and grant appropriate priveleges
      community.mysql.mysql_user:
        name: mysql
        password: password
        host: "%"
        priv: "*.*:ALL"
        state: present
```

Let us run the playbook by running the following command:

```bash
$ ansible-playbook -i inventory -l database fe-be-db.yml
```

This should work with no errors, but if it does not please read error messages, and feel free to reach out on any of our community resources for answers to your questions!

We have successfully provisioned each machine to house the necessary files/packages it needs to run its specific function. But how about actually running the frontend and backend service. We will look into that in the next sectino.