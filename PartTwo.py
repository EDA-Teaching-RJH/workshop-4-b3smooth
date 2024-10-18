tf = False
Utotal=0
while tf==False:
    Uval=input("please input your cash, 5,10,20,50 pence coins are accepted ")
    Sval=""
    if (type(Uval)==int):
        Uval=Uval
    else:
        for i in Uval:
            if(i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0"):
                Sval+=i
    
    if(Sval=="5" or Sval=="10" or Sval=="20" or Sval=="50"):
        Utotal+=int(Sval)
        print("total due="+str(75-Utotal))
        if(Utotal>=75):
            tf=True
    else:
        print("invalid currency")
    



print("Your change is "+ str(Utotal-75)+"p")