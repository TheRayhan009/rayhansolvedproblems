oparetion=int(input())
for i in range(oparetion):
    normal_time=input()
    normal_time=list(normal_time)
    if normal_time[0]+normal_time[1]=="13":
        print(*"01",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="14":
        print(*"02",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="15":
        print(*"03",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="16":
        print(*"04",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="17":
        print(*"05",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="18":
        print(*"06",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="19":
        print(*"07",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="20":
        print(*"08",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="21":
        print(*"09",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="22":
        print(*"10",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="23":
        print(*"11",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    elif normal_time[0]+normal_time[1]=="00":
        print(*"12",normal_time[2],normal_time[3],normal_time[4]," AM",sep="")
    elif normal_time[0]+normal_time[1]=="12":
        print(*"12",normal_time[2],normal_time[3],normal_time[4]," PM",sep="")
    else:
        print(*normal_time," AM",sep="")
        
    #01:84 -> 01:84 AM