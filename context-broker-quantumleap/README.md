# FIWARE Context Broker with QuantumLeap Setup

This repository contains a Docker Compose configuration for setting up a FIWARE Context Broker environment with QuantumLeap for time-series data management.

## Components

### Orion Context Broker
- Container Name: `fiware-orion`
- Port: 1026
- Purpose: Main context broker that handles context data management
- Dependencies: MongoDB
- Health Check: Monitors the service availability through the version endpoint

### MongoDB
- Container Name: `db-mongo`
- Ports: 27017, 27018
- Purpose: Database backend for Orion Context Broker
- Features:
  - Persistent storage using Docker volumes
  - Runs with --nojournal flag for development purposes
  - Data persisted in `mongo-db` volume

### CrateDB
- Container Name: `db-crate`
- Ports: 
  - 4200 (HTTP)
  - 4300 (Transport)
- Purpose: Time-series database for QuantumLeap
- Configuration:
  - Authentication disabled
  - CORS enabled
  - 2GB heap size
  - Cluster name: democluster

### QuantumLeap
- Container Name: `fiware-quantumleap`
- Port: 8668
- Purpose: Time-series data connector for FIWARE
- Dependencies: CrateDB
- Environment:
  - Configured to connect to CrateDB

## How to Run

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone this repository and navigate to the _context-broker-quantumleap/_ directory containing the docker-compose.yaml file.

3. Start all services:
```bash
docker compose up -d
```
## Setting up QuantumLeap Subscription

After all containers are running, you need to create a subscription in the Context Broker to forward data to QuantumLeap. This is done using the provided script:

```bash
1. Make the script executable:

> chmod +x subscribe-quantum-leap.sh

2. Run the script:

> ./subscribe-quantum-leap.sh

3. The subscription should now be registered in the Orion Context Broker. You can check this by calling the following script:

> chmod +x check-subscription.sh

> ./check-subscription.sh
```

## Example QuantumLeap Queries

QuantumLeap can be queried by type. To obtain measurements associated to a specific DeviceMeasurement (a specific simulation run for example), you can submit the following request:

```bash
> chmod +x query-by-type.sh

> ./query-by-type.sh
```