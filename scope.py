global_int = None
global_str = None

def set_globals(some_int, some_str):
    """Almacenar un entero global y una cadena de texto global."""
    global global_int
    global global_str
    global_int = some_int
    global_str = some_str

def get_globals():
    """Recuperar los valores de las variables globales."""
    global global_int
    global global_str
    lst = [global_int, global_str]
    ret=tuple(lst)
    return ret

print(get_globals())       
set_globals(10, "Hello")
print(get_globals()) 
