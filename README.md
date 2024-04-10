Informe de pruebas automatizadas de la página de Amazon

Descripción general:
Se realizaron pruebas automatizadas utilizando la librería Selenium en Python para verificar el correcto funcionamiento de las principales funcionalidades de la página de Amazon. Las pruebas se ejecutaron en un entorno de prueba local utilizando el navegador web Chrome.

Configuración del entorno de prueba:

Sistema operativo: Windows 10
Navegador web: Google Chrome (versión 112.0.5615.138)
Lenguaje de programación: Python (versión 3.9.0)
Frameworks y bibliotecas utilizadas:
Selenium (versión 4.8.2)
Pillow (versión 9.4.0)
Casos de prueba ejecutados:

Inicio de sesión en Amazon
Búsqueda de productos
Agregar producto al carrito de compras
Cerrar sesión
Resultados de las pruebas:

Inicio de sesión en Amazon
Resultado: Aprobado
Detalles: El usuario pudo iniciar sesión correctamente ingresando sus credenciales válidas.
Búsqueda de productos
Resultado: Aprobado
Detalles: El usuario pudo buscar y obtener resultados relevantes para el término de búsqueda ingresado.
Agregar producto al carrito de compras
Resultado: Fallido
Detalles: Al intentar agregar un producto al carrito de compras, se produjo un error inesperado. El carrito de compras no reflejó el producto agregado.
Posible problema: Es posible que haya habido un cambio reciente en la estructura o los elementos de la página web, lo que causó que el localizador utilizado para el botón de "Agregar al carrito" no funcionara correctamente.
Cerrar sesión
Resultado: Aprobado
Detalles: El usuario pudo cerrar sesión correctamente y fue redirigido a la página de inicio de Amazon.
Capturas de pantalla:
Se adjuntan capturas de pantalla automáticas para cada paso de las pruebas en la carpeta "results/screenshots".

Problemas encontrados y recomendaciones:

Error al agregar producto al carrito de compras:
Descripción: Durante la prueba de agregar un producto al carrito de compras, se produjo un error inesperado y el carrito no reflejó el producto agregado.
Recomendación: Se recomienda investigar y actualizar el localizador utilizado para el botón de "Agregar al carrito" para asegurar que funcione correctamente con la estructura actual de la página web.
Capturas de pantalla:
Recomendación: Aunque se lograron generar capturas de pantalla automáticas, se recomienda mejorar la calidad y resolución de las imágenes para una mejor visualización y análisis.
