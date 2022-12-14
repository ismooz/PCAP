text1 = input("Please enter a text :")
text2 = input("Pleas enter a second text :")

text1 = text1.lower().split()
text2 = text2.lower().split()

def strToOrd(text):
    word_sum = 0
    for word in text:
        for l in word:
            word_sum += ord(l)
    return word_sum

def isAnagrams(text1, text2):    
    if strToOrd(text1) == strToOrd(text2):
        print("Anamgrams")
    else:
        print("Not anagrams")
        
isAnagrams(text1, text2)