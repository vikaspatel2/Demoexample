def swap_values(a, b):
    temp = a
    a = b
    b = temp
    return a, b
    
    
    
    OR
    
    
  
  
x = 10
y = 20
   print("Before swap: x =", x, "and y =", y)
x, y = swap_values(x, y)

   print("After swap: x =", x, "and y =", y)

Before swap: x = 10 and y = 20
After swap: x = 20 and y = 10
