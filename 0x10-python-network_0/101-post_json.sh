#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -sLXH PUT "Origin: X-School-User-Id" -d "user_id=98" 0.0.0.0:5000/catch_me