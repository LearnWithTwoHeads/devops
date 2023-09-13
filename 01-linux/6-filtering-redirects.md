## Filtering, Redirects, and Chaining

In Linux, you will encounter scenarios where you will work with large directory structures or files, or have to deal with the input/output of one command in a certain way.

Linux provides out of the box tools/programs to help with these scenarios easily. We will learn about these utilities during this module.

### `grep`

Let us create the following file `lyrics.txt`, and put the following contents in it:

```
You see my dark shades on
Like I can't see you
But you know say me fancy you
You see my dark shades on
Like I can't see you
But you know say me fancy you
Might say Hello
Don't be surprised when I say hello, gal
Might say Hello
Don't be surprised when I say hello, hello

Shebi I been begging but you no wan gree
You saw me talking to Tolani
So you talk say I no be human being, ahn
Say you you know want me

So I'm here with the girl them that like to party and move somebody
So I'm here with the girl them that like to party and move somebody
Move it to the left to the right
Move it to the left to the right
Move it to the left to the right
Move it to the left to the right
So I'm here with the girl them that like to party and move somebody
So I'm here with the girl them that like to party and move somebody
```

The above file is not the biggest file but still large enough where it is hard to do something specific. Say that you want to filter for text in this file and see occurences of a piece of text. We can use the `grep` command for that, like below:

```bash
$ grep -i somebody lyrics.txt
So I'm here with the girl them that like to party and move *somebody*
So I'm here with the girl them that like to party and move *somebody*
So I'm here with the girl them that like to party and move *somebody*
So I'm here with the girl them that like to party and move *somebody*
```

The above command finds occurences of the word *somebody* (case insensitive with the `-i` flag) in the file `lyrics.txt`. If you want to search for another word in the file you can replace the word *somebody* with another word. There is also another common way to this.

```bash
$ cat lyrics.txt | grep -i somebody
So I'm here with the girl them that like to party and move *somebody*
So I'm here with the girl them that like to party and move *somebody*
So I'm here with the girl them that like to party and move *somebody*
So I'm here with the girl them that like to party and move *somebody*
```

The `|` symbol is important in Linux. It refers to piping the output of one command to another. In more technical terms, you are feeding the standard output of the command on the left to the standard input of the command on the left. `grep` looks to filter for text in standard input if a file is not provided as the second argument (this is common amongst most Linux commands).

### Redirecting

Sometimes there exists times where you want to capture the output of a program or script, and direct it to a certain file. Once the file is created, you can manipulate it in anyway you would like. Let us look at an example:

```bash
$ uptime > uptime.txt
```

`uptime` is a general Linux command that shows information on how long a login session has been. The `>` symbol tells Linux to direct the output of the command on the left to the file specified on the right. If the file does not exists, Linux will create it for you. Sometimes, there will exists cases where you want to append to the file if it already exists rather than creating and putting some text in there. To do this, you can add an extra `>` in between the command and the file. So the command in the end will look like this:

```bash
$ uptime >> uptime.txt
```

This tells Linux not to truncate the file and replace the file, but rather append to it at the end of the file whatever the output is from the command on the right of the `>>`.

### Chaining

Just like we've seen above where we used the `|` symbol to direct the output of one command to the input of another command. There could exists scenarios in Linux where you would like to chain multiple commands together, feeding the output of one command to another over and over again.

Look at the following command:

```bash
$ cat lyrics.txt | sort | head -4 > first-sorted-four-lyrics.txt
```

This command above chains three commands together and redirects the output to a file called `first-sorted-four-lyrics.txt`. It first reads the data in `lyrics.txt` and the output of that is provided as input to the `sort` command which sorts the content in `lyrics.txt`, then the `head -4` takes the first 4 lines of the sorted output of `lyrics.txt` and that is redirected to the `first-sorted-four-lyrics.txt`.

If you compare the 4 lines of the `first-sorted-four-lyrics.txt` file to the first four lines of `lyrics.txt`, you should see a difference.

```bash
$ head -4 lyrics.txt
You see my dark shades on
Like I can't see you
But you know say me fancy you
You see my dark shades on
```

compared to

```bash
$ head -4 first-sorted-four-lyrics.txt
But you know say me fancy you
But you know say me fancy you
Don't be surprised when I say hello, gal
Don't be surprised when I say hello, hello
```

This is because of the sorting we did of the lyrics during the chaining. It is important to practice these concepts on your own, and find ways to make your life easier with doing Linux tasks. You might find very efficient ways to do certain things that you have not thought of before.