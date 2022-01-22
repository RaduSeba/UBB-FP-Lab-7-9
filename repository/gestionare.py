from domain.entitati import client, film
from exceptions.exceptii import ClientnotfoundException, DuplicateIDException, FilmnotfoundException


class InMemoryRepositoryFilme:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de filme (i.e. sa ofere un depozit persistent pentru obiecte
        de tip film)

        Create,update,delete,find

        """

    def __init__(self):
    

        self.__filme = {}

    def find(self,id):
        """
        Cauta un film cu id-ul dat in lista
        :param id: id-ul dat
        :type id: str
        :return: filmul cu id-ul dat, None daca nu exista film cu id-ul cautat
        :rtype: film
        """
        id=int(id)
        if id in self.__filme:
            return self.__filme[id]
        return None    



    def store(self, film):
        """
        Adauga film in lista
        :param product: filmul de adaugat
        :type product: film
        :return: -; lista de produse se modifica prin adaugarea filmului dat
        :rtype:
        :raises:
        """
        if film.getid() in self.__filme:
           raise DuplicateIDException()
        
        self.__filme[film.getid()]=film



    # adauga in lista
    # sterge din lista
    # modifica element din list
    # cauta element in lista

    def get_all_movies(self):
        """
        Returneaza o lista cu toate filmele disponibile
        :rtype: list of film objects
        """
        return list(self.__filme.values())
    
    def size(self) :
        """
        Returneaza numarul de filme din lista
        :return: numarul de filme din lista
        :rtype:int

        """
        return len(self.__filme)

    def delete_film(self,id):
        """
        Sterge filmul cu id dat
        :param id: id dat
        :type id: str
        :return: filmul sters
        :rtype: film
        """ 
        id=int(id)
        if id not in self.__filme:
            raise FilmnotfoundException()

        film=self.__filme[id]
        del self.__filme[id]
        return film    

    def update_film(self,id,film):
        
        """
        Modifica un film
        :param id: id-ul filmului de modificat
        :type id: str
        :return: filmul modificat
        :rtype: film
        :raises: ValueError daca nu exista film cu identificator id in lista
        """ 
        id=int(id)
        if id not in self.__filme:
            raise FilmnotfoundException()
        self.__filme[id]=film
        return film       

    def inchiriat(self,film):
        
        try:
            film.getid()
        except ValueError :
            print("Nu exista filmul .")
            return
        
        id=int(film.getid())
        film=self.__filme[id]
        f=film.getinchirieri()
        f=int(f)
        f=f+1
        film.setinchirieri(f)
        
        return film


    def delete_criteriu(self,filter_function):
        """
        Sterge filme din multime dupa un criteriu dat
        :param filter_function: functia (criteriul dupa care se sterg filmele)
        :type filter_function: function
        :return: numarul de filme sterse
        :rtype: int
        """
        initial_filme=self.size()
        self.__filme=[film for film in self.__filme if not filter_function(film)]
        return initial_filme - self.size()

    def delete_all(self):
        """
        Sterge toate filmele din lista

        """
        self.__filme.clear()

    def get_film_criteriu(self,filter_function):
        """
        Selecteaza elementele din lista care indeplinesc un criteriu
        :param filter_function: functia dupa care se filtreaza
        :type filter_function: function
        :return: lista de filme care indeplinesc criteriul
        :rtype: list of filme
        """
        return[film for film in self.__filme if filter_function(film)]
    





class InMemoryRepositoryClienti:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de produse (i.e. sa ofere un depozit persistent pentru obiecte
        de tip Product)

        

        """

    def __init__(self):
    

        self.__clients = {}

    def find(self,id):
        """
        Cauta un client  cu id-ul dat in lista
        :param id: id-ul dat
        :type id: str
        :return: clientul cu id-ul dat, None daca nu exista client cu id-ul cautat
        :rtype: client 
        """
        id=int(id)
        if id in self.__clients:
            return self.__clients[id]
        return None

    def store(self, client):
        """
        Adauga film in lista
        :param product: filmul de adaugat
        :type product: film
        :return: -; lista de produse se modifica prin adaugarea filmului dat
        :rtype:
        :raises:
        """
        if client.getid() in self.__clients:
            raise DuplicateIDException()

        self.__clients[client.getid()]=client

        
        

    # adauga in lista
    # sterge din lista
    # modifica element din list
    # cauta element in lista

    def get_clienti(self):
        """
        Returneaza o lista cu toate produsele disponibile
        :rtype: list of Product objects
        """
        return list(self.__clients.values())

    def size(self) :
        """
        Returneaza numarul de clienti din lista
        :return: numarul de clienti din lista
        :rtype:int

        """
        return len(self.__client) 

    def delete_client(self,id):
        """
        Sterge filmul cu id dat
        :param id: id dat
        :type id: str
        :return: filmul sters
        :rtype: film
        """ 
        id=int(id)
        if id not in self.__clients:
            raise ClientnotfoundException()

        client=self.__clients[id]
        del self.__clients[id]
        return client    

    def update_client(self,id,client):
        
        """
        Modifica un client
        :param id: id-ul clientului de modificat
        :type id: str
        :return: clientul modificat
        :rtype: client
        :raises: ValueError daca nu exista client cu identificator id in lista
        """ 
        id=int(id)
        if id not in self.__clients:
            raise ClientnotfoundException()
        self.__clients[id]=client
        return client   

    
    def inchiriat(self,client):
        
        try:
           id=int(client.getid())
        except ValueError:
            print("NU exista filmul.")
            return
        client=self.__clients[id]
        c=client.getinchirieri()
        c=int(c)
        c=c+1
        client.setinchiriere(c)
        
        return client     

    def delete_criteriu(self,filter_function):
        """
        Sterge clienti din multime dupa un criteriu dat
        :param filter_function: functia (criteriul dupa care se sterg filmele)
        :type filter_function: function
        :return: numarul de clienti stersi
        :rtype: int
        """
        initial_clienti=self.size()
        self.__client=[client for client  in self.__client if not filter_function(client)]
        return initial_clienti - self.size()

    def delete_all(self):
        """
        Sterge toti clienti din lista

        """
        self.__client.clear()

    def get_client_criteriu(self,filter_function):
        """
        Selecteaza elementele din lista care indeplinesc un criteriu
        :param filter_function: functia dupa care se filtreaza
        :type filter_function: function
        :return: lista de clienti care indeplinesc criteriul
        :rtype: list of clients
        """
        return[client  for client in self.__client if filter_function(client)]



def setup_test_repo1():
    f1 = film(1234, "pulp fiction", "unul dintre cele mai bune filme ","quentin tarantino")
    f2 = film(1233, "forrest gump", "genial ","tom hanks")
    f3=film(2,"dark knight","batman","Cristopher Nolan")
    f4=film(4,"snatch","nice","Guy Ritchie")
    f5=film(10,"Good fellas","wow","Martin Scorsese")

    test_repo=InMemoryRepositoryFilme()
    test_repo.store(f1)
    test_repo.store(f2)
    test_repo.store(f3)
    test_repo.store(f4)
    test_repo.store(f5)
    return test_repo

def setup_test_repo2():
    c1= client(1234, "Radu Sebastian", 5020822)  
    c2=client(1112,"dit",5020714) 
    c3=client(1,"Alexandra Borsan",6020425)
    c4=client(4,"Alex Istrati",5020417)
    c5=(10,"Petrica Maios",5020729)

    test_repo=InMemoryRepositoryClienti()
    test_repo.store(c1)
    test_repo.store(c2)
    test_repo.store(c3)
    test_repo.store(c4)
    test_repo.store(c5)
    return test_repo


def test_store():
    test_repo1=InMemoryRepositoryClienti()
    test_repo2=InMemoryRepositoryFilme()
    f1 = film(1234, "pulp fiction", "unul dintre cele mai bune filme ","quentin tarantino")
    f2 = film(1233, "forrest gump", "genial ","tom hanks")
    c1= client(1234, "Radu Sebastian", 5020822)  
    c2=client(1112,"dit",5020714) 

    test_repo2.store(f1)
    assert(test_repo2.size()==1)
    test_repo2.store(f2)
    assert(test_repo2.size()==2)

    try :
        f1 = film(1234, "pulp fiction", "unul dintre cele mai bune filme ","quentin tarantino") 
        test_repo2.store(f1)
        #assert False
    except ValueError:
        assert True

    test_repo1.store(c1)
    assert(test_repo1.size()==1)
    test_repo1.store(c2)
    assert(test_repo1.size()==2)

    try:
        c1= client(1234, "Radu Sebastian", 5020822) 
        test_repo1.store(c1)
        #assert False
    except ValueError :
        assert True

def test_get_all():
    test_repo1=InMemoryRepositoryFilme()
    test_repo2=InMemoryRepositoryClienti()  
    f1 = film(1234, "pulp fiction", "unul dintre cele mai bune filme ","quentin tarantino")    
    c1= client(1234, "Radu Sebastian", 5020822)  
    test_repo1.store(f1)
    test_repo2.store(c1)

    crt_filme=test_repo1.get_all_movies()
    crt_clienti=test_repo2.get_clienti()

    assert(type(crt_filme)==list)
    assert(type(crt_clienti)==list)
    assert(len(crt_clienti)==1)
    assert(len(crt_filme)==1)
    assert(crt_filme[0].getname()=="pulp fiction")
    assert(crt_clienti[0].getname()=="Radu Sebastian")

def test_size():
    test_repo2=InMemoryRepositoryClienti()
    test_repo1=InMemoryRepositoryFilme()
    f1 = film(1234, "pulp fiction", "unul dintre cele mai bune filme ","quentin tarantino")    
    c1= client(1234, "Radu Sebastian", 5020822)
    test_repo1.store(f1)
    test_repo2.store(c1)

    assert(test_repo1.size()==1)
    assert(test_repo2.size()==1)
    test_repo1.delete_film(1234)
    test_repo2.delete_client(1234)
    assert(test_repo1.size()==0)
    assert(test_repo2.size()==0)

def test_find():
    test_repo2=InMemoryRepositoryClienti()
    test_repo1=InMemoryRepositoryFilme()
    f1 = film(1234, "pulp fiction", "unul dintre cele mai bune filme ","quentin tarantino")    
    c1= client(1234, "Radu Sebastian", 5020822)
    f2 = film(1233, "forrest gump", "genial ","tom hanks")
    c2=client(1112,"dit",5020714)
    test_repo1.store(f1)
    test_repo2.store(c1)
    test_repo2.store(c2)
    test_repo1.store(f1)
    #c=test_repo2.find(1112)
    #assert(c.getname()=="dit")
   # f=test_repo1.find(1233)
   # assert(f.getname()=="forrest gump")

    a=test_repo2.find(123123)
    assert(a is None)
    b=test_repo1.find(52521563)
    assert(b is None)

def test_delete_crietriu():
    test_repo1=setup_test_repo1()
    test_repo2=setup_test_repo2()

    
#test_store()
#test_size()
#test_delete_crietriu()
#test_find()
#test_get_all()