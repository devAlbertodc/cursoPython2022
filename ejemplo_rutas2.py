import os
from pathlib import Path

fichero_path = Path("directorio1", "quijote1.txt")
with fichero_path.open('r') as file:
    print(file.read())