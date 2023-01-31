def my_split(string:str, delimeter=" ") -> list:
    c = []
    start = 0
    for index, char in enumerate(string):
        if char == delimeter:
            c.append(string[start:index])
            start = index + 1
    if start == 0:
        return [string]
    c.append(string[start:index + 1])
    
    return c

a = "chkjgkj"
print(my_split(a,"."))



def my_join(li:list, delimeter:str) -> str:
    c = ""
    start = 0
    for char in range(len(li)-1):
        
            li[char] += delimeter
            c += li[char]
    return c +li[-1]

a = ["192", "168", "0","1"]
print(my_join(a,"."))



def my_upper(string:str)->str:
    newstr = ''
    for i in range(len(string)):
        if string[i] >= 'a' and string[i] <= 'z':
            newstr = newstr + chr((ord(string[i]) - 32))
        else:
            newstr = newstr + string[i]
    return newstr
     

print(my_upper("sLudUku"))



def my_lower(string:str)->str:
    newstr = ''
    for i in range(len(string)):
        if string[i] >= 'A' and string[i] <= 'Z':
            newstr = newstr + chr((ord(string[i]) + 32))
        else:
            newstr = newstr + string[i]
    return newstr
     

print(my_lower("sLudUJKFJFLFMVEs"))



def my_strip(string:str)->str:
    newstr = ""
    for i in range(len(string)):
        if string[i] == " ":
            continue
        else:
            newstr += string[i]
    return newstr

print(my_strip("  ksdhfksjf   "))



def my_replace(string:str, string1:str, string2:str) -> str:
    newstr = " "
    for i in range(len(string)):
        if string[i] == string1:
            newstr += string2
        else:
            newstr += string[i]
    return newstr

print(my_replace("dfdfdfrarat", "a", "b"))



def my_find(string:str,substr:str)-> str:
    tup = ""
    for i in range(len(string)):
        for j in range(len(substr)):
                if string[i] == substr[j]:
                    tup += str(i) + ","
    return tup
        

print(my_find("arbukarbtuk","rb"))


def my_count(string:str,substr:str)->int:
    count = 0
    for i in range(len(string)):
        if string[i] == substr:
            count += 1
    return count

print(my_count("abababkjhga","f"))




def my_startswith(string:str,substr:str)->bool:
    try:
        for i in range(len(string)//2):
            if string[i]==substr[i]:
                return True
    except:
        return False
        
print(my_startswith("labracatabra","labr"))


def my_isdigit(string:str)->bool:
    try:
        flag = False
        for i in string:
            if type(int(i)) == int:
                flag = True
        if flag:
            return True
    except:
        return False
    
        
print(my_isdigit("2l2"))

















           
