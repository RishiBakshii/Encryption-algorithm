print('Welcome')
print("Rules: Dont open it")

message=input ('Enter message you want to encrypt :')
alphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key = input("Enter a encrypt key of your Choice (at lease 8 Numbers long): ")
encrypt =''

for i in message:
  position=alphabet.find(i)
  newposition=(position+ int(key) )%94
  encrypt+=alphabet [newposition]
output = (encrypt)


print ('Encrypted Message: '+ (output) )
print ('Encryption Key: '+ (key) )