import argparse
from sql_traceability.logic.traceability import generate_traceability_report

def main():
    """
    Función principal para la interfaz de línea de comandos.
    """
    parser = argparse.ArgumentParser(description='Genera un informe de trazabilidad a partir de un script SQL.')
    parser.add_argument('sql_file', type=str, help='La ruta al archivo SQL.')
    parser.add_argument('output_file', type=str, help='La ruta al archivo CSV de salida.')
    args = parser.parse_args()

    with open(args.sql_file, 'r') as f:
        sql_script = f.read()

    generate_traceability_report(sql_script, args.output_file)
    print(f"Informe de trazabilidad generado en: {args.output_file}")

if __name__ == '__main__':
    main()
