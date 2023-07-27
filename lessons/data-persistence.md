## Data Persistence

### Intro
- Hard Drives
    - Buying a computer, you have the option to choose your storage capacity usually
    - Storage capacties range from GB to even TB of data
    - When you shut your computer off the data does not disappear but rather it is retained, and you can access the data again once you power the machine back on
    - Multiple types of storage formats: SSDs or HDDs
- Problem
    - If you are dealing with data in the cloud on VMs what happens once the machine is powered down?
    - We have seen storing code files on a VM (EC2 instance), and executing those code files, or binaries
    - If we power down the VM we will actually lose all that data (which makes sense)
    - Although this may not be a problem for code, it could be a problem for other types of storage. A database storing user data critical for your application, etc.
### Body
- Volumes
    - A volume in basic terms represents a logical storage unit that has a single file system
    - They aren't the storage units themselves but rather how the storage unit is represented through a file system
    - On a hard drive you can represent it via a file system, same thing with a USB drive, etc
    - How can you represent storage units on an EC2 instance somewhere else that is persistent?
- Mounting
    - Mounting is a process in which the OS makes files and directories on a storage device avaibable for users via the computer's file system
    - When you plug in a USB device the computer mounts that device for availability as a file system on the computer
    - Once a logical storage device is mounted onto the computer, it becomes a **volume**
- Cloud Storage
    - Amazon, GCP, etc have solved some of these problems by creating ways to mount cloud storage (logical storage unit) to a VM creating a volume for the storage unit
    - Once you store files, data on file system the machine creates via mounting, it will be persisted onto the storage unit
    - This creates persistence of data files even if a machine terminates
    - You can attach another provisioned machine to the storage units and leverage that data persistence. This is useful for stateful applications such as databases, message brokers at times, etc.

### POC/Examples
- Show and automate how to run a MySQL instance on an EC2 instance. show where the data lives at first, and how you can access the data on the EBS volume
- Show how you can create an EC2 instance with an EBS volume mounted, and store some data on the volume at the mount point. Show that data is persisted even once you terminate the instance

### Homework
