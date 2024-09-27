n=4,54,29,71,7,59,98,23
prime_count=0
composite_count=0
for n in n:
    if n>1:
        for i in range(2,n):
            if n%i==0:
                composite_count+=1
                break
            else:
                prime_count+=1
print("composite number:",composite_count)
print("prime number:",prime_count
      )
    
