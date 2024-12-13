#!/bin/bash

curl -L -X POST 'http://localhost:1026/ngsi-ld/v1/subscriptions/' \
-H 'Content-Type: application/ld+json' \
--data-raw '{
  "description": "Notify for all DeviceMeasurements",
  "type": "Subscription",
  "entities": [{"type": "DeviceMeasurement"}],
  "watchedAttributes": ["numValue", "dateObserved"],
  "notification": {
    "attributes": ["numValue", "dateObserved"],
    "format": "normalized",
    "endpoint": {
      "uri": "http://quantumleap:8668/v2/notify",
      "accept": "application/json"
    }
  },
   "@context": "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"
}'
