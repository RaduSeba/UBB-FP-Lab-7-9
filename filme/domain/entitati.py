
class  film () :
    def __init__(self,id,titlu,descriere,inchirieri):    
        
        self.__name=titlu
        self.__id=id
        self.__descriere=descriere
        self.__inchiriere=inchirieri

    def getname(self):
        return self.__name 

    def getid(self):
        return self.__id     

    def getdescriere(self):
        return self.__descriere

    def getinchirieri(self):
        return self.__inchiriere

    def setname(self,value):
        self.__name=value

    def setid(self,value):
        self.__id=value

    def setdescriere(self,value):
        self.__descriere=value

    def setinchiriere(self,value):
        self.__inchiriere=value

   

    def __eq__(self, other):
        """
        Verifica egalitatea
        :param other: filmul cu care se compara filmul curent
        :type other: film
        :return: True daca produsele sunt identice (au acelasi nume si acelasi pret pe unitate), False altfel
        :rtype: bool
        """
        if self.__name == other.getname() and self.__id == other.getid() and self.__descriere==other.getdescriere() and self.__inchiriere==other.getinchiriere():
            return True
        return False 
        

    
    def __str__(self):
        return " Denumire: " + str(self.__name) + '\n ID: ' + str(self.__id) + '\n Descriere: ' + str(self.__descriere)+"\n Inchirieri:" +str(self.__inchiriere)
    

class  client () :
    def __init__(self,id,nume,cnp,inchirieri):    
        
        self.__name=nume
        self.__id=id
        self.__cnp=cnp
        self.__inchirieri=inchirieri
        

    def getname(self):
        return self.__name 

    def getid(self):
        return self.__id     

    def getcnp(self):
        return self.__cnp

    def getinchirieri(self):
        return self.__inchirieri


    def setname(self,value):
        self.__name=value

    def setid(self,value):
        self.__id=value

    def setcnp(self,value):
        self.__cnp=value
    
    def setinchiriere(self,value):
        self.__inchirieri=value

    def __eq__(self, other):
        """
        Verifica egalitatea
        :param other: filmul cu care se compara filmul curent
        :type other: film
        :return: True daca produsele sunt identice (au acelasi nume si acelasi pret pe unitate), False altfel
        :rtype: bool
        """
        if self.__name == other.getname() and self.__id == other.getid() and self.__cnp==other.getcnp() and self.__inchirieri==other.getinchirieri() :
            return True
        return False                              
    
    def __str__(self):
        return " Denumire: " + str(self.__name) + '\n ID: ' + str(self.__id) + '\n CNP: ' + str(self.__cnp) + "\n Inchirieri:"+str(self.__inchirieri)

class rentitem:
    def __init__(self,film,client):
        self.__film=film
        self.__client=client

    def getFilm(self):
        return self.__film

    def getClient(self):
        return self.__client

    def setFilm(self,value):
        self.__film=value 

    def setClient(self,value):
        self.__client=value    

    """
    def __eq__(self,other):
        if  self.__client.getid()==other.__self.client.getid():
           return True
        return False
    """

    def __str__(self):
        return "Clientul :" + str(self.__client.getname()) +", " + "Filmul :" + str(self.__film.getname())    

















def test_create_film():
    f = film(1234, "pulp fiction", "unul dintre cele mai bune filme",1)
    assert (f.getname() == 'pulp fiction')
    assert (f.getid() == 1234)
    assert (f.getdescriere() == 'unul dintre cele mai bune filme')
    assert(f.getautor()=="quentin tarantino")

    f.setname("forrest gump")
    assert (f.getname() == 'forrest gump')
    f.setid(25)
    f.setdescriere("genial")
    f.setautor("tom hanks")

    assert (f.getautor() == "tom hanks")
    assert (f.getid() == 25)
    assert(f.getdescriere()=="genial")


def test_equal_films():
    f1 = film(1234, "pulp fiction", "unul dintre cele mai bune filme ","quentin tarantino")
    f2 = film(1234, "pulp fiction", "unul dintre cele mai bune filme ","quentin tarantino")
    #assert (f1 == f2)

    
    f3 = film(1234, "forrest gump", "genial ","tom hanks")
    #assert (f1 != f3)


def test_create_client():
    c= client(1234, "Radu Sebastian", 5020822,1)
    assert (c.getname() == 'Radu Sebastian')
    assert (c.getid() == 1234)
    assert (c.getcnp() == 5020822)
    

    c.setname("dit")
    assert (c.getname() == 'dit')
    c.setid(25)
    c.setcnp(5020714)
    

    assert (c.getcnp() == 5020714)
    assert (c.getid() == 25)


def test_equal_clienti():
    c1= client(1234, "Radu Sebastian", 5020822,0)
    c2= client(1234, "Radu Sebastian", 5020822,0)
    assert (c1 == c2)

    
    c3= client(12, "ALex istarati", 5020417,1)
    assert (c1 != c3)







#test_create_film()
#test_equal_films()
#test_create_client()
#test_equal_clienti()