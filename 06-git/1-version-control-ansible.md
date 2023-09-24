## Version Control Ansible

Ideally, from the last module you still have your EC2 instances running, specifically the Ansible control node. As we know, with the Ansible control node, there exists 4 folders of which have Ansible related configuration, YAML code, and application code.

Little did we know, we were actually practicing our own little form of version control. We did not have a way to refer back to old modifications of all the Ansible related files, code, so instead of modifying and building upon `ansible-exercise1`, we just created a new directory each time we wanted to enhance the playbook.

If we wanted to run the oldest playbook, we would just `cd` into `ansible-exercise1` and run that playbook. If we wanted the latest playbook, we `cd` into the `ansible-exercise4` and run that playbook.

Thinking of this in a Git sense, you can think of the `anisble-exercise2` as a branch of `ansible-exercise1` (what we deem to be stable), `ansible-exercise3` as a branch of `ansible-exercise2`, and `ansible-exercise4` as a branch of `ansible-exercise3`.

Instead of making whole new directories for each time we want to make edits to the code, we can let Git take care of versioning the edits! In the end, we can have just one directory `ansible-exercise1`, and refer to all the changes to that directory via the commit hash.

Let us actually see how this works practically.

### Initialize Git repository

A Git repository is a fancy name for a directory within a filesystem that has some special directories within it to track changes. For our purposes, just think of it as a directory.

**Step 1:** Install Git

By default, Git should already be installed on your Ubuntu machine, but in case it is not lets install it.

```bash
$ sudo apt install git-all
```

**Step 2:** Initialize `ansible-exercise1` to be Git repository

`cd` into `anisble-exercise1`, and run the following command:

```bash
$ git init
```

This will make `ansible-exercise1` a Git repository. Your terminal prompt might change, depending on how it is set up, and that can confirm that you indeed have a git repository, but to confirm another way, you can:

```bash
$ ls -a
```

If there is a `.git` directory, that means you have successfully created a Git repository.

**Step 3:** See which changes are not tracked

Now that we have a Git repository it will keep track of changes that it does not know about yet. These changes happen to be initially everything that exists within the `ansible-exercise1` directory.

You can always check which files the Git repository does not know about by doing `git status`.

```bash
$ git status
```

You should see an output that looks like the following:

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	ansible.cfg
	inventory
	privkey.pem
```

You see Git is now saying that "Hey, all these files that are in red text are untracked, and I do not know about them yet relative to the Git repo you are operating under." So for us to track these changes we have to "stage" and commit them which will provide that unique hash (snapshot).

> There is one issue here, we do not want to "stage" and commit the `privkey.pem` file. The reason for this is that if you are to push
> your repository to a remote host you do not want your `*.pem` file to be out in the public.

To alleviate this issue, we have to add a `.gitignore` file, and specify which files we do not want Git to track. Edit a file called `.gitignore` and add the following content in it.

```
*.pem
```

This should tell Git not to track `.pem` files.

**Step 4:** Stage untracked files

To stage untracked files and get the ready for a snapshot, we can do that by the `git add`, command. The `git add` command accepts directories, globs, individual files as arguments. All depends on what you want to stage for commit.

In our case, we want to stage everything that is untracked for a commit. We can do that by the following command:

```bash
$ git add .
```

**Step 5:** Commit and snapshot changes

Now that the changes have been staged and are ready for snapshotting, we can do that by the command `git commit`. Before we commit the files, lets change some settings for our global git configuration.

There exists by default a file called `.gitconfig` which lives in the home directory (`/home/ubuntu`). This contains configuration for Git associating user and email information for whomever is making changes to the Git repository. By default, this file has user and email information defaulted to the system. Lets change this file to contain user and email information that is your personal ones.

We can do that by the following command:

```bash
$ git config --global --edit
```

This will open up an editor for you to use, it should be either `nano` or `vi`. If it is `vi`, you can read about how to use `vi` [here](https://www.tutorialspoint.com/unix/unix-vi-editor.htm). If you struggle with it, please reach out on Discord for further help.

You should see output like the following:

```
# This is Git's per-user configuration file.
[user]
# Please adapt and uncomment the following lines:
# name = Ubuntu
# email = ubuntu@ip-192-168-5-211.us-east-2.compute.internal
```

You can uncomment the lines, removing the pound sign next to `name` and `email`. Instead of `Ubuntu`, you can put your first and last name, and instead of `email` you can place the email you have used to sign up on GitHub. Save and exit out of the editor once you are done.

Now let us commit the files.

Execute the following command:

```bash
$ git commit -m "initial commit"
```

You should see output similar to the following:

```
 9 files changed, 178 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 ansible.cfg
 create mode 100644 inventory
```

This tells Git to commit and snapshot whatever was staged, with the commit message "initial commit". Now we have a unqiue identifier which we will see in the next step that can refer to our changes that we have made.

**Step 6:** Verify the commit/snapshot

We executed the `git commit` command in the previous step, but let us verify that the snapshot was indeed created.

You can do that by the command `git log`. This command will show the commit logs, basically details of each commit in the repository.

```bash
$ git log
```

This should show output similar to the following:

```
commit 8a66520ed6a92a108f3315d9d5fe850e1ed12705 (HEAD -> master)
Author: Yoofi Quansah <ybquansah@gmail.com>
Date:   Sat Sep 23 15:57:33 2023 +0000

    initial commit
```

You can see my name and email address as the author of this commit, but most importantly you see the commit hash. That is the alphanumeric string located above the Author information. This is the unique identifier we have continued to refer to previously. Essentially, if you know the commit hash, you can reference the state of the repository at that point in time, even if you continue to make changes in this repository.

Let us see the power of that as we make edits to this directory.