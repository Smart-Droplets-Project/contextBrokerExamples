#!/bin/bash

curl -X GET "http://localhost:8668/v2/types/DeviceMeasurement?limit=10&refDevice=urn:ngsi-ld:Device:30741bc7-4be6-4133-abef-4da74cf4ac35-id&attrs=numvalue" \
    -H "Accept: application/json" \
    -H "Fiware-ServicePath: /"