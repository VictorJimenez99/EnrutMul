import paramiko
import time


def send_message(channel, msg: str):
    msg = msg + "\n"
    channel.send(msg.encode())
    time.sleep(3)
    ret = channel.recv(5000)
    print(ret)


if __name__ == '__main__':
    ip = input("Ingrese la ip del router")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username="admin", password="admin", look_for_keys=False, allow_agent=False)

    channel = client.invoke_shell()
    send_message(channel, "configure terminal")
    send_message(channel, "ip route 10.0.5.0 255.255.255.0 10.0.2.253")
    send_message(channel, "router rip")
    send_message(channel, "version 2")
    send_message(channel, "network 10.0.3.0")
    send_message(channel, "no auto-summary")
    send_message(channel, "exit")

    send_message(channel, "router ospf 1")
    send_message(channel, "network 10.0.4.0 0.0.0.255 area 0")
    send_message(channel, "redistribute static metric 200 subnets")
    send_message(channel, "redistribute rip metric 200 subnets")
    send_message(channel, "exit")
    send_message(channel, "router rip")
    send_message(channel, "redistribute static")
    send_message(channel, "redistribute ospf 1")
    send_message(channel, "default-metric 1")
    send_message(channel, "exit")
    send_message(channel, "exit")
    send_message(channel, "write")

    channel.close()
    client.close()

