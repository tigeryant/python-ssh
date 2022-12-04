import paramiko
import os

command = "bitcoin-cli getbestblockhash"

HOST = os.environ["NODE_IP"]
USERNAME = os.environ["SSH_USER"]
PASSWORD = os.environ["SSH_PASSWORD"]

def lambda_handler(event, context): 
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, username=USERNAME, password=PASSWORD)
    _stdin, _stdout,_stderr = client.exec_command(command)
    print(_stdout.read().decode())
    client.close()
    return 'executed!'
