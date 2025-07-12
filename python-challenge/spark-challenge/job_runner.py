import json
import logging
from parsers.unzip_parser import ZipFileParser
from parsers.xml_to_csv_parser import XmlToCsvParser

logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Nivel de los logs

# Manejador para el archivo (logs/app.log)
file_handler = logging.FileHandler('logs/app.log', mode='a')
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formato para los logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Registro de parsers
PARSERS = {
    "ZipFileParser": ZipFileParser,
    "XmlToCsvParser": XmlToCsvParser
}


def simulate_s3_path(s3_path):
    """Convierte rutas simuladas de S3 a rutas locales."""
    return s3_path.replace("s3://", "./s3_simulation/")


def run_job(job_definition_file):
    """Ejecuta las tareas especificadas en el archivo JSON."""
    try:
        with open(job_definition_file, 'r') as file:
            job_definition = json.load(file)

        for task in job_definition['transformations']:
            obj = task['object']
            parser_class = PARSERS.get(obj['classname'])

            if not parser_class:
                raise ValueError(f"Parser no encontrado: {obj['classname']}")

            origin = simulate_s3_path(obj['origin'])
            destiny = simulate_s3_path(obj['destiny'])
            parser = parser_class()
            result = parser.parse(origin, destiny, **task.get('kwargs', {}))
            logging.info(f"Tarea completada: {result}")
    except Exception as e:
        logging.error(f"Error: {e}")
        raise


if __name__ == "__main__":
    run_job("job_definition.json")
