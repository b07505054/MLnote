import socket
import time

HOST = '127.0.0.1'
PORT = 8000
server_addr = (HOST, PORT)

send_base = 0
next_seq_num = 0

cwnd_size = 3
num_pkt = 10

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# TODO: write your codes here
client.connect((HOST, PORT))


while (send_base < num_pkt):
    time.sleep(1)
    for i in range(next_seq_num ,min(send_base +cwnd_size,10)):
        if(next_seq_num==send_base):
            client.settimeout(5)
            print("send"+str(i))
            client.sendall(str(i).encode())
        else:
            print("send"+str(i))
            client.sendall(str(i).encode())

	    
    next_seq_num=send_base +cwnd_size
        
    for i in range(send_base ,send_base +cwnd_size):
        try:
            clientMessage, addr = client.recvfrom(1024)
            print('Client message is:',clientMessage.decode("utf-8"))
            if(clientMessage.decode("utf-8")==str(send_base)):
                print("ack"+str(send_base))
                send_base=send_base+1
        
            else:
                print("loss")
                next_seq_num=send_base
                break
        except Exception as e:
                print('timeout')
                next_seq_num=send_base
                break
client.close()