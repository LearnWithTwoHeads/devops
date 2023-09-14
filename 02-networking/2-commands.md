## Networking commands

### ifconfig

If you want to view all the active network interfaces on your device you can use the command `ifconfig`. This will show the network interfaces an the IP Addresses associated with them.

```bash
$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9001
        inet 192.168.5.138  netmask 255.255.255.0  broadcast 192.168.5.255
        inet6 fe80::851:42ff:fe34:9a5  prefixlen 64  scopeid 0x20<link>
        ether 0a:51:42:34:09:a5  txqueuelen 1000  (Ethernet)
        RX packets 197562  bytes 257269299 (257.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 66339  bytes 8124861 (8.1 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 460  bytes 51496 (51.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 460  bytes 51496 (51.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

In the above command we see that the `eth0` interface has the IP Address `192.168.5.138` associated with it, that is the private IP Address assigned to our EC2 instance.

The lo (loopback) network interface has the IP Address `127.0.0.1` associated with it. This is a special IP Address that will loopback traffic to wherever it originated from. Essentially, whenever you see those numbers `127.0.0.1` the computer is referring to itself.

### Ping

Sometimes it is important to just know if two machines are able to communicate with each other with an IP Address or a DNS name. `ping` is a common command used for this purposes. If the `ping` command is successful it will resolve the DNS name (if it was provided) with an IP address and show bytes being transferred between the two machines.

```bash
$ ping www.google.com
PING www.google.com (142.250.191.132) 56(84) bytes of data.
64 bytes from ord38s29-in-f4.1e100.net (142.250.191.132): icmp_seq=1 ttl=114 time=16.2 ms
64 bytes from ord38s29-in-f4.1e100.net (142.250.191.132): icmp_seq=2 ttl=114 time=16.3 ms
64 bytes from ord38s29-in-f4.1e100.net (142.250.191.132): icmp_seq=3 ttl=114 time=16.3 ms
64 bytes from ord38s29-in-f4.1e100.net (142.250.191.132): icmp_seq=4 ttl=114 time=16.4 ms
```

The `ping` command is successful if you see similar output from the command as above. More technically it will send out ICMP echo requests to the hosts specified, and is successful if that hosts sends back an ICMP echo reply response.

You can read more about what ICMP is and how `ping` works [here](https://blog.cloudflare.com/the-most-exciting-ping-release/) and [here](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/)


### SS (socket statistics)

Lets look at a command to examine network statistics on your machine: [ss](https://www.tecmint.com/ss-command-examples-in-linux/).

```bash
$ ss -a
```

This command will print out to the terminal a load of networking information on your machine. There are two main protocols we are interested in `TCP`, and `UDP`, which we described in the previous section.

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

These are all snapshot in time outputs which sort of mimics how the `ps aux` command worked for processes. There is a way to continuously monitor the network and that is the command `tcpdump`.

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