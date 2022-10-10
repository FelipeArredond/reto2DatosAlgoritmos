from nodes import *

acumuladorDistanciaAnteriorCamino = 1022012001021**10
mejoresCaminos = []
def circuitoHamiltoniano(bodegas, bodega, centro_comercial, visitados, camino, n, acumuladorDistanciaCaminoActual, mejor):
    if len(camino) == n:
        for cc in camino:
            acumuladorDistanciaCaminoActual += cc[1]

        acumuladorDistanciaCaminoActual += bodega[mejor[0][len(mejor[0])-1][0]]['distanciaBodega']
        mejor[1] = acumuladorDistanciaCaminoActual
        
        if acumuladorDistanciaCaminoActual < acumuladorDistanciaAnteriorCamino: 
            globals()['mejoresCaminos'] += mejor[0]
            globals()['acumuladorDistanciaAnteriorCamino'] = acumuladorDistanciaCaminoActual
        return
    
    for centroComercial in bodega[centro_comercial]['conexiones']:
        if centroComercial[0] not in visitados:
            visitados.append(centroComercial[0])
            camino.append(centroComercial)
            mejor = [camino, 0]
            
            circuitoHamiltoniano(bodegas, bodega, centroComercial[0], visitados, camino, n, acumuladorDistanciaCaminoActual, mejor)

            visitados.pop()
            camino.pop()

def hamiltoniano(bodegas, centroscomerciales, n):
    mejoresCaminosBodegas = []
    distanciasMejoresCaminosBodegas = []
    for bodega in bodegas:
        camino = [['bodega', 0]]
        visitados = ['bodega']

        circuitoHamiltoniano(bodegas, bodega, centroscomerciales[0], visitados, camino, n, 0, [])

        mejorCaminoBodega = [mejoresCaminos[len(mejoresCaminos)-len(centros_comerciales)+1 : len(mejoresCaminos)]]
        mejoresCaminosBodegas += mejorCaminoBodega
        distanciasMejoresCaminosBodegas += [acumuladorDistanciaAnteriorCamino]
    return mejoresCaminosBodegas, distanciasMejoresCaminosBodegas

def ImprimirMejorBodega(mejoresCaminosBodegas):
    distanciaMejorBodega = min(mejoresCaminosBodegas[1])
    indiceMejorBodega = mejoresCaminosBodegas[1].index(min(mejoresCaminosBodegas[1]))
    nombreMejorBodega = nombresBodegas[indiceMejorBodega]
    caminoMejorBodega = mejoresCaminosBodegas[0][indiceMejorBodega]
    
    print(f'La mejor bodega es: {nombreMejorBodega}\nEl camino recorrido por el carro es: || {nombreMejorBodega} -> {caminoMejorBodega} -> {nombreMejorBodega} ||, y la distancia total recorrida es de: {distanciaMejorBodega}Km')


if __name__ == '__main__':
    mejoresCaminosBodegas = hamiltoniano(bodegas, centros_comerciales, len(centros_comerciales))
    
    ImprimirMejorBodega(mejoresCaminosBodegas)
