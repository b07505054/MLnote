# computer network (python)  
## send-encrypted-message   
client:encrypting and encoding before tranlating data  
server:decoding and verifying the data
![image](https://user-images.githubusercontent.com/68935450/167303495-56184652-0260-4dfd-a985-f4336b043db8.png)

### AES456加密  
```python  
from simplecrypt import encrypt, decrypt 
passkey = 'wow’ 
str1 = 'I am okay’ 
cipher = encrypt(passkey, str1) 
print(cipher)
```    
  
  
What I achive : all spec above  


## Go-Back-N RDT  
sender: sending data with go-back-n  
receiver: if receiving data correctly , sending ack in return , while pack 2,9 being setted loss.
![image](https://user-images.githubusercontent.com/68935450/167307416-121d8fc4-bc9a-4454-a8c6-eaf4ce808d1d.png)

send_base = 0 --> send_base指標位置  
next_seq_num = 0 --> next_seq_num位置  
cwnd_size = 3 --> window的大小為3  
num_pkt = 10 --> 總共要送出10個封包  
  
  
timer sample code
```python 
client.settimeout(5)

  try:
    serverMessage, addr = client.recvfrom(1024)
  except Exception as e:
    print('timeout')
    # the codes to handle the timeout event
```    
  
   
   
What I achive : all spec above

## Dijkstra Algorithm 
![image](https://user-images.githubusercontent.com/68935450/186636190-0f7769b3-9f84-4ef6-8b4d-d104500ace25.png)
![image](https://user-images.githubusercontent.com/68935450/186636643-e180c840-cae1-423b-aa33-451b23bcf797.png) 
input node is topo.py
