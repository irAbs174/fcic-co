#!/bin/bash
response_file="server_response.json"

curl -s -d "order_code=3043897" -X POST "http://127.0.0.1:8000/report" >> "$response_file"
echo "" >> "$response_file"
grep -i "3043897" "$response_file"
