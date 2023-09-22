## First Ansible Playbook

The good thing about Ansible playbooks is that the types of tasks you want to execute on the target machines are all written down in files. You can reference these files, and that property makes these files reusable and also reproducible. Instead of remembering all the commands that you need to execute on a machine to get certain things to work, you can write all of that down within an Ansible playbook in a YAML file, and have that file to reference the certain commands you need.

The ultimate goal here is to reproduce all that we needed to do to get the three tier architecture working as we did in the previous module, but use Ansible playbooks to get it working rather than logging into the machines and manually doing it.

**Note**: Ideally we should try to have a blank slate for all the target machines that Ansible will be accessing. Which means uninstalling all softwares that we did on the target machines, and also removing all files on target machines. These will be things Ansible will do as we write playbooks for it.

### Writing the Ansible Playbook

First let us copy the `ansible-exercise1` directory and create a new directory called `ansible-exercise2`. We will do this to keep track of the steps that we have taken to arrive at a specific goal.

```bash
$ cp -r ansible-exercise1 ansible-exercise2
```

Now lets begin!

**Step 1:** Create a file called `frontend.yml` and write the following contents in it

```yaml
---
- name: Copy app files to frontend
  hosts: frontend
  become: true

  tasks:
    - name: Copy frontend sepcific files to frontend machine
      ansible.posix.synchronize:
        src: ./app
        dest: /home/ubuntu
        rsync_opts:
          - "--exclude=**/python"
          - "--chown=ubuntu:ubuntu"
```

Before executing this playbook, we have to copy the `/app` folder under the `resources` folder under this module into the `ansible-exercise2` directory on the Ansible control machine.

You can see the YAML structure of the above file. Ignore the three `---` on top that is just to separate multiple YAML documents from each other. But the rest of the document tells the structure. There is an array/list of dictionaries, which have the keys `name`, `hosts`, `become`, and `tasks`. `tasks` also is an array/lists of dictionaries which contain the keys, `name`, `ansible.posix.synchronize`, so on and so forth. You can take the time to try and understand the YAML structure all the way down, but at least you should have a basic understanding.

What this playbook will do is synchronize the files from the `app` directory from the Ansible control machine onto the frontend. After you run this playbook, you should see the same files on the frontend machine, just without the `python` directory.

Another thing to note here is that this task is making use of the `ansible.posix.synchronize` module which you can read about [here](https://docs.ansible.com/ansible/latest/collections/ansible/posix/synchronize_module.html). Once you get going on Ansible, there will be a lot of referencing documentation on modules and seeing how the modules are used. There are usually a lot of ways to provide configuration for modules to do exactly what you need them to do. Ansible also does a great job of providing some examples of module usage towards to bottom of every module documentation page.

**Step 2:** Run the playbook

To run any Ansible playbook, you will use the `ansible-playbook` command with some arguments.

```bash
$ ansible-playbook -i inventory frontend.yml
```

You should see output similar to the following after you run.

```
PLAY [Copy app files to frontend] *****************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************
ok: [3.131.141.50]

TASK [Copy app files to frontend machine] *********************************************************************************************************************************************
changed: [3.131.141.50]

PLAY RECAP ****************************************************************************************************************************************************************************
3.131.141.50               : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Ansible will indicate to you that something indeed changed on the target machines within the `frontend` group. There should be some yellow colored text indicating that something did changed as well. If you run this command again right after, you will see output similar to the following.

```
PLAY [Copy app files to frontend] *****************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************
ok: [3.131.141.50]

TASK [Copy app files to frontend machine] *********************************************************************************************************************************************
ok: [3.131.141.50]

PLAY RECAP ****************************************************************************************************************************************************************************
3.131.141.50               : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Nothing should have changed. In fact, Ansible will show in green text that everything is `ok` on the target machine. This is the power and a very important property of Ansible. It operates [idempotently](https://www.merriam-webster.com/dictionary/idempotent). Essentially, if there is nothing to change on the target machine Ansible is supposed to execute a task on, Ansible will not do anything, and report that things are `ok` on the target server.

If something does need to change, Ansible will change it and also report back to the user that it did so.

You have now written and executed your first Ansible playbook, an important step. Let us explore and extend on that in the next section.