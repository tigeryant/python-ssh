import paramiko
import os
import json

# command = "df"

HOST = os.environ["NODE_IP"]
USERNAME = os.environ["SSH_USER"]
PASSWORD = os.environ["SSH_PASSWORD"]

def lambda_handler(event, context): 
    # print('event block hash: ', event['hash'])
    # myhash = event['hash']
    myhash = "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"
    
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, username=USERNAME, password=PASSWORD)
    # _stdin, _stdout,_stderr = client.exec_command(f"bitcoin-cli -named getblock blockhash={myhash} verbosity=0")
    _stdin, _stdout,_stderr = client.exec_command(f"bitcoin-cli -named getblock blockhash={myhash} verbosity=1")
    response = _stdout.read().decode()
    client.close()
    
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-type'] = 'application/json'
    response_object['body'] = json.loads(response)
    # response_object['body'] = json.dumps(response)
    
    return response_object

