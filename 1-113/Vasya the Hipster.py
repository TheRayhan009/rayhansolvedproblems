red_socks,blue_socks=map(int,input().split())
different_socks_she_can_wear=min(red_socks,blue_socks)
x=max(red_socks,blue_socks)
same_socks=(x-different_socks_she_can_wear)/2
print(different_socks_she_can_wear,int(same_socks))