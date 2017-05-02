import socket, threading

sem = threading.Semaphore()
count = 0
th = []
conns = []
def to_client(conn, addr, count):
    cnt = count
    global conns
    x=0
    while count:
        x+=1
        count = (int)(count/10)
    conn.sendall((str(x)+"!server create user%d"%cnt).encode('utf8'))
    for i in range(len(conns)):
        conns[i].sendall(("%s에서 유저 %d님이 접속했습니다."%(addr[0],cnt)).encode('utf8'))
    print("%s에서 유저 %d님이 접속했습니다."%(addr[0],cnt))

    try:
        while 1:
            read = conn.recv(1024).decode('utf8')
            if read == 'exit()' or not read:
                conn.sendall("종료합니다.".encode('utf8'))
                for i in range(len(conns)):
                    conns[i].sendall("%s에서 유저 %d님이 exit 명령을 통해 종료했습니다."%(addr[0],cnt))
                print("%s에서 유저 %d님이 exit 명령을 통해 종료했습니다."%(addr[0],cnt))
                exit(0)
            read = "user%d : %s"%(cnt,read)
            print(read)
            for i in range(len(conns)):
                conns[i].sendall(read.encode('utf8'))
    except:
        conns.remove(conn)
        print("%d // 유저 %d님이 나갔습니다."%(l0en(conns),cnt))
        for i in range(len(conns)):
            print(conns[i])
            conns[i].sendall(("유저 %d님이 나갔습니다."%cnt).encode('utf8'))
        exit(0)

HOST='0.0.0.0';
PORT=int(input("열 포트 번호를 입력해주세요 : "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
print("서버를 성공적으로 열었습니다.")

while 1:
    conn,addr = s.accept()
    conns.append(conn)
    sem.acquire()
    count +=1
    sem.release()
    client = threading.Thread(target=to_client, args=(conn,addr,count))
    client.start()
    th.append(client)
for t in th:
    t.join()
