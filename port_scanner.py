import socket

def main():
    print('輸入1 掃描 port 1~65535')
    print('輸入2 掃描常用port')
    while True:
        
        mode = input("請輸入選項\n")
        if mode == "1" or mode == "2":
            break
        else :
            print('輸入錯誤 請在輸入一次')
            continue 
    ip = input('請輸入IP\n')
    
    if mode == '1':
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            s.settimeout(0.5)
            if not s.connect_ex((ip, port)):
                print('IP : %s  port %s is open' % (ip , port))
            s.close()
    else :
        tmp = [20,21,22,23,53,80,161,162,443,1234,3389,8080,8086,8888]
        for port in tmp :
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            s.settimeout(0.5)
            if not s.connect_ex((ip, int(port))):
                print('IP : %s  port %s is open' % (ip , port))
            s.close()

if __name__ == "__main__":
    main()