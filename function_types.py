def list_shift(data, nums):
    """Modificar una lista sumando un valor a cada elemento."""
    for n in range(len(data)):
        data[n] += nums
    return print(data)

def calc_avg(num):
    """Calcular el promedio de una lista de flotantes."""
    if len(num) == 0:
        return 0.0
    else:
        resultado = sum(num) / len(num)
    return resultado
def print_normalized(data):
    """Imprimir una lista de flotantes normalizados."""
    return print(data)  

data=[2.0, 4.0, 6.0, 8.0]
prom= calc_avg(data)
list_shift(data, -prom)
print_normalized(data)
