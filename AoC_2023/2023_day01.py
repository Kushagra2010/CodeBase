file1 = open(r"C:\Users\swati\Kushagra\Temp\AoC2023\Input1_1.txt", "r+")

allnumbers = []
for word in file1:
    #print(word)
    digits = []

    
    for i in word:
        if i.isdigit():
            digits.append(i)
    allnumbers.append(digits)
    #print(allnumbers)

total = []
for x in allnumbers:
    total.append((int(x[0])*10) + int(x[-1]))
    
print(sum(total))
=========================================

file1 = open(r"C:\Users\swati\Kushagra\Temp\AoC2023\Input1_1.txt", "r+")

dicrefrence = {"one":"1",
"two":"2",
"three":"3",
"four":"4",
"five":"5",
"six":"6",
"seven":"7",
"eight":"8",
"nine":"9",
"zero":"0",
"1":"1",
"2":"2",
"3":"3",
"4":"4",
"5":"5",
"6":"6",
"7":"7",
"8":"8",
"9":"9",
"0":"0"}

total=[]
for word in file1:
    #print(word)
    
    bothnumber=[]
    
    i=0
    breakloop = 0
    for x in word:
        if breakloop==1:
            break
        #print(word[0:i])
        i+=1
        for key in dicrefrence:
            #print("Print Key from Dictionary: "+ key)
            if key in word[0:i]:
                #print("Printing sliced string: " + word[0:i])
                bothnumber.append(dicrefrence.get(key))
                #print("printing matched key :" + key)
                breakloop = 1
                break
                
    
    #print("###second loop###") 
       
    # y=len(word)
    # for x in word:
    #     print(word[y-1:])
    #     y-=1
    
    i=len(word)
    breakloop = 0
    for x in word:
        if breakloop==1:
            break
        #print(word[i-1:])
        i-=1
        for key in dicrefrence:
            #print("Print Key from Dictionary: "+ key)
            if key in word[i-1:]:
                bothnumber.append(dicrefrence.get(key))
                #print("printing matched key :" + key)
                breakloop = 1
                break
    #print(bothnumber)
    
    total.append((int(bothnumber[0])*10) + int(bothnumber[1]))

        
print(total)      
print(sum(total))
    
    
    
            

 
    
    
    
            

