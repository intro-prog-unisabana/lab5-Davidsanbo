import math 

num=int(input("Enter an integer: "))

valor_log=math.log2(num)
val_piso= math.floor(valor_log)
val_techo= math.ceil(valor_log)
print(f"Log base 2 of {num} is: {valor_log}")
print(f"Floor: {val_piso}")
print(f"Ceiling: {val_techo}")        
