#!/bin/bash

curl -X GET \
  'http://localhost:1026/ngsi-ld/v1/subscriptions/' 
  #-H 'Link: <http://context/user-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
