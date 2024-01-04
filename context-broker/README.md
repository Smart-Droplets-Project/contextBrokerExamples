# The Orion Context Broker

The Orion Context Broker is the core interoperability component of the Smart Droplets project.

It consists of 2 main components:

1. The Context Broker -- Conforms with the NGSI-LD API specification. 
2. A document database (MongoDB) used to store and serve context information.

## How to Install

Installation of these 2 component is trivial through the use of Docker Compose. The following command creates the 2 Docker Containers:

> docker-compose up

Once finished, it is recommended to destroy the containers:

> docker-compose down