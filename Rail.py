#########################################
##### railfence Encryption function #####
#########################################
"""
 encryption(2, 'meetmeafterthetogaparty')

 output --> 'mematrhtgpryetefeteoaat'
"""
def encryption(key, text):
    
    text = text.replace(' ','')# remove spaces from plaintext
    
    cipherText = [""] * key #empty num of rows = key 
    
    for row in range(key):
        pointer = row
        while pointer < len(text):
            cipherText[row] += text[pointer] #mema --ete
            pointer += key
        print(cipherText[row])
   # return cipherText
    return "".join(cipherText)

########################################################
text= input("Enter message: ") 
text = text.replace(' ','')
key = int(input("Enter key [2-%s]: " % (len(text) - 1)))

print("the cipher text = " , encryption(key,text))