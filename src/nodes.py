trinidad = {}
guayabal = {}
campo_amor = {}
granada = {}

nombresBodegas = ['trinidad', 'guayabal', 'campo_amor', 'granada']
bodegas = [trinidad, guayabal, campo_amor, granada]
centros_comerciales = ['bodega', 'arkadia', 'tesoro', 'viva_env', 'monterrey', 'oviedo', 'viva_laur', 'santafe', 'premium_plaza', 'plaza_fabricato', 'molinos']

trinidad['posicion'] = [6.22451,-75.58530]
trinidad['bodega'] = {
    'distanciaBodega': 0,
    'conexiones': [['arkadia', 3.2], ['tesoro', 6.1], ['viva_env', 7.0], ['monterrey', 2.8], ['oviedo', 4.6], ['viva_laur', 3.8], ['santafe', 5.0], ['premium_plaza', 2.7], ['plaza_fabricato', 12.6], ['molinos', 3.5]]
    }
trinidad['arkadia'] = {
    'distanciaBodega': 3.2,
    'conexiones': [['tesoro', 6.2], ['viva_env', 5.6], ['monterrey', 5.3], ['oviedo', 3.8], ['viva_laur', 5.0], ['santafe', 4.4], ['premium_plaza', 5.0], ['plaza_fabricato', 14.5], ['molinos', 6.2]]
    }
trinidad['tesoro'] = {
    'distanciaBodega': 6.1,
    'conexiones': [['arkadia', 6.2], ['viva_env', 6.5], ['monterrey', 9.8], ['oviedo', 3.3], ['viva_laur', 11.7], ['santafe', 3.0], ['premium_plaza', 5.4], ['plaza_fabricato', 17.8], ['molinos', 9.2]]
    }
trinidad['viva_env'] = {
    'distanciaBodega': 7.0,
    'conexiones': [['arkadia', 5.6], ['tesoro', 6.5], ['monterrey', 9.9], ['oviedo', 4.2], ['viva_laur', 11.0], ['santafe', 3.7], ['premium_plaza', 6.9], ['plaza_fabricato', 18.0], ['molinos', 10.1]]
    }
trinidad['monterrey'] = {
    'distanciaBodega': 2.8,
    'conexiones': [['arkadia', 5.3], ['tesoro', 9.8], ['viva_env', 9.9], ['oviedo', 8.9], ['viva_laur', 2.0], ['santafe', 10.2], ['premium_plaza', 5.3], ['plaza_fabricato', 11.9], ['molinos', 3.7]]
    }
trinidad['molinos'] = {
    'distanciaBodega': 3.5,
    'conexiones': [['arkadia', 3.5], ['tesoro', 9.2], ['viva_env', 10.1], ['monterrey', 3.7], ['oviedo', 6.6], ['viva_laur', 2.1], ['santafe', 7.9], ['premium_plaza', 3.8], ['plaza_fabricato', 14.3]]
    }
trinidad['oviedo'] = {
    'distanciaBodega': 4.6,
    'conexiones': [['arkadia', 3.8], ['tesoro', 3.3], ['viva_env', 4.2], ['monterrey', 8.9], ['viva_laur', 8.7], ['santafe', 0.45], ['premium_plaza', 5.5], ['plaza_fabricato', 15.2], ['molinos', 15.2]]
    }
trinidad['viva_laur'] = {
    'distanciaBodega': 3.8,
    'conexiones': [['arkadia', 5.0], ['tesoro', 11.7], ['viva_env', 11.0], ['monterrey', 2.0], ['oviedo', 8.7], ['santafe', 8.6], ['premium_plaza', 5.4], ['plaza_fabricato', 12.6], ['molinos', 2.1]]
    }
trinidad['santafe'] = {
    'distanciaBodega': 5.0,
    'conexiones': [['arkadia', 4.0], ['tesoro', 3.0], ['viva_env', 3.7], ['monterrey', 10.2], ['oviedo', 0.45], ['viva_laur', 8.6], ['premium_plaza', 4.0], ['plaza_fabricato', 15.9], ['molinos', 7.9]]
    }
trinidad['premium_plaza'] = {
    'distanciaBodega': 2.7,
    'conexiones': [['arkadia', 5.0], ['tesoro', 5.4], ['viva_env', 6.9], ['monterrey', 5.3], ['oviedo', 5.5], ['viva_laur', 5.4], ['santafe', 4.0], ['plaza_fabricato', 11.9], ['molinos', 3.8]]
    }
trinidad['plaza_fabricato'] = {
    'distanciaBodega': 12.6,
    'conexiones': [['arkadia', 14.5], ['tesoro', 17.8], ['viva_env', 18.0], ['monterrey', 11.9], ['oviedo', 15.2], ['viva_laur', 12.6], ['santafe', 15.9], ['premium_plaza', 11.9], ['molinos', 14.3]]
    }

guayabal['posicion'] = [6.19562,-75.59012]
guayabal['bodega'] = {
    'distanciaBodega': 0,
    'conexiones': [['arkadia', 1.2], ['tesoro', 5.0], ['viva_env', 5.0], ['monterrey', 5.4], ['oviedo', 2.6], ['viva_laur', 5.3], ['santafe', 3.8], ['premium_plaza', 4.4], ['plaza_fabricato', 14.7], ['molinos', 4.4]]
    }
guayabal['arkadia'] = {
    'distanciaBodega': 1.2,
    'conexiones': [['tesoro', 6.2], ['viva_env', 5.6], ['monterrey', 5.3], ['oviedo', 3.8], ['viva_laur', 5.0], ['santafe', 4.4], ['premium_plaza', 5.0], ['plaza_fabricato', 14.5], ['molinos', 6.2]]
    }
guayabal['tesoro'] = {
    'distanciaBodega': 5.0,
    'conexiones': [['arkadia', 6.2], ['viva_env', 6.5], ['monterrey', 9.8], ['oviedo', 3.3], ['viva_laur', 11.7], ['santafe', 3.0], ['premium_plaza', 5.4], ['plaza_fabricato', 17.8], ['molinos', 9.2]]
    }
guayabal['viva_env'] = {
    'distanciaBodega': 5.0,
    'conexiones': [['arkadia', 5.6], ['tesoro', 6.5], ['monterrey', 9.9], ['oviedo', 4.2], ['viva_laur', 11.0], ['santafe', 3.7], ['premium_plaza', 6.9], ['plaza_fabricato', 18.0], ['molinos', 10.1]]
    }
guayabal['monterrey'] = {
    'distanciaBodega': 5.4,
    'conexiones': [['arkadia', 5.3], ['tesoro', 9.8], ['viva_env', 9.9], ['oviedo', 8.9], ['viva_laur', 2.0], ['santafe', 10.2], ['premium_plaza', 5.3], ['plaza_fabricato', 11.9], ['molinos', 3.7]]
    }
guayabal['molinos'] = {
    'distanciaBodega': 4.4,
    'conexiones': [['arkadia', 3.5], ['tesoro', 9.2], ['viva_env', 10.1], ['monterrey', 3.7], ['oviedo', 6.6], ['viva_laur', 2.1], ['santafe', 7.9], ['premium_plaza', 3.8], ['plaza_fabricato', 14.3]]
    }
guayabal['oviedo'] = {
    'distanciaBodega': 2.6,
    'conexiones': [['arkadia', 3.8], ['tesoro', 3.3], ['viva_env', 4.2], ['monterrey', 8.9], ['viva_laur', 8.7], ['santafe', 0.45], ['premium_plaza', 5.5], ['plaza_fabricato', 15.2], ['molinos', 15.2]]
    }
guayabal['viva_laur'] = {
    'distanciaBodega': 5.3,
    'conexiones': [['arkadia', 5.0], ['tesoro', 11.7], ['viva_env', 11.0], ['monterrey', 2.0], ['oviedo', 8.7], ['santafe', 8.6], ['premium_plaza', 5.4], ['plaza_fabricato', 12.6], ['molinos', 2.1]]
    }
guayabal['santafe'] = {
    'distanciaBodega': 3.8,
    'conexiones': [['arkadia', 4.0], ['tesoro', 3.0], ['viva_env', 3.7], ['monterrey', 10.2], ['oviedo', 0.45], ['viva_laur', 8.6], ['premium_plaza', 4.0], ['plaza_fabricato', 15.9], ['molinos', 7.9]]
    }
guayabal['premium_plaza'] = {
    'distanciaBodega': 4.4,
    'conexiones': [['arkadia', 5.0], ['tesoro', 5.4], ['viva_env', 6.9], ['monterrey', 5.3], ['oviedo', 5.5], ['viva_laur', 5.4], ['santafe', 4.0], ['plaza_fabricato', 11.9], ['molinos', 3.8]]
    }
guayabal['plaza_fabricato'] = {
    'distanciaBodega': 14.7,
    'conexiones': [['arkadia', 14.5], ['tesoro', 17.8], ['viva_env', 18.0], ['monterrey', 11.9], ['oviedo', 15.2], ['viva_laur', 12.6], ['santafe', 15.9], ['premium_plaza', 11.9], ['molinos', 14.3]]
    }

campo_amor['posicion'] = [6.21545,-75.58454]
campo_amor['bodega'] = {
    'distanciaBodega': 0,
    'conexiones': [['arkadia', 2.4], ['tesoro', 5.0], ['viva_env', 6.0], ['monterrey', 5.1], ['oviedo', 5.6], ['viva_laur', 2.6], ['santafe', 2.9], ['premium_plaza', 3.6], ['plaza_fabricato', 13.9], ['molinos', 5.6]]
    }
campo_amor['arkadia'] = {
    'distanciaBodega': 2.4,
    'conexiones': [['tesoro', 6.2], ['viva_env', 5.6], ['monterrey', 5.3], ['oviedo', 3.8], ['viva_laur', 5.0], ['santafe', 4.4], ['premium_plaza', 5.0], ['plaza_fabricato', 14.5], ['molinos', 6.2]]
    }
campo_amor['tesoro'] = {
    'distanciaBodega': 5.0,
    'conexiones': [['arkadia', 6.2], ['viva_env', 6.5], ['monterrey', 9.8], ['oviedo', 3.3], ['viva_laur', 11.7], ['santafe', 3.0], ['premium_plaza', 5.4], ['plaza_fabricato', 17.8], ['molinos', 9.2]]
    }
campo_amor['viva_env'] = {
    'distanciaBodega': 6.0,
    'conexiones': [['arkadia', 5.6], ['tesoro', 6.5], ['monterrey', 9.9], ['oviedo', 4.2], ['viva_laur', 11.0], ['santafe', 3.7], ['premium_plaza', 6.9], ['plaza_fabricato', 18.0], ['molinos', 10.1]]
    }
campo_amor['monterrey'] = {
    'distanciaBodega': 5.1,
    'conexiones': [['arkadia', 5.3], ['tesoro', 9.8], ['viva_env', 9.9], ['oviedo', 8.9], ['viva_laur', 2.0], ['santafe', 10.2], ['premium_plaza', 5.3], ['plaza_fabricato', 11.9], ['molinos', 3.7]]
    }
campo_amor['molinos'] = {
    'distanciaBodega': 5.6,
    'conexiones': [['arkadia', 3.5], ['tesoro', 9.2], ['viva_env', 10.1], ['monterrey', 3.7], ['oviedo', 6.6], ['viva_laur', 2.1], ['santafe', 7.9], ['premium_plaza', 3.8], ['plaza_fabricato', 14.3]]
    }
campo_amor['oviedo'] = {
    'distanciaBodega': 2.6,
    'conexiones': [['arkadia', 3.8], ['tesoro', 3.3], ['viva_env', 4.2], ['monterrey', 8.9], ['viva_laur', 8.7], ['santafe', 0.45], ['premium_plaza', 5.5], ['plaza_fabricato', 15.2], ['molinos', 15.2]]
    }
campo_amor['viva_laur'] = {
    'distanciaBodega': 6.5,
    'conexiones': [['arkadia', 5.0], ['tesoro', 11.7], ['viva_env', 11.0], ['monterrey', 2.0], ['oviedo', 8.7], ['santafe', 8.6], ['premium_plaza', 5.4], ['plaza_fabricato', 12.6], ['molinos', 2.1]]
    }
campo_amor['santafe'] = {
    'distanciaBodega': 2.9,
    'conexiones': [['arkadia', 4.0], ['tesoro', 3.0], ['viva_env', 3.7], ['monterrey', 10.2], ['oviedo', 0.45], ['viva_laur', 8.6], ['premium_plaza', 4.0], ['plaza_fabricato', 15.9], ['molinos', 7.9]]
    }
campo_amor['premium_plaza'] = {
    'distanciaBodega': 3.6,
    'conexiones': [['arkadia', 5.0], ['tesoro', 5.4], ['viva_env', 6.9], ['monterrey', 5.3], ['oviedo', 5.5], ['viva_laur', 5.4], ['santafe', 4.0], ['plaza_fabricato', 11.9], ['molinos', 3.8]]
    }
campo_amor['plaza_fabricato'] = {
    'distanciaBodega': 13.9,
    'conexiones': [['arkadia', 14.5], ['tesoro', 17.8], ['viva_env', 18.0], ['monterrey', 11.9], ['oviedo', 15.2], ['viva_laur', 12.6], ['santafe', 15.9], ['premium_plaza', 11.9], ['molinos', 14.3]]
    }

granada['posicion'] = [6.22891,-75.59405]
granada['bodega'] = {
    'distanciaBodega': 0,
    'conexiones': [['arkadia', 2.3], ['tesoro', 7.8], ['viva_env', 7.9], ['monterrey', 3.5], ['oviedo', 6.2], ['viva_laur', 3.2], ['santafe', 6.7], ['premium_plaza', 3.3], ['plaza_fabricato', 12.7], ['molinos', 1.6]]
    }
granada['arkadia'] = {
    'distanciaBodega': 2.3,
    'conexiones': [['tesoro', 6.2], ['viva_env', 5.6], ['monterrey', 5.3], ['oviedo', 3.8], ['viva_laur', 5.0], ['santafe', 4.4], ['premium_plaza', 5.0], ['plaza_fabricato', 14.5], ['molinos', 6.2]]
    }
granada['tesoro'] = {
    'distanciaBodega': 7.8,
    'conexiones': [['arkadia', 6.2], ['viva_env', 6.5], ['monterrey', 9.8], ['oviedo', 3.3], ['viva_laur', 11.7], ['santafe', 3.0], ['premium_plaza', 5.4], ['plaza_fabricato', 17.8], ['molinos', 9.2]]
    }
granada['viva_env'] = {
    'distanciaBodega': 7.9,
    'conexiones': [['arkadia', 5.6], ['tesoro', 6.5], ['monterrey', 9.9], ['oviedo', 4.2], ['viva_laur', 11.0], ['santafe', 3.7], ['premium_plaza', 6.9], ['plaza_fabricato', 18.0], ['molinos', 10.1]]
    }
granada['monterrey'] = {
    'distanciaBodega': 3.5,
    'conexiones': [['arkadia', 5.3], ['tesoro', 9.8], ['viva_env', 9.9], ['oviedo', 8.9], ['viva_laur', 2.0], ['santafe', 10.2], ['premium_plaza', 5.3], ['plaza_fabricato', 11.9], ['molinos', 3.7]]
    }
granada['molinos'] = {
    'distanciaBodega': 1.6,
    'conexiones': [['arkadia', 3.5], ['tesoro', 9.2], ['viva_env', 10.1], ['monterrey', 3.7], ['oviedo', 6.6], ['viva_laur', 2.1], ['santafe', 7.9], ['premium_plaza', 3.8], ['plaza_fabricato', 14.3]]
    }
granada['oviedo'] = {
    'distanciaBodega': 6.2,
    'conexiones': [['arkadia', 3.8], ['tesoro', 3.3], ['viva_env', 4.2], ['monterrey', 8.9], ['viva_laur', 8.7], ['santafe', 0.45], ['premium_plaza', 5.5], ['plaza_fabricato', 15.2], ['molinos', 15.2]]
    }
granada['viva_laur'] = {
    'distanciaBodega': 3.2,
    'conexiones': [['arkadia', 5.0], ['tesoro', 11.7], ['viva_env', 11.0], ['monterrey', 2.0], ['oviedo', 8.7], ['santafe', 8.6], ['premium_plaza', 5.4], ['plaza_fabricato', 12.6], ['molinos', 2.1]]
    }
granada['santafe'] = {
    'distanciaBodega': 6.7,
    'conexiones': [['arkadia', 4.0], ['tesoro', 3.0], ['viva_env', 3.7], ['monterrey', 10.2], ['oviedo', 0.45], ['viva_laur', 8.6], ['premium_plaza', 4.0], ['plaza_fabricato', 15.9], ['molinos', 7.9]]
    }
granada['premium_plaza'] = {
    'distanciaBodega': 3.3,
    'conexiones': [['arkadia', 5.0], ['tesoro', 5.4], ['viva_env', 6.9], ['monterrey', 5.3], ['oviedo', 5.5], ['viva_laur', 5.4], ['santafe', 4.0], ['plaza_fabricato', 11.9], ['molinos', 3.8]]
    }
granada['plaza_fabricato'] = {
    'distanciaBodega': 12.7,
    'conexiones': [['arkadia', 14.5], ['tesoro', 17.8], ['viva_env', 18.0], ['monterrey', 11.9], ['oviedo', 15.2], ['viva_laur', 12.6], ['santafe', 15.9], ['premium_plaza', 11.9], ['molinos', 14.3]]
    }
