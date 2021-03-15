'''
calculator function like eval (not the same )
'''
multiplaylist=[]
powerlist=[]
operatorallowed=["+","-","/","*","^"]
numberlist=[]
number=''
lastn=""
lastopr=""
new=False
negative=False
dervative=False
equationslist=[]




def evalfunction(i):
    '''
    that funcation for abstarct to addtion or multiply the equation with out brackets 
    
    '''

    global number,new,negative,dervative,lastn
    '''the ASCII value of a character '0' is 48 and '9' is 57'''
    print("numberlist",numberlist)
    i=i.replace("**","^")
    print("Input",i)
    for n in i:
        checkifnumber=ord(n)
        if checkifnumber>=48 and checkifnumber<=57 or n==".":
            if negative:
                 number+="-"
            number+=n
        elif n =="+":
            addnumber(float(number),True,True)
            lastopr="+"
        elif n =="-":
            if lastn not in operatorallowed:
                addnumber(float(number),True,True)
            negative=True
            lastopr="-"
        elif n =="/":
            addnumber(float(number),False,True)
            dervative=True
            lastopr="/"
        elif n =="*":
            addnumber(float(number),False,True)
            lastopr="*"
        elif n=="^":
            addnumber(float(number),False,False)
            lastopr="^"
        else:
            raise Exception("entar a good equations")
        lastn=n
        
    
    addnumber(float(number),True,True)
    
    print("n",numberlist)
    return solve(numberlist)

def addnumber(n,new,newpart=False):
    ''' that funaction design the equation int 3D array array for addation hava an array fo multiply hava an array for powers'''
    global multiplaylist,powerlist
    if dervative:
        n=1/float(n)
    powerlist.append(n)
    if newpart:
         multiplaylist.append(powerlist)
         powerlist=[]
    if new:
        numberlist.append(multiplaylist)
        multiplaylist=[]
    reset()

def addpowerlist(n,new):
    global multiplaylist,powerlist
    powerlist.append(n)
    if new:
        multiplaylist.append(powerlist)
        powerlist=[]
    reset()

def reset():
    global number,new,negative,dervative
    number=''
    negative=False
    dervative=False

def solve( listnumber):
    ''' find the final result '''
    global numberlist
    x=0
    for numbergroup in listnumber:
        listnumber[x]=totalmultiply(numbergroup)
        x+=1
    numberlist=[]
    return sum(listnumber)
def totalmultiply(l):
    
    r=1
    print("t",l)
    for n in l:
        r=totalpower(n)*r
        print("r",r,l)
    return r
def totalpower(l):
    if len(l)==1:
        return l[0]
    r=l[0]
    p=sum(l[1:])
    return r**p

    
def getthefunction(i):
    ''' solve the brackets first using eval funcation'''
    if i.find("(") == -1 and i.find(")") == -1:
        return evalfunction(i)
    firstbrackets,lastbrackets=findthebrackets(i)
    print("se",firstbrackets,lastbrackets)
    valuereplaced=str(evalfunction(i[firstbrackets+1:lastbrackets]))
    
    i=i.replace(i[firstbrackets:lastbrackets+1],valuereplaced)
    print("i",i)
    return getthefunction(i)
def findthebrackets(i):
    ''' find the brackets and what close it'''
    checkbrackets=[]
    
    first=0
    last=len(i)-1
    x=0
    for s in i:
        if s == "(":
            checkbrackets.append("(")
            first=x
        elif s ==")":
            if len(checkbrackets) ==0:
                 raise Exception("the brackets is error")
            checkbrackets.pop("(")
            last=x
        x+=1
        if len(checkbrackets) !=0:
            raise Exception("the brackets is not closed")
    return (first,last)
inputeq=input("please entar the equation \n")
if len(inputeq) ==0:
    raise Exception("entar a good equations")

print("fl",getthefunction(str(inputeq)))