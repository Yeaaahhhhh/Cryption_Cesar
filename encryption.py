#basic usage of encryption and decryption



# basic idea and usage of 
letterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

plainText = 'Hello, world'

shift = 2

for i in plainText:
    cipherText = ''
    #if i == ' ':
        #newchar = ' '
        #cipherText += newchar        
    #elif i == ',':
        #newchar = ','
        #cipherText += newchar        
    #elif i == '.':
        #newchar = '.'
        #cipherText += newchar
    #elif (i.lower() in letterList) and (i not in [' ',',','.']):
        #newchar = '.'
        #cipherText += newchar
        
    #optimize it
    symbolList =  [' ',',','.']
    if i.lower() not in letterList:
        newchar = i
        cipherText += newchar
    else:
        newchar = letterList[letterList.index(i.lower()) +shift%26]
        cipherText += newchar
    print(cipherText,end='')
    
    
#def cesar(shift, plainText):
    #for i in plainText:
        #print(pl)