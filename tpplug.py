import socket
from struct import pack

ip='192.168.8.211'
port='9999'

commands = {'on'       : '{"system":{"set_relay_state":{"state":1}}}',
            'off'      : '{"system":{"set_relay_state":{"state":0}}}',
            'info'     : '{"system":{"get_sysinfo":{}}}'}

def encrypt(string):
    key = 171
    result = pack(">I", len(string))
    for i in string:
        a = key ^ ord(i)
        key = a
        result += bytes([a])
    return result

def decrypt(string):
    key = 171
    result = ""
    for i in string:
        a = key ^ i
        key = i
        result += chr(a)
    return result

def send_cmd(string):
    cmd=commands[string]
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_tcp.settimeout(10)
    sock_tcp.connect((ip, int(port)))
    sock_tcp.send(encrypt(cmd))
    data = sock_tcp.recv(2048)
    sock_tcp.close()
    decrypted = decrypt(data[4:])
    return decrypted
