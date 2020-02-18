#!/usr/bin/env python3

# See https://www.youtube.com/watch?v=XZ3LUyyz_V0 for walkthrough

import json

with open("incidents.json","r") as myfile:
	json_data=myfile.read()
loaded_json=json.loads(json_data)
print(loaded_json['tickets'][0])

# Most common source IP
common=dict()
for ticket in loaded_json['tickets']:
	common[ticket['src_ip']] = common.get(ticket['src_ip'],0)+1
most_common=max(common, key=lambda k: common[k])
print(most_common)

# How many unique destination IP addresses
uniq_dest=dict()
uniq_src_ip=input("What is the source IP?")
for ticket in loaded_json['tickets']:
	if (ticket['src_ip'] == uniq_src_ip):
		uniq_dest[ticket['dst_ip']] = uniq_dest.get(ticket['dst_ip'],0)+1
print(len(uniq_dest.keys()))

# Avg number of unique destination IP sent file with same hash
sent_hash=dict()
for ticket in loaded_json['tickets']:
	sent_hash[ticket['file_hash']] = sent_hash.get(ticket['file_hash'],0)+1   
num=(float("%0.2f" % (float(sum(sent_hash.values()))/len(sent_hash))))		# Going to get to the nearest two decimal places;
# getting the sum of the sent_hash files, divided by the total
#print(float(sum(sent_hash.values()))/len(sent_hash))		
print (num)
