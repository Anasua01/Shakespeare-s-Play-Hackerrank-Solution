#Shakespeare's Play Hackerrank Solution in Python Programming

s=input()
s.lower()
flag=0
alphabet= "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    if i not in s.lower():
        print("Italy")
        flag=1
        break
if flag==0:
    print("France")
