import unittest
from sql_traceability.logic.parser import parse_sql

class TestParser(unittest.TestCase):

    def test_simple_select(self):
        sql = "SELECT id, name, value AS amount INTO new_table FROM old_table;"
        expected = [
            {'tabla_fuente': 'old_table', 'campo_fuente': 'id', 'tabla_destino': 'new_table', 'campo_destino': 'id', 'logica': 'id'},
            {'tabla_fuente': 'old_table', 'campo_fuente': 'name', 'tabla_destino': 'new_table', 'campo_destino': 'name', 'logica': 'name'},
            {'tabla_fuente': 'old_table', 'campo_fuente': 'value', 'tabla_destino': 'new_table', 'campo_destino': 'amount', 'logica': 'value'}
        ]
        result = parse_sql(sql)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
