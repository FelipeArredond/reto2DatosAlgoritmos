from circuito import *

if __name__ == '__main__':
    mejoresCaminosBodegas = hamiltoniano(bodegas, centros_comerciales, len(centros_comerciales))
    ImprimirMejorBodega(mejoresCaminosBodegas)
