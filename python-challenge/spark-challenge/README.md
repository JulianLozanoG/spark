# Proyecto S3 Transformations

Este proyecto ejecuta transformaciones especificadas en un archivo JSON. Simula S3 con rutas locales.

## Requisitos
1. Python 3.9+
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto
- `logs/`: Contiene logs en tiempo de ejecución.
- `parsers/`: Parsers para realizar las transformaciones.
- `s3_simulation/`: Almacén local que simula S3.
- `job_definition.json`: Definición del trabajo.
- `job_runner.py`: Script principal.

## Ejecución
Ejecuta el proyecto con:
```bash
python job_runner.py
```
Los resultados estarán en `s3_simulation/`.