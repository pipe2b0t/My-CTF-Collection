from cryptography.fernet import Fernet
fk = open("key.txt","r")
fm = open("secret.txt","r")
fans = open("ans.txt","w")
msg = fm.read()
lkey = fk.readlines()



for i in range(len(lkey)+1):
    
    try:
        testkey = Fernet(lkey[i])
        ans = testkey.decrypt(msg)
        ans = ans.decode()
        fans.write(ans)
        print(i)
        print(lkey[i])
        print(ans)
        print("done")
    except:
        pass


fk.close()
fm.close()
fans.close()
