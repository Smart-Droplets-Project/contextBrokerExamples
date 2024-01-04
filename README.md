# Context Broker Examples

The Orion Context Broker represents the core interoperability component of the Smart Droplets system. As such, it is crucial for seamless communication between all of the Smart Droplets edge and cloud components.

This repository contains examples of how the contextual data from the Smart Droplets domain is managed using the Orion Context Broker. 

## Requirements

In order to run these examples, it is required you have:

* Docker & Docker Compose
* Postman
* Pyhton 3.x

Some additional requirements may be needed which are specific to certain demos. This will be highlighted in their respective sections of the README file contained in the __demos/__ directory.

## Repository Contents

```
.
├── context-broker/ - Contains the Docker Compose file for running the CB
├── demos/          - Contains Postman collections for running interacting with the CB  
└── scripts/        - Additional scripts (e.g. data seeding)
```

## How to Run the Examples

Once all of the required software is installed, take the following steps in order to be able to run the examples:

1. Run the Orion CB using docker and the compose file in the context-broker directory.
2. Seed the Orion CB's database using the relevant Python scripts in the scripts/ directory.
3. Import the prepared collections from the demos/ directory into Postman.
4. Done. You can now run the example requests in Postman.

All relevant subdirectories in the project contain detailed instructions on their purpose and steps to execute them.