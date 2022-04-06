a = 45
b = 30
c = 10

print(a + c >= b) # True

print( b-c < a - b) # False 
    #   20 <  15

print( (a > b and b > c) or (b < c and a > b) ) # True
      # (45 > 30 and 30 > 10) or (30 < 10 and 45 > 30)
       #      True          or        False

print( a * b < a * b / c) # False
    #   1350 < 135
    
print( a > c and b) # 30
        