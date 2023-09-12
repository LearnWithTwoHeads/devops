## Networking commands

### ifconfig

### SS (socket statistics)

Lets look at a command to examine network statistics on your machine: [ss](https://www.tecmint.com/ss-command-examples-in-linux/).

```bash
$ ss -a
```

This command will print out to the terminal a load of networking information on your machine. There are two main protocols we are interested in `tcp`, and `udp`. The `tcp` protocol is probably the most important protocol for our purposes because it is what one of the most popular protocols `http`, relies on. `udp` on the other has a lot of popular use cases. There is a wealth of sources that exhaustively explain the big differences between the two, but here is a short list.

**tcp**
- Requires an established connection before transmitting data (dialing to another computer)
- Can retransmit data
- Delivery to destination is guaranteed
- Slower than udp, but tradeoff is complete data deliver

**udp**
- No connection is needed
- No data retransmitting
- Delivery is not guaranteed
- Faster that tcp, but at risk of data loss between machines

To filter for `tcp` you can type in the command:

```bash
$ ss -t
```

The output here on a fresh machine (EC2 instance) that isn't running anything should just be one line. This line is actually **very** important. It shows the details of the `ssh` connection that was made from your host machine to the EC2 instance. Lets go column by column:

`State`: This shows the state of the connection. A connection has a lifetime and goes through multiple states during that lifetime
`Recv-Q`: Number of network packets recieved over this connection
`Send-Q`: Number of network packets sent over this connection
`Local Address:Port`: The address and port of the local machine this connection is initiated
`Peer Address:Port`: The remote address and port by which this connection is initiated

If there active processes on your machine you can actually get statistics on which process doing networking as well, using the command with flag:

```bash
$ ss -p
```

You can also combine these commands and declaritively get information for any filter you want.

**Show PIDs for all tcp connections on my machine**
```bash
$ ss -tp
```

**Show all TCP traffic and resolve host names from IP, along with PIDs**
```bash
$ ss -r
```

These are all snapshot in time outputs which sort of mimics how the `ps aux` command worked for processes. There is a way to continuously monitor the network and that is the command `tcpdump`. However, before we look at `tcpdump`, we will look at another command `ping` which is one of the most fundamental networking commands on Linux.

### Ping

Sometimes it is important to just know if two machines are able to communicate with each other. `ping` is a common command used for this purposes. If the `ping` command is successful it will resolve the DNS name with an IP address and show bytes being transferred between the two machines.

```bash
$ ping www.google.com
```

### Tcpdump

`tcpdump` is one of the more advanced commands when it comes to networking but very powerful. It allows you to continuously see the raw bytes that are entering or leaving a network interface. You can even filter to see the bytes entering a specific port. Let us try and run it (it needs to be ran as the `root` user).

```bash
$ sudo tcpdump
```

Well the output of that was way too much to even try and soak in anything useful. By default `tcpdump` will output all things from all the network interfaces on your machine.

As with most things, we are most likely specific in what we are looking for and concerned with a specific use case. So lets filter the `tcpdump` command down some.

```bash
$ sudo tcpdump -c 5 port 22
```

What this command is doing is telling your machine to just capture 5 network packets that are going through the port 22 (inbound and outbound) traffic. The port `22` is standardized as the `ssh` port, so basically the port we used for `ssh` onto a machine. There seems to be continuous packets sent, this is most likely `ssh` acknowledging that the connectivity should still exist.

In modern day technologies, `tcpdump` is usually considered a last ditch effort to understand at the byte level what is going on with the network on a specific machine. There are higher level tools that are used in modern day to examine network activity, but to know how to use `tcpdump` is always to your advantage.

Currently, we do not have anything running on our machine that can receive or send web traffic. In most cases, there are applications that listen over a port (port 22 for ssh connections), and developers create these applications to listen on these ports. Lets look at how to run a application listening on a port to receive web traffic.