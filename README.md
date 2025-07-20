# Trazabilidad de SQL

Esta herramienta genera un informe de trazabilidad a partir de un script SQL. Proporciona una interfaz web para introducir un script SQL y ver el informe de trazabilidad.

**Demo en vivo:** [https://mjmc4498.github.io/TrabilidadSQL](https://mjmc4498.github.io/TrabilidadSQL)

**Autor:** [mjmc4498](https://github.com/mjmc4498)

## Manual del Sistema

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/mjmc4498/TrabilidadSQL.git
    cd TrabilidadSQL
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución de la Aplicación

1.  **Inicia el servidor Flask:**
    ```bash
    python app.py
    ```

2.  Abre tu navegador web y navega a `http://127.0.0.1:5000`.

## Manual de Usuario

1.  Introduce tu script SQL en el área de texto.
2.  Haz clic en el botón "Generar Trazabilidad".
3.  El informe de trazabilidad se mostrará en una tabla debajo del área de texto.

## Contribuciones

Las pull requests son bienvenidas. Para cambios importantes, por favor abre un issue primero para discutir lo que te gustaría cambiar.

Por favor, asegúrate de actualizar las pruebas según corresponda.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
