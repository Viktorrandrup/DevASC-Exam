import json
import requests
import paramiko
import time

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

# Define the RESTCONF API endpoint and headers
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback14"
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}

# Define the YANG configuration for the loopback interface
yang_config = {
    "ietf-interfaces:interface": {
        "name": "Loopback14",
        "description": "My RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {},
        "ietf-ip:ipv6": {
            "address": [
                {
                    "ip": "2001:db8:acad:14::14",
                    "prefix-length": 64
                }
            ]
        }
    }
}

# Define the basic authentication credentials for the RESTCONF API
basicauth = ("cisco", "cisco123!")

# Update the loopback interface configuration using RESTCONF
resp = requests.put(api_url, data=json.dumps(yang_config), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
# SSH into the virtual router and run the 'show ip int brief' command
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname="192.168.56.101", username="cisco", password="cisco123!")
stdin, stdout, stderr = ssh_client.exec_command("sh ipv6 int br")
time.sleep(1) # wait for the output to be generated
output = stdout.readlines()
print("".join(output))
ssh_client.close()

