import csv
from sql_traceability.logic.parser import parse_sql

def generate_traceability_report(sql_script, output_file):
    """
    Genera un informe de trazabilidad en formato CSV a partir de un script SQL.

    Args:
        sql_script (str): El script SQL a analizar.
        output_file (str): La ruta del archivo CSV de salida.
    """
    columns_data = parse_sql(sql_script)

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['tabla_fuente', 'campo_fuente', 'tabla_destino', 'campo_destino', 'logica']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data in columns_data:
            writer.writerow(data)
