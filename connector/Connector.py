import time

import paramiko


class Connector:
    def __init__(self, ip: str):
        self.ip = ip
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip, username="admin", password="admin", look_for_keys=False, allow_agent=False)

    def show_router_version(self) -> str:
        channel = self.client.invoke_shell()
        channel.recv(5000)
        channel.send(b"show version\n")
        time.sleep(3)
        ret = channel.recv(5000)
        return str(ret)



    def close_conn(self):
        self.client.close()
