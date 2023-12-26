a,b=list(map(int,input().split()))
ans=0
for N in range(a,b+1)
	bad=0
	for i in range(2,N)
		if N%i==0bad=1
	if bad==0ans+=1
print(ans)