import base64
def sixfour(aha):
    aha.insert(7, '4')
    aha.insert(15, '2')
    aha.insert(23, '0')
    aha.insert(31, '5')
    aha = ''.join(aha)
    print("aha =",aha)

    aha_sixfour = aha.encode('ascii')
    naja_boy = base64.b64decode(aha_sixfour)
    naja = naja_boy.decode('ascii')
    
    print("flag{"+str(naja)+"}")
    
	

def rolling(realText, step):
	out = []
	cryptText = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for eachLetter in realText:
		if eachLetter in uppercase:
			#print(eachLetter)
			index = uppercase.index(eachLetter)
			#print("index",index)
			crypting = (index + step) % 26
			#print("crypting",crypting)
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			out.append(newLetter)
			#print(f"original letter : {eachLetter} [{index}] crypt to {newLetter} [{crypting}]")
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			out.append(newLetter)
	out.append("=")
	sixfour(out)
	print("(out) =",out)

print("========== Welcome to PRINT ==========")
msg = "UNMtFqHTgY"+"rGATTAMqGDFUAH"+"eFATUqXfVKUsFgL"

rolling(msg,19)
