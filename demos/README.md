
# Demos

All of the demos in this directory are defined as Postman collections.

All of the demos require you to previously start the Orion Context Broker locally. See directory __context-broker/__ for further instructions.

Some of the demos consist of Postman collections while other are Python scripts. 

# How to Run Python Scripts

Once the Orion Context Broker is up and running (see directory __context-broker/__), you can run Python scripts to interact with it. 

It is recommended to install all of the requirements for these scripts in a virtual envionment. This can be done by creating a new virtual environment. First, go to the directory of the demo you wish (in this case "demo_1"):

> cd demo_1

Now, create a virtual environment: 

> python -m venv venv/

This creates a new directory __venv/__. The virtual environment can be activated by running:

> source venv/bin/activate

Following this, you can install the requirements in the virtual envionrment by running:

> pip install -r requirements.txt

Now, the virtual environment is prepared and you can execute the python scripts in this directory. For example:

> python script.py

Once finished, you can deactivate the virtual environment by running:

> deactivate

To clean up, you can remove the __venv/__ directory. This will destroy the virtual environment.

> rm -rf venv/

# List of Demos

This section gives an overview of all demos and what they intend to show. 

## Demo 1

Showcases the use of the NGSI-LD client library used to interact with the context broker. 

It creates entities through NGSI-LD and stores them in the Context Broker's database. It does this by sending POST requests to the Orion CB containing all of the entities in NGSI-LD format. Communication with the CB is achieved through the Python NGSI-LD client library.

The list of entities created through this script:

* Wheat crop
* Soy crop
* Apple crop
* 3 Parcels for each crop
* 2 Farms
* 2 Pesticide application events

## Demo 2

Demo 2 consists of a Postman collection of requests which highlight how the Orion CB's RESTful API functions. 