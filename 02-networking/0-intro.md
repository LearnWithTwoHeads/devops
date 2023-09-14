## Introduction

You have most likely already, actually 100%, performed some sort of computer networking operation(s) in your life, without even knowing it. The basic idea of computer networking is for one computer to communicate to another usually via the internet, so most of the times computers can not talk to each other without being online.

In your case, the computer network operation you've mostly performed is visiting a website, any website for that matter. If you did not know, when you visit a website, you are most likely communicating if not one at least multiple computers before you see the web page on your end.

Lets say for instance you want to visit `https://www.youtube.com`. What usually happens first is that your request gets routed to your ISP (internet service provider), and your ISP has information on how to translate `https://www.youtube.com` to an IP address. The computers really only understand IP addresses in terms of networking, which we'll talk about later on in this lesson.

This is probably one of the most important lessons when it comes to not just DevOps, but engineering in general. This is because a lot of tech and even non tech companies nowadays run their sofware product across multiple machines. Machines in this setup in most cases would need to talk to each other to get relevant information for whatever they need to do, and that by nature is dependent on the network. Furthermore, whenever you are dependent on the network for your software to work, anything can happen (failure-wise), which means that you have to account for/monitor these error scenarios. That leads to a big topic of **observability** which in very important in the DevOps world as well, and what we will talk about in a later lesson.

For now, we will concern ourself on how to examine the network on a Linux machine, and what it is all about.
