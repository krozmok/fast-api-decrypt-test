# Guia de configuración

## Sobre la implementación

La API fue desarrollada con el uso de las siguientes librerias:

* Tortoise
* FastApi

**Algo que importante sobre la esctructura de las columnas de la tabla FrequencyTable, se hizo el cambio del nombre de la columna `pk` a `id` por el hecho de que se generaba un error de recursión haciendo uso de tortoise.**

## Creación del contendor

```
git clone <repository>
cd fast-api-decrypt-test
docker-compose -d --build
```

## Sobre los endpoints

* La URL que usaremos por defecto es `localhost:8080`
* Para ejecutar los endpoints y ver la documentación de los metodos implementados podemos revisar `localhost:8080/docs`. Esto gracias a que FastAPI implementa la funcionalidad de Swagger para la documentación de los endpoints.
* Los metodos implementados fueron
  * POST: `/freqlang` -> Inputs: `freqlang`
  * PUT: `/freqlang` -> Inputs: `pk`
  * GET: `/freqlang/{pk}` -> Inputs: `pk`
  * GET: `/freqlang`
  * DELETE: `/freqlang/{pk}` -> Inputs: `pk`
  * POST: `/freqlang/decrypt` -> Inputs: `message`
  * POST: `/freqlang/{pk}/decrypt` -> Inputs: `pk`, `message`

## Notas

* Si se desea ejecutar solo el script de desencriptación dirigirse a la carpeta utils y usar python 3 para ejecutar el script con los parametros por defecto.
* Existe la posibilidad de agregarle una herramienta de migración de base de datos llamado aerich, en este caso decid no implementarlo por ver que el proyecto no escalab a grandes cambios en la estructura de la base de datos, pero se tiene lista la configuración de la base de datos para una implementación de aerich.

## Conclusiones

* Una aplicación bastante interesante, el planteamiento del problema y analisis fue lo más interesante de este desde mi punto de vista.
* La parte que más me tomo tiempo fue el tratar de resolver el problema que encontré con problemas con las base de datos, al parecer hacer uso de la variable pk para la creación de esta columna genera errores de recursión haciendo imposible la implementación de la base de datos. No logre encontrar mucha información de las razones de este error.
* Otra parte a tomar en cuenta es el pasar datos multilineas en formato JSON, en este caso estuve investigando y pues la forma más simple era pasar el texto con los saltos de linea dentro del texto JSON.
* Algo que me demoró en la implementación también fue la implementación de los archivos de configuración de la base de datos. Esto debido a la poca información encontrada en los foros. Sin embargo logre encontrar una referencia que aplicaba buenas practicas para escalar bien proyectos grandes.
