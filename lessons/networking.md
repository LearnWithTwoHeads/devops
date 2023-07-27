## Networking

### Intro
- Overview
    - What does networking entail of?
    - What do we need to know about networking?
    - Networking practically as DevOps
    - **One of the more important topics** something to deal with almost every day on the job due to the nature of distributed computing
- How does the internet actually work?
    - Your computerized device is connected to a router which is connected to your ISP (internet service provider)
    - The ISP has other devices that it is connected to (DNS servers for IP address resolution)
    - A bunch of networks that are interconnected and know how to talk to each other
- IP Addresses
    - Internet speaks in terms of IP addresses, which are 4 numbers delimited by `.`, all numbers are in the range of 1-255 (255.255.255.255)
    - Machines provide a way for other machines to communicate with them, and this is done through networking
    - Usually the previous point is done by opening up a port on your machine
- LAN
    - Local area network
- NAT
    - 1 IP address for your router/modem that is public
    - Private IP addresses for every other device connected to your to router
    - Before NATs every computer had a public IP address

### Body
- Networking on machine
    - Networking on a machine is divided into two major segments: inbound and outbound
- Commands
    -`ping` - used to test basic networking connectivity between two machines via IP address or domain name
        - Used in pretty basic scenarios, maybe the first line of defense when analyzing networking issues (unreachable machines)
    - `ifconfig` - used to grab information about the network interfaces present on your machine
    - `tcpdump` - listening for packet information going in and out of your machine
    - `netstat` - abbreviated command for network statistics
- Hosts file
    - Host file acts like a local DNS lookup before any lookups happen at the ISP level
    - You can edit the hosts file to map any domain name to an IP address and your computer will look at that file firsts
    - Show the permissions of the file at first and how you can only edit the file as root user

### POC/Examples
- Show the commands above and their importance for understanding networking

### Homework
