# Ejemplo adaptado de Match-Case PEP 636
def http_status(cod_estado):
    match cod_estado:
        case 301:
            return "Se movió permanentemente"
        case 400:
            return "Mala solicitud"
        case 401 | 403:
            return "No autorizado o Prohibido"
        case 404:
            return "No encontrado"
        case _:
            return "Otro error"
print(int(http_status(404)))