import unittest

from main import app
from unittest.mock import patch

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    @patch("main.create_db_connection")
    def test_get_names(self, mock_db_connection):
        mock_conn = mock_db_connection.return_value
        mock_cursor = mock_conn.cursor.return_value

        mock_cursor.fetchall.return_value = [("Kwabena", 0), ("Afia", 1), ("Kofi", 2)]

        response = self.app.get("/names")
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data["names"]), 3)

    @patch("main.create_db_connection")
    def test_put_names(self, mock_db_connection):
        mock_conn = mock_db_connection.return_value
        mock_cursor = mock_conn.cursor.return_value

        mock_cursor.execute.return_value = None
        mock_conn.commit.return_value = None
        mock_conn.close.return_value = None

        response = self.app.put("/names/Abena")
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "Abena")