## Running services

Up until now we have written the Ansible configuration to just provision our server in a way that it will at lease be ready to run. To run the services right now, you would have to `ssh` into the backend machine and invoke:

```bash
$ python3 main.py &
```

and then the frontend machine and invoke:

```bash
$ python3 -m http.server
```

This will allow you to access the frontend machine on port 8000, and have the same enter name experience as we have seen before during the real world application module.

Now that we are using Ansible, we can even automate the process of running the services as well as provisioning configuration on them.

Let us look into how to do that.

### `systemd`

If you remember back in the Linux module we briefly introduced the concept of Linux services, and how to use `systemctl` to manage the services with `systemd`.

Back then in that module they did not have much meaning, but now it will come in handy as we are looking to run services on our machines in an automated way.

Let us copy `ansible-exercise4` over to `ansible-exercise5`, just as we have been doing to give us a clean working space for changes.

**Step 1:** Create two files called `frontend.service` and `backend.service` and put the following content in them respectively.

`frontend.service`
```
[Unit]
Description=Frontend application to server HTML
After=network.target

[Service]
Type=simple
Restart=always
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/app
ExecStart=/usr/bin/python3 -m http.server

[Install]
WantedBy=multi-user.target
```

`backend.service`
```
[Unit]
Description=Python web application to start
After=network.target

[Service]
Type=simple
Restart=always
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/python
ExecStart=/usr/bin/python3 /home/ubuntu/python/main.py

[Install]
WantedBy=multi-user.target
```

These are `systemd` configuration files that tell `systemd` how to run your application. As you can see with the `ExecStart` configuration this tells `systemd` which command to invoke when running your service.

For the frontend the command is `/usr/bin/python3 -m http.server`, looks familiar to just `python3 -m http.server` huh? The only difference between what we have been doing and what we provided to `systemd` is that we provide the full path to the `python3` program.

The same goes for the backend but we invoke `/usr/bin/python3 /home/ubuntu/python/main.py`, basically providing the full paths to both the binary and the Python file we would like to run.

There are much more pieces of configuration other than `ExecStart` as we can see above. This [article](https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files) provides a nice overview of a good amount of the different types of configuration. If you have any questions as always hop into Discord and ask.

**Step 2:** Modify the Ansible playbook to respect the service files and run them on the different machines

In the `frontend` configuration on the playbook provide the following YAML.

```yaml
    - name: Copy frontend service file
      ansible.builtin.copy:
        src: frontend.service
        dest: /etc/systemd/system/frontend.service
    - name: Restart frontend service
      ansible.builtin.systemd:
        name: frontend.service
        state: restarted
```

In the `backend`, provide the following YAML.

```yaml
    - name: Copy backend service file
      ansible.builtin.copy:
        src: backend.service
        dest: /etc/systemd/system/backend.service
    - name: Restart backend service
      ansible.builtin.service:
        name: backend.service
        state: restarted
```

These pieces of configuration will copy the files from the host to the respective target machine, and then use `systemd` to restart the service as necessary. So this allows us to start both of the Python web servers on the `frontend` and the `backend`, and in the end run our application end to end.


At the end of it all, your whole file should be the following:

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
    - name: Copy frontend service file
      ansible.builtin.copy:
        src: frontend.service
        dest: /etc/systemd/system/frontend.service
    - name: Restart frontend service
      ansible.builtin.systemd:
        name: frontend.service
        state: restarted

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
    - name: Copy backend service file
      ansible.builtin.copy:
        src: backend.service
        dest: /etc/systemd/system/backend.service
    - name: Restart backend service
      ansible.builtin.service:
        name: backend.service
        state: restarted

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

**Step 3:** Run the playbooks

You should run the playbook as we have done multiple times before, be sure to run the playbook from the `database` upwards to the `frontend`, so in this order.

`database`
```bash
$ ansible-playbook -i inventory -l database fe-be-db.yml
```

`backend`
```bash
$ ansible-playbook -i inventory -l backend fe-be-db.yml
```

`frontend`
```bash
$ ansible-playbook -i inventory -l frontend fe-be-db.yml
```

After you have run all of these commands, when you access the frontend machine on port `8000`, you should the see the same `Adding Names` app as we have seen before!

We have now leveraged Ansible to run our whole application end to end, and we did not have to `ssh` into the target machines ourselves, what an accomplishment!