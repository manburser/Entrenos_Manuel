
from entrenos import*

def test_lee_entrenos(datos):
    print("Prueba de la función lee_entrenos")
    print(f"Se han leído {len(datos)} entrenos")
    print(f"Los tres primeros son: {datos[:3]}")

def test_tipo_entreno(datos):
    print("Prueba dee la función tipos_entreno")
    tipos = tipos_entreno(datos)
    print(f'Los tipos de entreno son:{tipos}')

if __name__=='__main__':
    datos = lee_entrenos("data/entrenos.csv")
    test_lee_entrenos(datos)
    test_tipo_entreno(datos)