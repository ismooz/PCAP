strng1 = "nabucsor"
strng2 = "Nabucodonosor"

strng1 = strng1.lower()
strng2 = strng2.lower()

def findStrng(strng1, strng2):
    compare = 0
    for l in strng1:
        if l in strng2:
            compare += 1
        else:
            compare += 0
    if compare < len(strng1):
        print("No")
    else:
        print("Yes")
        
findStrng(strng1, strng2)
