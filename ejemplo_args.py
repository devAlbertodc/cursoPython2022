#Función sin saber cuantos parametros recibe:
def calculaMedia(*argumentos):
    #Cantidad de argumentos:
    total = 0
    for i in argumentos:
        total += i
    res_final = total / len(argumentos)
    return res_final

a,b,c = 50,10,10
media = calculaMedia(a,b,c)
print(f'La media de {a},{b} y {c} es de {media:.2f}')