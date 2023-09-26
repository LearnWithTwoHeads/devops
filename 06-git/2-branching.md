## Branching

Branching is an important feature of Git, for reasons we have learned in a previous section. To keep a long story short, branching is waht enables the power of collaboration on a codebase without developers stepping on each others toes.

Let us get into how branching works, and when to use it.

### Push local copy to remote host

Before we actually branch on the local repository `ansible-exercise1` in the Ansible control machine. We want this code/configuration to be hosted somewhere just in case we lose access to the Ansible control machine or the machine mysteriously goes away. It would be a shame to lose all of our hard work we have coded up throughout the Ansible module.

In an earlier section in this module, you signed up for GitHub using an email and a password. This account will be the one that will create and host the repository that we only have stored locally currently.

Lets get into how to get all this working.

**Step 1:** Login to your GitHub account

Self-explanatory.

**Step 2:** Click `Settings` under the Profile menu

Access your account settings by clicking the `Settings` menu option under the Profile menu in the top right. Should be the menu under the profile picture.

**Step 3:** Access `Developer Settings`

There should be a list of menu options on the left. The last menu option should be `Developer Settings` click on that.

**Step 4:** Create a Personal Access Token

The menu on the right should have a `Personal access token` dropdown menu option click on that, and then click on `Tokens (classic)` underneath.

The page that you are brought to should have a `Generate new token` button that is actually a dropdown as well on the top right. Click on that and then click on the `Generate new token (classic)` menu option.

Give your token a name and then set the expiration to `90 days`.

Under `Select Scopes` just select the `repo` checkbox, this will allow us to use this tokent to push from somewhere to a repo owned by the owner of the Personal Access Token.

Once that is done click on the green `Generate New Token` at the bottom of this page.

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

**Step 5:** Copy the token on the page and do **NOT** lose it

Copy this token, and make sure you have easy access to refernce it once again. Store it on your computer or somewhere you know you will not forget it. The reason for this is that you will not be able to access the value for this token once again.

**Step 6:** Create repository

Click on the Profile icon once again and then click on `Your repositories`. This will bring you to a page where you will be able to see any repositories you have created.

Click on the `New` green button towards the top right. This will bring you to a form page where you will fill out the details of the repository you wish to create.

Under `Repository Name` call it `ansible-exercise`.

Under `Description` give this repo a meaningful description. Something to describe how we are using it to practice Ansible.

Select `Public`, and then click the green `Create repository` button on the bottom right.

The next page you are brought to should actually list instructions on how to push a repository from your local machine to the remote branch. We have actually done a lot of these steps already, all that is needed is pushing the branch.

**Step 7:** Push `ansible-exercise1` on local machine to GitHub

On your Ansible control machine, access your local repository.

```bash
$ cd ansible-exercise1
```

Once you are in the repository directory, let us add the remote URL to this repository so we can push our code up. To do this, issue the following command.


```bash
$ git remote add origin https://github.com/yquansah/ansible-exercise.git
```

> The username will obviously be different here, so instead of `yquansah` yours will be something else.

Once that command successfully completes, you can verify that the origin has been added by issuing the following command.

```bash
$ git remote -v
```

If you see output similar to the following:

```
origin	https://github.com/yquansah/ansible-exercise.git (fetch)
origin	https://github.com/yquansah/ansible-exercise.git (push)
```

You have done it correctly.

Now let us push this code up to our remote host. Issue the following command for that.

```bash
$ git push -u origin master
```

As you hit enter this should prompt you with entering your `username` and `password`. For the `username` use the username associated with your GitHub account. For the password, use the Personal access token we created previously.

If you see output similar to the following:

```
Username for 'https://github.com': yquansah
Password for 'https://yquansah@github.com':
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Compressing objects: 100% (11/11), done.
Writing objects: 100% (14/14), 2.54 KiB | 1.27 MiB/s, done.
Total 14 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/yquansah/ansible-exercise.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

You have done it correctly, and your code should be successfully hosted now on GitHub!

<img src="../static/images/repository-initial.png" width="90%" height="30%" />

If you refresh your repository page on GitHub, you should see the file structure just like the above image. Great first step!

Now let us get into branching!

### Creating branches

Now that we have a remote copy of the initial code, we want to make some edits to it to account for the changes we want to see. For this we will be applying the `ansible-exercise2` changes we have made previously in the Automation module to `ansible-exercise1`, the difference here is that the changes will go in a branch rather than a whole separate folder.

Let us get started!

**Step 1:** Create a branch

To create a branch there are a few ways Git allows command wise for it to happen, we will be using the `git switch` variant. There also happens to be a `git checkout` command that allows for creating local branches.

```bash
$ git switch -c apply-frontend-provisioning
```

The command above tells Git to create a local branch called `apply-frontend-provisioning`. This branch is based off of the `master` branch, so that means it will have everything that was on the `master` branch. We can safely make edits to this branch without affecting `master` branch, and reconcile the changes later.

**Step 2:** Make changes to branch

In this branch, we will create a file called `playbook.yml` and write the following content to it.

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

If you remember this is the exact content we have seen for the frontend playbook before, we are just recreating it, and version controlling it.

Also copy the `app/` directory, which we have been playing with, to this branch.

If you now check untracked changes using `git status` on this current branch you should see the following:

```bash
$ git status
On branch apply-frontend-provisioning
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	app/
	frontend.yml

nothing added to commit but untracked files present (use "git add" to track)
```

We can now stage these changes on this branch using `git add`.

```bash
$ git add .
```

Once the changes are staged, let us commit and push this `apply-frontend-provisioning` branch up to GitHub.

```bash
$ git commit -m "add app directory and playbook"
```

This should create the commit snapshot for changes.

```bash
$ git push -u origin apply-frontend-provisioning
```

You probably will be asked for your credentials again. To prevent from this happening each time you push you can issue the following command before you push next time which enables credentials caching:

```bash
$ git config credential.helper store
```

### Compare changes on GitHub

Once the `apply-frontend-provisioning` branch is pushed up onto GitHub. You can create what is called a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) and then compare those changes to the base branch, `master`, which we based our `apply-frontend-provisioning` branch off of.

**Step 1:** Create a Pull Request

A Pull Request is short terms is a way for you to have a visual representation of the changes that will be made from one branch to another. This is a very important term in Software Development, because it allows others in the organization to comment on your changes, and suggest their thoughts and opinions.

To create a pull request, you can click on the `Pull requests` tab on your repository, and then click on the `New pull request` green button on the mid top right of your screen. This should bring you to a page that looks like this:

<img src="../static/images/create-new-pull-request.png" width="90%" height="30%" />

Change the `compare` branch to `apply-frontend-provisioning` and then click on the `Create pull request` green button on the same page.

<img src="../static/gifs/pull-request.gif" width="90%" height="30%" />

Above is a `gif` showing how a pull request looks. As you can see in this `gif`, you are looking at all the new files and directories that we have added onto the `apply-frontend-provisioning` branch, and since all of this differs from what is on the `master` branch, the Pull Request reflects all of those changes.

**Step 2:** Merge the Pull Request

Since it is only you that is making changes to this repository, you can safely merge this Pull Request in. This will apply the changes from the `apply-frontend-provisioning` branch onto the `master` branch.

Click on the `Merge Pull Request` green button and hit `Confirm Merge` as it will show for the next button.

The new changes on the `master` branch should include all of the changes from `apply-frontend-provisioning` branch. If you refresh your repository page, and see a directory structure like this:

<img src="../static/images/master-branch-changes.png" width="90%" height="30%" />

You have done it correctly!

### Sync local repository with remote

On GitHub we managed to merge the `apply-frontend-provisioning` branch into `master`, so the remote copy of `master` will have all the changes, but our local copy still will have the old `master` code in it. We need to sync up the local branch with the remote one, and since we have already configured the remote for our local we can pull any changes fro the remote branch to keep the local up-to-date.

To do this you can issue a `git pull` command.

```bash
$ git pull
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (1/1), 638 bytes | 638.00 KiB/s, done.
From https://github.com/yquansah/ansible-exercise
   f4a5aed..1b452da  master     -> origin/master
```

You should see an output similar to this. This is the Git client telling you that it has synced `origin/master` which is the remote copy to `master` which is the local copy.

You can confirm that the sync actually did happen by looking at the contents of the directory now.

### Wrap Up

Since we are a single developer working on a repository, we could actually just make changes directly on the `master` branch and pish those changes up to the remote `master` copy, `origin/master, however you definitely want to get in the practice of branching to make changes to repositories. So please, make this a habit!

### Referencing old commits

The current contents of the `master` branch should have the `app` directory and a `frontend.yml`. As we have stated before every commit on the branch is referencable via a commit hash, which is just a snapshot in time of the changes.

We can make use of this by referring to an old commit hash to see what the repository looked like at that snapshot.

Lets see this in action:

**Step 1:** Get the commit hash of the first commit we made

If you remember, we can see the commit log and history with the command `git log`, so lets execute that.

```bash
$ git log
```

You now want to copy to your clipboard the commit hash that is above the commit message "initial commit".

**Step 2:** Checkout repo at the commit hash

Once that is copied run the `git checkout` command with the argument being the commit hash you have just copied.

```bash
$ git checkout {commit_hash}
```

This will put you in a detached HEAD state, and the output of the command will tell you exactly what that means.

If you now browse around the directory, you can see that there is no more `app` directory or `frontend.yml` playbook. That is because we are looking at the repo at the point in time of that commit.

This is the power of Git! Instead of creating different directories to version the code ourselves, we can just use these commit hashes to our advantage to reference the repository at different points in time of its history.