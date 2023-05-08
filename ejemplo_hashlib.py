import hashlib

fichero = 'quijote1.txt'
fichero_codificado = fichero.encode()
fichero_hash = hashlib.sha512(fichero_codificado)
print(fichero_codificado)
print(fichero_hash.hexdigest())