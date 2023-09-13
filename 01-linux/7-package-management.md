## Package Management

Just like with any computer system, it becomes a lot more interesting if you can download and install additional software/packages, and Linux is no different. You have actually 100% done this before but just with Windows or Mac. Things like installing Firefox, Google Chrome, or Serato (for DJs) are all instances where you have downloaded/installed additional software onto your machine. When it comes to DevOps, there are several packages/software that are free for download and can speed up your workflows or tasks. Let us look into how to install packages on Ubuntu.

### APT

Ubuntu comes by default with a powerful command line tool for installing, removing, and updating packages and software, `apt` (Advanced Packaging Tool). Usually to use the `apt` command utility, you have to be the root user, meaning prepend your package installation, removal, updating with the `sudo` keyword. Let us have a first look at installing a package.

```bash
$ sudo apt update
```

The command above is critical before installing any software because the package index may be out of date. Basically, Ubuntu looks at a couple of locations to determine which remote repositories it should look at to locate a particular package. These places include the locations, the file `/etc/apt/sources.list`, and the directory `/etc/apt/sources.list.d`.

Usually, if you try to install a package on Ubuntu and it fails, try to update the package index first, then install again.

Now Let us install a package
```bash
$ sudo apt install tree
```

`tree` is a command line utility that helps a user understand the directory tree of a folder. In most cases, Ubuntu will install the package if its a binary and place that program into your user executables directory `/usr/bin`, but it depends on the type of package.

If you execute the command on the home directory, you should see a similar output (of course this depends on the files you have present on your machine):

```
$ tree
.
├── first-sorted.four.txt
├── lyrics.txt
└── uptime.txt
```

There are the files that exist in my home directory, basically files that were created in the previous lesson.

You can also remove the same software installed onto the machine with `apt`, like so:

```bash
$ sudo apt remove tree
```

This command should not take too long to execute, and it will probably ask you for confirmation. After that has completed successfully, if you try and execute the tree command you should see a failure:

```bash
$ tree
bash: /usr/bin/tree: No such file or directory
```

This means that the command was not able to be found on the machine, basically that it was successfully removed.

## Wrapping up

It is important that as you become more accustomed to Linux, that you understand package management very well. There are also different package managers for different Linux distributions. For instance, Debian based distributions use `apt`, while `rpm` based distributions use `yum` as a package installer.

Overall, there are going to be times where you need to install packages for your machine that might not already exist.