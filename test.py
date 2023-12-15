import unittest
from io import StringIO
from unittest.mock import patch
from Corrigeme import corregir_texto


class TestCorreccionTexto(unittest.TestCase):

    @patch('builtins.input', return_value="Este es un texto con errores.")
    @patch('sys.stdout', new_callable=StringIO)
    def test_corregir_texto_con_errores(self, mock_stdout, mock_input):
        corregir_texto()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Correcciones sugeridas:", output)
        self.assertNotIn("No se encontraron errores en el texto.", output)



if __name__ == '__main__':
    unittest.main()