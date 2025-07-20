import unittest
import os
import csv
from sql_traceability.logic.traceability import generate_traceability_report

class TestTraceability(unittest.TestCase):

    def setUp(self):
        self.sql_script = "SELECT id, name, value AS amount INTO new_table FROM old_table;"
        self.output_file = "test_traceability.csv"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_traceability_report(self):
        generate_traceability_report(self.sql_script, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

        with open(self.output_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[0]['tabla_fuente'], 'old_table')
            self.assertEqual(rows[0]['campo_fuente'], 'id')
            self.assertEqual(rows[0]['tabla_destino'], 'new_table')
            self.assertEqual(rows[0]['campo_destino'], 'id')
            self.assertEqual(rows[0]['logica'], 'id')

if __name__ == '__main__':
    unittest.main()
