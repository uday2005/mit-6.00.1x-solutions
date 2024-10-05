time_efficiency =0
def fib(n):
    global time_efficiency
    time_efficiency +=1 
    if n ==1:
        return 1
    
    if n ==2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    

why = int(input("What number do you want to print"))
print(fib(why))
print(f"times:{time_efficiency}")

time_efficiency = 0
def fib_eff(n,d):
    global time_efficiency
    time_efficiency +=1
    if n in d: # if n is in dictionary then reurn that dictionary values
        return d[n] # access the dict and take the values of d[n]
    
    else:
        ans = fib_eff(n-1,d)+ fib_eff(n-2,d)#if that fib is not in list then we take a varibale and put that variable in dict
        d[n] = ans
        return ans
    
d = {1:1,2:2}   #intialising base case values

print(fib_eff(why, d))
print(f"times:{time_efficiency}")
