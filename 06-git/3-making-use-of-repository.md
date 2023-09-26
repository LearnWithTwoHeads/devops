## Making use of repository

Up until now we have been developing and using Git directly on the Ansible control machine. This is not terrible practice, but ideally we would like the Ansible control machine to be more reactive.

What this means is that it just sources the changes it needs from somewhere and runs the commands it needs to. This allows us to minimize human error away from a machine that will probably be used in production.

Now that we have GitHub, we actually have a remote copy of a codebase the Ansible machine can just reference! Let's see how that can work.

### Create developer instance

We will create a developer Linux instance to house our Git repository, and this is where we will make any edits to the repository as necessary.

So go ahead and create another Ubuntu EC2 instance, and remove all `ansible-exercise*` from the Ansible control machine.

```bash
$ rm -rf ansible-exercise*
```

### Develop on repo on developer instance

As we have stated before, we will use the developer instance as a playground for writing our code and configuration, so `ssh` onto this machine and we will set up the machine to be that developer instance.

**Step 1:** Clone remote repository to local machine

To download the repository so we can reference it locally, you have to make use of the `git clone` command which accepts an argument as the remote Git repository you want to clone/download.

If you go onto the repository page, you can get the repository link of which you will use to download it by clicking the dropdown green button `Code`, and copying the `HTTPS` link.

Now on your local developer machine, type and execute the following command.

```bash
$ git clone {https_link}
```

If the output of the clone command looks like the following:

```
Cloning into 'ansible-exercise'...
remote: Enumerating objects: 17, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 17 (delta 2), reused 14 (delta 0), pack-reused 0
Receiving objects: 100% (17/17), done.
Resolving deltas: 100% (2/2), done.
```

You have successfully downloaded the repository, and you can even do an `ls` to see if the repository exists locally.

**Step 2:** Make edits to this repo to include the final playbook we have seen in previous module

Create a branch from `master` on the repo locally, and name it `final-playbook`.

On this branch rename the `frontend.yml` file to `final-playbook.yml`.

```bash
$ mv frontend.yml final-playbook.yml
```

Edit the `final-playbook.yml` file to include all of the content you see in `ansible/final-playbook.yml` under this modules resources.

**Step 3:** Stage, commit, and push branch to remote

Lets do the dance once again to push this branch to the remote.

Stage the changes.

```bash
$ git add .
```

Commit the changes to create a snapshot.

> Make sure to change the git configuration to be your name and email as we have done before.

```bash
$ git commit -m "modify playbook to be final"
```

Push the changes to remote.

> Remember you have to use your Personal access token which we have created before to push changes onto the remote.
> If you do not have it handy, create another one on GitHub, and use that one.

```bash
$ git push -u origin final-playbook
```

**Step 4:** Create Pull Request on GitHub with `final-playbook` branch and merge

We have done this before in the previous section. Reference that piece of the section again, and merge the `final-playbook` changes into `master`.

### Run Ansible playbook with the Git repo

Now that we have pushed the changes that we want onto GitHub from the developer machine, we want to reference those changes, and run the Ansible playbook referenced.

Exit the developer machine, and ssh onto the Ansible control machine, or use a different terminal to ssh onto the Ansible control machine.

**Step 1:** Clone Repo to Ansible control machine

Use the `git clone` commad with the `HTTPS` argument again to clone the repository onto the Ansible control machine as we have done before.

**Step 2:** Copy private key back onto Ansible control machine and change permissions

Because we previously deleted all the `ansible-exercise*` directories, we do not have a private key anymore to use to connect to the machines listed in the inventory.

Copy the private key back onto the Ansible control machine and give only the owner read permissions to the file.

```bash
$ chmod 400 privkey.pem
```

**Step 2:** Run the Ansible playbook for (frontend, backend, database)

Against the `frontend` group.

```bash
$ ansible-playbook -i inventory -l frontend final-playbook.yml
```

Against the `backend` group.

```bash
$ ansible-playbook -i inventory -l backend final-playbook.yml
```

And finally against the `database` group.

```bash
$ ansible-playbook -i inventory -l database final-playbook.yml
```

All of these runs of the playbooks should give nothing but either `ok` or `changed` statuses for its runs. If you received any failures, please check if configurations are right or that your machines in each group are reachable.

As always, please do not hesitate to reach out on Discord if you are facing further issues.