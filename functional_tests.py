import socket
import time

HOST = "34.77.191.226"
PORT = 5000

retry = 5
delay = 0
timeout = 3


def is_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()


def check_host(ip, port):
    ip_up = False
    for i in range(retry):
        if is_open(ip, port):
            ip_up = True
            break
        else:
            time.sleep(delay)
    return ip_up


assert check_host(HOST, PORT) == False
print("Functional test passed <3")
