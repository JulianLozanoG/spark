import os
import pandas as pd
import xml.etree.ElementTree as ET


class XmlToCsvParser:
    def parse(self, origin, destiny, **kwargs):
        if not os.path.exists(origin):
            raise FileNotFoundError(f"El archivo {origin} no existe.")

        output_file = os.path.join(destiny, os.path.basename(origin).replace('.xml', '.csv'))

        tree = ET.parse(origin)
        root = tree.getroot()

        # Suponiendo que cada nodo hijo tiene los mismos atributos
        data = [child.attrib for child in root]
        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False)
        return f"Archivo convertido en: {output_file}"
