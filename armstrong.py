



for num in range(500,1000000):
   
    temp = num
    sum = 0
    while temp>0:
        digit = temp%10
        sum+= digit**3
        temp = temp//10
        if num==sum:
          print("Armstrong no",num) 
        break
         
      
    


