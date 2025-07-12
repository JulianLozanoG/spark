import os
import zipfile

class ZipFileParser:
    def parse(self, origin, destiny, **kwargs):
        if not os.path.exists(origin):
            raise FileNotFoundError(f"El archivo {origin} no existe.")

        # Crear la carpeta de destino si no existe
        if not os.path.exists(destiny):
            os.makedirs(destiny)

        with zipfile.ZipFile(origin, 'r') as zip_ref:
            extract_path = os.path.join(destiny, os.path.basename(origin).replace('.zip', ''))
            zip_ref.extractall(extract_path)
        return f"Archivo extraído en: {extract_path}"
