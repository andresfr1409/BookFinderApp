<h1 align="center">
  <b>BookFinderApp</b>
</h1>

## Nombre y descripcion 

BookFinderApp es una aplicación web desarrollada con Flask, HTML, CSS y Bootstrap. La aplicación permite a los usuarios buscar información detallada sobre libros mediante la integración e implementación de la API de Google Libros. La experiencia se centra en una única sección de búsqueda, donde los usuarios pueden buscar libros por nombre o autor.

## Capturas de Pantalla

1. ### Seccion de busqueda

![image](https://github.com/andresfr1409/BookFinderApp/assets/138944864/10821c6a-fcb5-4f83-98c2-388854144164)

2. ### Busqueda de libro por su nombre haciendo una solicitud REQUEST.POST a la API

![image](https://github.com/andresfr1409/BookFinderApp/assets/138944864/86cd5a90-7556-4c11-9713-999fba307744)

3. ### Muestra de informacion del libro y resumen corto

![image](https://github.com/andresfr1409/BookFinderApp/assets/138944864/9a1541eb-d917-4be1-ae74-a0a93d4a54e3)

4. ### Redireccion al libro en Google Libros oprimiendo en Mas Informacion

![image](https://github.com/andresfr1409/BookFinderApp/assets/138944864/c3925a36-be5e-4ab2-894e-c4030cbdaf94)

## Funcionalidades principales

- ### Seccion de Busqueda

#### Buscador de Libros

- Implementa un buscador que utiliza la API de Google Libros para buscar libros por nombre o autor.
- Proporciona resultados detallados sobre los libros encontrados.

#### Informacion Detallada del libro

- Muestra detalles importantes del libro, como nombre, imagen de portada, fecha de publicación, autor, número de páginas, un resumen corto.
- Incluye un botón que redirige directamente al libro en Google Libros para una exploración más profunda.

## Tecnologias utilizadas

### Flask

- Se utilizo Flask para crear la aplicación web y gestionar las solicitudes del usuario.

### HTML y CSS

- HTML y CSS se combinan para crear una interfaz de usuario atractiva y amigable.

### Bootstrap

- Bootstrap se utiliza para mejorar la apariencia y la experiencia del usuario, proporcionando un diseño consistente y agradable.

## Instalacion

1. Clonar el repositorio
2. Configurar el entorno virtual y instalar las dependencias con el comando "pip install -r requirements.txt".
3. Ejecuta la aplicación directamente en el archivo app.py.

## Uso 

Una vez que la aplicación esté en ejecución, abre tu navegador y visita http://localhost:5000. Utiliza el buscador de libros para encontrar información detallada sobre tus libros favoritos. Explora los resultados y descubre nuevos títulos de manera sencilla.
