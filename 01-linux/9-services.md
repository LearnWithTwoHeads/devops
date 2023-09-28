## Services
 
A lot of the processes that we have executed on the Linux machine up to this point have had very short lifespans.

Commands such as `ls`, `mkdir`, `ps`, etc. Once invoked these commands start a process, spit out the output and then exit.

Sometimes there exists long running processes that you want to run on your Linux machine. For instance, a web server or a daemon (we will learn about these types of services in a later module).

For these long running services, how do we go about managing its lifetime or monitoring the status of it?

This actually is a more complicated task then the question poses, but Linux offers a service on almost all distributions by default called `systemd`.

`systemd` is a program that allows you to manage services on Linux machines. It offers a way to start, enable, stop, and also check the status of the services that you run.

Like I said typically `systemd` is associated with longer running services, but you could use it with anything that can be invoked as a process.

### `systemctl`

The command that allows you to manage and manipulated Linux services is `systemctl`. There are a variety of subcommands you can use with `systemctl` to manage the services i any way you would like, let us look at a few.

Check the status of a service.

```bash
$ systemctl status {service_name}
```

Start a service.

```bash
$ systemctl start {service_name}
```

Stop a service.

```bash
$ systemctl stop {service_name}
```

Enable a service (this allows the service to start on the boot of a Linux machine or on reboot)

```bash
$ systemctl enable {service_name}
```

> Keep in mind that you may have to run some of these commands as the `root` user (prefix with sudo) depending on the requirements
> of your service.

### Example with `sshd`

Lets ask ourselves how were we able to `ssh` onto this machine in the first place? And that in fact is a great question.

There exists a service called `sshd` that understands the `ssh` protocol and allows a user to log in via that if the credentials and everything looks right. `sshd` is actually a Linux service managed by `systemd`!

Let us take a look at it in more detail. Execute the command to check the status of `sshd`.

```bash
$ systemctl status sshd
```

You should see output similar to the following:

```
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
    Drop-In: /usr/lib/systemd/system/ssh.service.d
             └─ec2-instance-connect.conf
     Active: active (running) since Wed 2023-09-27 06:10:39 UTC; 1 day 15h ago
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 43780 (sshd)
      Tasks: 1 (limit: 1141)
     Memory: 5.6M
        CPU: 3.302s
     CGroup: /system.slice/ssh.service
             └─43780 "sshd: /usr/sbin/sshd -D -o AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys %u %f -o AuthorizedKeysCommandUser ec2-instance-connect>
```

You might see some other output below these fields and those are logs from the service you are checking the status of. The important part of this output we would like to look at is where it says `enabled` after `/lib/systemd/system/ssh.service`. `enabled` means that the service will start on boot of the machine.

This is important so that the service can just run without someone manually intervening to do so.

### Custom `systemd` service

A cool thing about `systemd` is that you can create your own services for `systemd` to manage for you. You would have to provide some configuration files for `systemd` to pick up.

The configuration file usually looks something like the following:

```ini
[Unit]
Description=Frontend application to server HTML
After=network.target

[Service]
Type=simple
Restart=always
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/app
ExecStart=/usr/bin/python3 -m http.server

[Install]
WantedBy=multi-user.target
```

Everything after the `=` sign is modifiable, but for this example it is a custom service that will run a Python HTTP server. Typically, this file will be stored at a location as the following, `/etc/systemd/system/{name}.service`. The `{name}` here will be replaced with whatever you want to name the service, and this is what `systemd` will pick up.

Right now this section might be a bit difficult to ingest, but that is because we do not have a practical use case for it yet. In the later modules, it will all come together. It just useful to know the concept of services, and how Linux can manage them for now.