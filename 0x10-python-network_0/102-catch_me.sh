#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me for server to respond with "You got me!".
curl -sL -X PUT -d "u_id=10" -H "Origin: BestSchool" 0.0.0.0:5000/catch_me
