import math

m = int(input("Enter lower limit :"))
n = int(input("Enter upper limit :"))

p = []
for i in range(2,n+1):
    p.append(i)

i = 2
while(i <= int(math.sqrt(n))):
    if i in p:
        for j in range(i*2, n+1, i):
            if j in p:
                p.remove(j)
    i = i+1

for k in range(2,n+1):
    if k<m:
        p.remove(k)
print (p)
