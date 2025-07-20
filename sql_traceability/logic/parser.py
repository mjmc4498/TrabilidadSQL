import sqlparse
from sqlparse.sql import Identifier, IdentifierList

def parse_sql(sql):
    """
    Analiza un script SQL para extraer información de trazabilidad.

    Args:
        sql (str): El script SQL a analizar.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa una columna
              y contiene 'tabla_fuente', 'campo_fuente', 'tabla_destino',
              'campo_destino' y 'logica'.
    """
    parsed = sqlparse.parse(sql)[0]
    columns_data = []

    # Asumimos que la primera tabla en un FROM es la fuente principal
    # y la tabla en el INTO es el destino.
    source_table = None
    destination_table = None

    from_seen = False
    into_seen = False

    # Extraer nombres de tablas
    tokens = parsed.tokens
    for i, token in enumerate(tokens):
        if token.is_keyword and token.normalized == 'FROM':
            next_token = tokens[i+2]
            if isinstance(next_token, Identifier):
                source_table = next_token.get_real_name()
        if token.is_keyword and token.normalized == 'INTO':
            next_token = tokens[i+2]
            if isinstance(next_token, Identifier):
                destination_table = next_token.get_real_name()

    # Extraer las columnas
    for token in parsed.tokens:
        if isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                identifier_str = str(identifier)
                if ' AS ' in identifier_str.upper():
                    logic, alias = identifier_str.split(' AS ')
                    source_field = logic.strip()
                    destination_field = alias.strip()
                else:
                    logic = identifier_str
                    source_field = identifier.get_real_name()
                    destination_field = identifier.get_real_name()

                columns_data.append({
                    'tabla_fuente': source_table,
                    'campo_fuente': source_field,
                    'tabla_destino': destination_table,
                    'campo_destino': destination_field,
                    'logica': logic.strip()
                })

    return columns_data
