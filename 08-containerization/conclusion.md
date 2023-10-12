## What's Next?

Before the shift to using containerization to package up our applications, we were concerned with running the different components on separate machines. This change allowed for isolation between components of the application and also allowed us to abide by our three-tier architecture principles we talked about during that module.

As we moved to containers, the different components of the application are still logically isolated, but all still run on the same machine. So technically, if that machine shuts down or loses power, we lose our entire application.

We could run the containers on separate machines, but this will still have the problem of resource wastage since VMs could run a lot more workloads than one Docker container. So how do we solve this problem?

[Container orchestration](https://cloud.google.com/discover/what-is-container-orchestration) are incredible pieces of technology that basically solve the problem of packing containers onto different machines efficiently and managing their lifetimes, state, resources, etc.

There are different container orchestration technologies out there, but the one that is most industry standard today is [Kubernetes](https://kubernetes.io/). In the next module, we will introduce what Kubernetes is and how to use it effectively for running applications.