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

### Recursos

 Circuito Hamiltoniano con Python:  <https://www.techiedelight.com/es/print-all-hamiltonian-path-present-in-a-graph/>

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
trinidad['posicion'] = [6.22451,-75.58530]
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

### Grafico de distancias desde Guayabal (w representa km)
![Guayabal](/graficoGuayabal.drawio.png)
~~~
guayabal['posicion'] = [6.19562,-75.59012]
guayabal['arkadia'] = 2.7
guayabal['tesoro'] = 6.6
guayabal['viva_env'] = 3.8
guayabal['monterrey'] = 3.6
guayabal['molinos'] = 5.9
guayabal['oviedo'] = 2.9
guayabal['viva_laur'] = 6.8
guayabal['santafe'] = 2.6
guayabal['premium_plaza'] = 5.9
guayabal['plaza_fabricato'] = 5.9
~~~

### Grafico de distancias desde Campo Amor
![CampoAmor](/graficoCampoAmor.drawio.png)
~~~
campo_amor['posicion'] = [6.21545,-75.58454]
campo_amor['arkadia'] = 1.9
campo_amor['tesoro'] = 4.4
campo_amor['viva_env'] = 5.3
campo_amor['monterrey'] = 1.2
campo_amor['molinos'] = 4.0
campo_amor['oviedo'] = 2.9
campo_amor['viva_laur'] = 4.9
campo_amor['santafe'] = 3.4
campo_amor['premium_plaza'] = 3.1
campo_amor['plaza_fabricato'] = 13.1
~~~

### Grafico de distancias desde Granada
![Granada](/graficoGranada.drawio.png)

~~~
granada['posicion'] = [6.22891,-75.59405]
granada['arkadia'] = 2.6
granada['tesoro'] = 8.7
granada['viva_env'] = 8.0
granada['monterrey'] = 4.4
granada['molinos'] = 1.5
granada['oviedo'] = 6.8
granada['viva_laur'] = 2.6
granada['santafe'] = 6.8
granada['premium_plaza'] = 3.6
granada['plaza_fabricato'] = 13.1
~~~