import unittest

from domain.entitati import film,client
from domain.validare import FilmValidator,ClientValidator
from exceptions.exceptii import ValidationException


class TestFilme(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator=FilmValidator()

    def test_create_film(self):
        f = film(1234, "pulp fiction", "unul dintre cele mai bune filme",1) 
        self.assertEqual(f.getname(),"pulp fiction")
        self.assertEqual(f.getid(),1234)

        f.setname("shrek")
        self.assertEqual(f.getname(),"shrek")
        f.setdescriere("shrek")
        self.assertEqual(f.getdescriere(),"shrek")

    def test_egal(self):
        f1 = film(1234, "pulp fiction", "unul dintre cele mai bune filme",1) 
        f2 = film(1234, "pulp fiction", "unul dintre cele mai bune filme",1) 
        self.assertEqual(f1,f2)
        f3 = film(1, "forrest gump", "genial ",22)
        self.assertNotEqual(f3,f1)

    def test_validate(self):
       f = film(1234, "pulp fiction", "unul dintre cele mai bune filme",1)     
       self.__validator.validate(f)
       f1 = film(1234, "", "unul dintre cele mai bune filme",1)
       self.assertRaises(ValidationException,self.__validator.validate,f1)








class TestClient(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator=ClientValidator()

    def test_create_client(self):
        c= client(1234, "Radu Sebastian", 5020822232332,0)
        self.assertEqual(c.getname(),"Radu Sebastian")
        self.assertEqual(c.getid(),1234)

        c.setname("Dit")
        self.assertEqual(c.getname(),"Dit")
        c.setcnp(1234567891234)
        self.assertEqual(c.getcnp(),1234567891234)

    def test_egal(self):
        c1= client(1234, "Radu Sebastian", 5020822,0)
        c2= client(1234, "Radu Sebastian", 5020822,0)
        self.assertEqual(c1,c2)
        c3= client(12, "ALex istarati", 5020417,1)
        self.assertNotEqual(c1,c3)

    def test_validate(self):
        c= client(1234, "Radu Sebastian", 5020822232332,0)   
        self.__validator.validate(c)
        c1= client(1234, "", 5020822232332,0) 
        self.assertRaises(ValidationException,self.__validator.validate,c1)