from domain.entitati import film,client
from domain.validare import FilmValidator,ClientValidator,ValidationException
from repository.gestionare import InMemoryRepositoryClienti,InMemoryRepositoryFilme
from service.genereator import Generator

class MoviesService:
    """
        GRASP Controller
        Responsabil de efectuarea operatiilor cerute de utilizator
        Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
        (i.e. declansare actiune: utilizator -> ui-> obiect tip service in ui -> service -> service coordoneaza operatiile
        folosind alte obiecte (e.g. repo, validator) pentru a realiza efectiv operatia)
    """
    def __init__(self, repo, validator):
        """
        Initializeaza service
        :param repo: obiectul de tip repo care ne ajuta sa gestionam lista de filme
        :type repo:InMemoryRepositoryFilm
        :param validator: validatorul pentru verificarea filmelor
        :type validator: FilmValidator
        """
        self.__repo = repo
        self.__validator = validator





    def add_film(self, id, titlu, descriere,inchirieri):
        """
        Adauga film
        :param denumire: denumirea filmului
        :type denumire:str
        :param stoc: numarul de unitati in stoc pentru produs
        :type stoc:int
        :param pret: pretul pe unitate al produsului
        :type pret: float
        :return: produsul adaugat in lista
        :rtype: Product
        :raises: ValueError daca produsul e invalid

        """
        
        f=film(id,titlu,descriere,inchirieri)
        f.setinchiriere(0)
        self.__validator.validate(f)
        self.__repo.store(f)
        return f

    def generatefilm(self,times):
        times=int(times)
        for i in range(times):
            self.add_film(Generator.idrandom(1),Generator.numerandom(10,5),Generator.numerandom(10,10),Generator.numerandom(10,6),Generator.idrandom(0))


    def get_all_movies(self):
        """
        Returneaza o lista cu toate filmele disponibile
        :return: lista de filme disponibile
        :rtype: list of film objects
        """
        return self.__repo.get_all_movies()

    def delete_by_id(self, id):
        """
        Sterge filmyl cu id dat
        :param id: id-ul dat
        :type id: str
        :return: filmul sters
        :rtype: film
        :raises: ValueError daca nu exista filmul cu id-ul dat
        """
        return self.__repo.delete_film(id)

    def update_film(self, id, denumire,descriere,inchirieri):
        """
        Modifica produsul cu id id cu datele date
        :param id: id-ul dat
        :type id: str
        :param denumire: noua denumire a produsului
        :type denumire: str
        :return: produsul modificat
        :rtype: Product
        :raises: ValueError daca nu exista produs cu id dat
        """
        f = film(id, denumire, descriere,inchirieri)
        self.__validator.validate(f)
        return self.__repo.update(id, f)

    def filter_by_name(self, str_to_search):
        """
        Selecteaza filmele care contin str_to_search in nume
        :param str_to_search: string de cautat in numele filmelor
        :type str_to_search: str
        :return: lista de filme care au str_to_search in nume
        :rtype: list of film objects
        """
        all_filme= self.get_all_movies()
        filtered_list = [film for film in all_filme if str_to_search in film.getname()]
        return filtered_list




class ClientsService:
    """
        GRASP Controller
        Responsabil de efectuarea operatiilor cerute de utilizator
        Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
        (i.e. declansare actiune: utilizator -> ui-> obiect tip service in ui -> service -> service coordoneaza operatiile
        folosind alte obiecte (e.g. repo, validator) pentru a realiza efectiv operatia)
    """
    def __init__(self, repo, validator):
        """
        Initializeaza service
        :param repo: obiectul de tip repo care ne ajuta sa gestionam lista de produse
        :type repo:InMemoryRepository
        :param validator: validatorul pentru verificarea produselor
        :type validator: ProductValidator
        """
        self.__repo = repo
        self.__validator = validator



    def add_client(self, id, nume, cnp,inchirieri):
        """
        adauga un client la lista
        """
        
        c=client(id,nume,cnp,inchirieri)
        c.setinchiriere(0)
        self.__validator.validate(c)
        self.__repo.store(c)
        return c


    def generateclient(self,times):
        times=int(times)
        for i in range(times):
            self.add_client(Generator.idrandom(1),Generator.numerandom(10,5),Generator.cnprandom(13),Generator.cnprandom(0))



    def get_all_clients(self):
        """
        returneaza lista cu toti clienti
        """
        return self.__repo.get_all()

    def delete_by_id(self, id):
        """
        Sterge clientul cu id dat
        :param id: id-ul dat
        :type id: str
        :return: client sters
        :rtype: client 
        :raises: ValueError daca nu exista clientul cu id-ul dat
        """
        return self.__repo.delete(id)

    def update_client(self, id, denumire,cnp,inchiriere):
        """
        Modifica produsul cu id id cu datele date
        :param id: id-ul dat
        :type id: str
        :param denumire: noua denumire a produsului
        :type denumire: str
        :return: produsul modificat
        :rtype: Product
        :raises: ValueError daca nu exista produs cu id dat
        """
        c = client(id, denumire,cnp,inchiriere)
        self.__validator.validate(c)
        return self.__repo.update_client(id, c)    
    
    def filter_by_name(self, str_to_search):
        """
        Selecteaza clienti care contin str_to_search in nume
        :param str_to_search: string de cautat in numele clientilor
        :type str_to_search: str
        :return: lista de clienti care au str_to_search in nume
        :rtype: list of client objects
        """
        all_clienti = self.get_all_clients()
        filtered_list = [client for client in all_clienti if str_to_search in client.getname()]
        return filtered_list











def test_add_film():
    test_repo = InMemoryRepositoryFilme()
    test_val = FilmValidator()

    test_srv = MoviesService(test_repo, test_val)

    film = test_srv.add_film(1234, "pulp fiction", "unul dintre cele mai bune filme ","quentin tarantino")
    assert (film.getname() == 'pulp fiction')
    assert (film.getid() == 1234)

    assert (len(test_srv.get_all_movies()) == 1)

    try:
        test_srv.add_film(-1, "pulp fiction", "unul dintre cele mai bune filme ","quentin tarantino")
        assert False
    except ValidationException:
        assert True        

def test_add_client():
    test_repo = InMemoryRepositoryClienti()
    test_val = ClientValidator()

    test_srv = ClientsService(test_repo, test_val)

    client = test_srv.add_client(1234, "Radu Sebastian", 5020822)
    assert (client.getname() == 'Radu Sebastian')
    assert (client.getid() == 1234)

    assert (len(test_srv.get_all_clients()) == 1)

    try:
        test_srv.add_client(1234, "Radu Sebastian", 0)
        assert False
    except ValidationException:
        assert True          


#test_add_client()
#test_add_film()        