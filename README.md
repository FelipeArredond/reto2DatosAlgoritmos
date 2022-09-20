# Problema a resolver
Una empresa que vende productos en 10 centros comerciales de la ciudad y los surte todos los días, cuanta con 4 bodegas y un solo camión de reparto.

Los socios de la empresa se plantean la posibilidad de reducir el número de bodegas a una, para reducir los costos asociados al producto y aumentar la rentabilidad.

Por tal motivo se solicita generar un analisis que argumente cual de las cuatro bodegas se debe conservar.

Por esta razón, el reto preparar los datos y los algoritmos para la propuesta de cual bodega conservar y por que razón.

Consideraciones:
Los 10 puntos comerciales son de libre selección, pero si deben ser centro o plazas comerciales exitentes, sin que el comercio este relacionado. Puede pensar en un marca o seleccionar entre la oferta existente, por ejemplo: comidad, ropa, mercados, etc. e imaginar que su cliente es Presto, Velez, Exíto, como ejemplo si está consideración clarifica la comunicación.
Las 4 bogegas estarán en cualquier punto de la ciudad, seleccionado por usted para el modelo.
Puede apoyarse en Google Maps (https://www.google.com/maps) y GeoMedellin (https://www.medellin.gov.co/geomedellin/index.hyg) para generar y extraer datos
La estructura de datos es libre
La ecuación de costos es libre

# Desarrollo de la solucion
## Centros comerciales seleccionados
1. Arkadia
2. El tesoro
3. Viva Envigado
4. Monterrey
5. Los Molinos
6. Oviedo
7. Viva Laureles
8. Santafe
9. Premium Plaza
10. Plaza Fabricato

## Ubicacion de las bodegas
1. Belen trinidad (Barrio Antioquia)
2. Guayabal
3. Campo Amor
4. Belen Granada

### Grafico de distanicas desde Belen trinidad (w representa km)
![Belen](/graficoTrinidad.drawio.png)

~~~
trinidad = {}
trinidad['arkadia'] = 3.3
trinidad['tesoro'] = 7.2
trinidad['viva_env'] = 7.1
trinidad['monterrey'] = 2.9
trinidad['molinos'] = 3.4
trinidad['oviedo'] = 4.5
trinidad['viva_laur'] = 4.5
trinidad['santafe'] = 6.0
trinidad['premium_plaza'] = 3.2
trinidad['plaza_fabricato'] = 3.3
~~~