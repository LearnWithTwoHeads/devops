## Three Tier Web Architecture

### Intro
- Websites, Applications, and their components
    - There are mutliple kinds of websites, with all different kinds of functionality
    - Some websites just serve static HTML content, and some are more computationally intensive and have backend, database components
- Running an application on a machine
    - Code is written by developers and ran on some type of machine, whether it be a physical host or a VM
    - Usually the presentation, application, and data layer are all separate code bases and are networked with each other to power an application/website

### Body
- Presentation Layer
    - Usually written in some high level language such as Javascript, or markup languages with styling like html/css
    - This layer is what the user sees
- Application Layer
    - The presentation layer calls out to the app layer, and uses responses from the app layer to populate whatever it needs to populate on its layer
    - This layer is written in some programming language that is more general purpose (e.g. node.js, golang, python, rust)
- Data Layer
    - This layer is usually networked with the application layer and responds to that layer with data the app layer requests
    - This layer is usually written in some lower level systems level language such as C, C++, Golang, Rust
    - In most cases developers only have to deal with the app, and presentation layer code-wise, as the data layer is usually never actively developed by developers
- Advantages of three tier web architecture
    - (Image of a glacier to show that a lot goes on beneath the surface)
    - Logical separation of concerns. Allows different types of engineers to fit in where necessary without too many bells and whistles
    - More reliability. An outage on 1 tier, will not affect other tiers negatively
    - Individual components can be scaled independently (depedending on where bottleneck is)
- Disadvantages
    - Network, network, network
    - Previous point is important to understand, because network will always be a concern

### POC/Examples
- Show an example of deploying a full stack app on an EC2 instance, and explain that this can be a problem (why?) if the instance dies all of a sudden
- Show how the application can be split up into multiple tiers, and how to make that happen

### Homework
