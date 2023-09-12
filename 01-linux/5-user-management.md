## Adding and Deleting users

Up until this point we have seen two users on the system, `ubuntu` and `root`. We know the purpose of `root` being the super user, to do things on the system that are likely prohibited for other users.

The `ubuntu` user is the user we have created the machine with, and is the only non-root/regular user on the system.

What if we had use cases of using different users on the system, how would we go about creating these users. Also, if we no longer have any use for a particular user on a system, how do we go about deleting that user off of the system, and all of the semantics behind that.

### Which users already exist?

First, let us check which users already are on the system. We can view this by the following command:

```bash
$ cat /etc/passwd
```

This command will show output similar to the following:

```bash
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
...
```

There are definitely many more entries than what is listed above, but let us examine this bit of output. There are three types of users on a Linux system overall: super or root user, system users, and normal users.

Super/root user is a user that has the most permissions to do certain actions on a Linux machine. The home directory for this user is `/root`, and it operates with the `/bin/bash` shell. This was already created by the Linux machine as it was provisioned. So a the super user in this output is `root`, as we have learned before.

System users are users who are created by other software and applications. You can usually tell which is a system user by their shell: `/usr/sbin/nologin`. This means that system users are unallowed to login to our machine.

Normal users are users that are created by the root user. It was a transparent process, but when we provisioned/initialized our Linux machine, the root user actually created the `ubuntu` user behind the scenes, and is now the default user we use to login to the Linux machine.

Now let's get to the fun part by adding and deleting users.

### Adding a user

There are a couple commands that allow you to create a user on the system, but we will look at just one, which will work on most Linux systems.

**Adding a user**
```bash
$ sudo useradd abena -m -s /bin/bash
```

Let's break this command and all of its flags down one by one. `abena` is the user we want to add, you can replace this with any name or whatever you want to create.

The `-m` flag is what instructs the command to create a home directory for the user with the users name. So, in this scenario the directory `/home/abena` will be created.

The `-s` flag specifies which shell should be assigned to the user when you login what that user. In this case, we use the very popular shell `/bin/bash`.

You can go ahead and give that a try and see if everything was created right. Here are some commands to verify.

```bash
$ cat /etc/passwd
```

This should show some output, basically showing a line like this:

```bash
abena:x:1001:1001::/home/abena:/bin/bash
```

You should also see that a home directory was created:

```bash
$ ls /home
```

This should output a line that indicates it has found an abena entry from listing out the home directory.

### Switching users

To switch users from the command line, you can use the simple command `su`.

```bash
$ sudo su abena
```

Executed successfully, this should change your terminal prompt to include `abena` instead of `ubuntu` in the very beginning. You can further verify that you are switched to abena by checking "who you are"? Remember the command for that `whoami`.

```bash
$ whoami
```

If you see abena here, you have successfully switched over to the abena user. To go back to `ubuntu` since this brought up a different shell, you can just type in `exit`.

With the user abena, you can do everything that we did with `ubuntu`, and all the same file permission semantics apply.

### Deleting users

To delete a user you can use the following command:

**Delete a user**
```bash
$ sudo userdel -r abena
```

This is a pretty simple command, the `-r` flag tells the `userdel` command to delete the home directory for that user as well.

To verify that the user has been deleted, you can verify in all the places we checked to see existence of the user. `cat /etc/passwd`, and `ls /home`.

### Significance of adding and deleting users

These commands are particularly useful for a Linux system administrator managing a whole bunch of users in an organization on a Linux machine, and their permissions for certain files, programs and such.