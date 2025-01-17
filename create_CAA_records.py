#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, re

zone_ID = '4000000'
API_token = 'supersecrettoken'
API_URI = 'https://dynv6.com/api/v2/zones/' + zone_ID + '/records'
API_header = {'Authorization': 'Bearer ' + API_token, 'content-type': 'application/json'}

my_json_object = """{
"type": "CAA",
"name": "blank",
"data": "letsencrypt.org;validationmethods=dns-01",
"priority": null,
"flags": 128,
"tag": "issue",
"weight": null,
"port": null,
"id": 20000000,
"zoneID": 4000000
}"""

default_route_json = re.sub(r'blank', '@', my_json_object)
my_post =  requests.post(url=API_URI,data=default_route_json,headers=API_header)
my_reply = my_post.content.decode('utf-8')
print(my_reply)

wildcard_json = re.sub(r'blank', '*', my_json_object)
my_post =  requests.post(url=API_URI,data=wildcard_json,headers=API_header)
my_reply = my_post.content.decode('utf-8')
print(my_reply)
