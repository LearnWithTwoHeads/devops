## Linux commands
Knowing linux is all about knowing your way around the terminal/command line. The terminal is an application that allows the user to interact with a variety of things on the machine. Things such as directories, files, executable programs. As a DevOps engineer the terminal is where you will probably spend a majority of your day, so it helps to get very comfortable with it.

The practicals in this section are expressed independently, meaning we assume your machine is in a new state every time.

### Directories and Files (Basics)
**Listing contents of a directory**
```bash
$ ls
```

**Creating a directory**
```bash
$ mkdir newdir
```

**See which directory you are currently working from**
```bash
$ pwd
```

**Creating a file**
```bash
$ touch newfile.txt
```

**Change current working directory**
```bash
$ cd {directory_name}
```

The commands above are basic ones that relate to navigating your machines directory structure. Knowing your way around a Linux machine in the terminal is very useful.

(**NOTE**: Most of these commands assume relative path if you do not provide an absolute path, so it will execute in terms of the `pwd`.)

(**NOTE**: The `.` refers to the current working directory while `..` refers to the parent of the current working directory. So if you want to change your working directory to its parent you should use the command `cd ..`.)

### **Practical**
1. Check your current working directory and verify that it is `/home/ubuntu`, the terminal aliases this directory to `~`, so you will most likely see that on your terminal prompt
2. Create a new directory inside `/home/ubuntu`, and call it by your first name. In my case, the directory will be called `yoofi`
3. Change your working directory to the folder you just created
4. Verify that your working directory has changed, you should see the output be `/home/ubuntu/{first name}`
5. Create a file in this working directory called `{last-name}.txt`, using your specific last name
6. List the contents under your working directory

If you see `{last-name}.txt` as output to your terminal, you've done it correctly! 🎉

### Directories and Files (Basics cont.)
**Copy a file from one location to another**
```bash
$ cp {source} {destination}
```

**Move (or rename) file from one location to another**
```bash
$ mv {source} {destination}
```

**Remove a file**
```bash
$ rm {file_name}
```

### **Practical**
1. Create a file in your home directory (`/home/ubuntu`) named `copy.txt`
2. Create a directory named `{first-name}` from your home directory
3. Copy `copy.txt` to `{first-name}` directory
4. Verify that `copy.txt` exists in your home directory and in the `/home/ubuntu/{first-name}` directory
5. Create a file in your home directory named `move.txt`
6. Move `move.txt` to the directory you have created
7. Verify that `move.txt` does not exist in the home directory, but in the directory that you have created
8. Change directory to `{first-name}` and remove `move.txt`

### Editing Files
Now that we have learned how to create files, it would be way cooler if we can actually do something with the file. If you have very seen engineers work, you have most likely seen that they spend a good amount of there day writing code on something. That something is called a text editor. Some text editors are optimized for different use cases, and some are a bit more barebones allowing the user to configure it to their hearts desires.

Natively, on any Linux machine there exists two text editors by default (`nano`, and `vi`). For now we will use `nano` to edit text since we are editing flat text files. Once you start to write some code, and automate some things, `vi` may be a better option, due to its configurability.

Before we open a file in the `nano` editor to manipulate it, let us examine some deeper details about a file. Let us first create a file named `sample.txt` in the home directory. Then execute the command `ls -l`. You should see output like the following:

```bash
$ ls -l
total 0
-rw-rw-r-- 1 ubuntu ubuntu    0 Jul  1 00:00 sample.txt
```

There is a lot to look at here, and we will revist these details soon. The important thing to note of the output right now is the number `0` which is to the right of the word `staff`. That number is the size of this file. Obviously, this file is empty since we have only created it, but lets see what happens to that number once we add some things to the file.

Open `sample.txt` in the `nano` text editor via the command:

```bash
$ nano sample.txt
```

This should bring you to another view on the terminal. In this view, you can start adding text, just as you would any other word document. Type in the phrase "Hello World!", and save the file (`Ctrl-O`). The `nano` editor will ask you where you would like to save the file, if it says `sample.txt` just hit `return`. After the file successfully saved, you can exit the editor via (`Ctrl-X`), and this should bring you back to the regular terminal view.

We have succesfully edited our first (of many) file(s) on Linux! 🎉

Before we examine the long listing (`ls -l`), let us learn one very important command which allows us to view the contents of a file.

```bash
$ cat sample.txt
```

As you execute this command, you should see the output on your screen as `Hello World!`. This allows us to further verify that the contents of what we wanted to write to the file was actually successfully saved.

Let us now revist the `ls -l` command. You should now see this:

```bash
$ ls -l
total 4
-rw-rw-r-- 1 ubuntu ubuntu    13 Jul  1 00:00 sample.txt
```

The number `13` represents how many bytes are in the file it is referring to. In our case there are 12 characters, and one carriage return under `Hello World`, which is the 13th character.

### **Practical**
1. Create a file named anything you want in your home directory
2. Edit the file you have just created and type in the days of the week with a new line in between each day
3. Create a new directory from your home directory named anything you want
4. Move the file you have edited to the directory you created in the previous step
5. Verify that the amount of bytes in the file are what you expect. Should be `57`