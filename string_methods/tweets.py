tweets="""what a game,hats off to both teams. well done @benstokes38 @patcummins30 you have bought test
    cricket @thebarmyarmy @cricketaus @ecb_cricket"""
    
words=tweets.split(" ")  
for w in words:
    if w.startswith('@'):
        print(w) 
        

var="pneumonoultramicroscopicsilicovolcanoconiosis"
#vowels
#consonants

vowels='a','e','i','o','u'
v_count=0
c_count=0

for ch in var:
    if ch in vowels:
       v_count+=1
    elif ch.isalpha():
       c_count+=1
            
print(v_count)
print(c_count)
print(len(var))