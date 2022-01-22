import unittest
from domain.entitati import rentitem

class TestRentItem(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def test_create_rent_item(self):
        rent_item=rentitem("Radu Senastian","Forrest Gump")
        self.assertEqual(rent_item.getClient,"Radu Sebastian")
        self.assertEqual(rent_item.getFilm,"Forrest Gump")
        