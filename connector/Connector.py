import paramiko


class Connector:
    def __init__(self, ip: str):
        self.ip = ip
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip, username="admin", password="admin", look_for_keys=False, allow_agent=False)


    def close_conn(self):
        self.client.close()
