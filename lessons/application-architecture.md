## Application Architecture

### Intro
- 3 tier web arch
    - Talked about how all layers can be ran on one machine
    - Taught us about logical separation of different layers give some advantage over running on one machine
    - (Allude to the glacier image and ask audience to ponder that for a second)
    - (Show backend architecture in a diagram of a popular application)
- Standardization of ways app layer is developed
    - Monolith - one big program/process that has many parts but avoids network
    - Microservices - several different programs/processes that are usually networked together in some fashion

### Body
- Monolith
    - Advantages:
        - Popular app architecture and is usually the default way of building an application in the beginning
        - Low difficulty of startup and management
        - Bound by one language
        - Easy to test
        - Easy to upgrade dependency wise
    - Disadvantages:
        - Hard to develop fast with
        - Decreased reliability: single point of failure
- Microservices
    - Advantages:
        - Logical separation of services for allocation to different teams. A team in charge of a group of services
        - Can be programming language agnostic
        - Increased reliability: services are independent of each other
    - Disadvantages:
        - Network, network, network
        - High startup, maintenance difficulty
        - Harder to upgrade dependency wise
        - Difficult to test
        - Complicated deployment process
- What does today look like?
    - Usually organizations that use container orchestration technologies like kubernetes, nomad, Amazon ECS etc. leverage the microservices
    - General advice: go with monolith until you are forced to break into microservices due to logical or technical reasons
    - (Give some examples of a logical or technical reason that would force an organization to break into microservices.)

### POC/Examples
- Show how you can run a example of a monolith and microservice architecture locally (which you will create yourself)
- Show example of the Google microservices example with services being written in multiple different languages
- Show how Google has configuration for deployment of those services
