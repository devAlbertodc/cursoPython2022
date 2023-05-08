from sys import platform

assert('linux' in platform),'Solamente se ejecuta en Linux'
assert('win32' in platform),'Solamente se ejecuta en Windows'
exit(1)

def fun_excepciones():
    try:
        print(10/1)
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    #else:
    #    print("Sin errores")
    finally:
        print("Imprime")

fun_excepciones()