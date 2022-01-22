from domain.entitati import film,client
from exceptions.exceptii import DuplicateIDException, FilmAlreadyAssingedException,FilmMagazinExceptie,FilmnotfoundException,ClientnotfoundException


class ClientRepoFile:
    def __init__(self,filename):
        self.__filename=filename


    def __load_from_file(self):
        with open(self.__filename,"r") as c:

            films=[]
            lines=c.readlines()
            for line in lines:
                client_id,client_name,client_cnp,client_inchirieri=[token.strip() for token in line.split(" ")]
                cli=client(client_id,client_name,client_cnp,client_inchirieri)
                films.append(cli)

    
        return films

    def __save_to_file(self,filme_list):
        with open(self.__filename,"w") as f:
            for film in filme_list:
                film_string=str(film.getid())+" "+str(film.getname())+" "+str(film.getcnp())+" "+str(film.getinchirieri())+"\n"
                f.write(film_string)

    def find(self,id):
        all_filme=self.__load_from_file()
        for film in all_filme:
            if film.getid()==id:
                return film
        return None

    def __find_by_index(self,all_filme,id):
        index=-1
        for i in range(len(all_filme)):
            if all_filme[i].getid()==id:
                index=i
        return index

    def __find_index_rec(self,i,all_filme,id):
        if i<range(len(all_filme)):
            if all_filme[i].getid()==id:
                index=i
                return index
            else:
                self.__find_index_rec(i+1,all_filme,id)         
        else:
            return -1


    def store(self,film):
        """
        Adauga film in lista
        :param product: filmul de adaugat
        :type product: film
        :return: -; lista de produse se modifica prin adaugarea filmului dat
        :rtype:
        :raises:
        
        """

        all_filme=self.__load_from_file()
        if film in all_filme:
            raise DuplicateIDException()

        all_filme.append(film)
        self.__save_to_file(all_filme)

    def update(self,id,new_film):
        """
        Modifica un film
        :param id: id-ul filmului de modificat
        :type id: str
        :return: filmul modificat
        :rtype: film
        :raises: ValueError daca nu exista film cu identificator id in lista
        
        """
        all_filme=self.__load_from_file() 
        index=self.__find_index_rec(all_filme,id)
        if index==-1:
            raise FilmnotfoundException()

        all_filme[index]=new_film
        self.__save_to_file(all_filme)
        return new_film


    def delete(self,id):
        """
        Sterge filmul cu id dat
        :param id: id dat
        :type id: str
        :return: filmul sters
        :rtype: film
        """ 
        
        all_filme=self.__load_from_file() 
        index=self.__find_by_index(all_filme,id)
        if index==-1:
            raise FilmnotfoundException()

        d=all_filme.pop(index)
        self.__save_to_file(all_filme)
        return d   

    def size(self):
        return len(self.__load_from_file())

    def delete_all(self):
        self.__save_to_file([])

    def get_all(self):
        return self.__load_from_file()

    def inchiriat(self,client):
        
        all_clienti=self.__load_from_file()


        try:
            client.getid()
        except ValueError :
            print("Nu exista filmul .")
            return
        
        c=client.getinchirieri()
        c=int(c)
        c=c+1
        client.setinchiriere(c)
        id=client.getid()
        index=self.__find_by_index(all_clienti,id)
        if index==-1:
            raise ClientnotfoundException()

        all_clienti[index]=client
        self.__save_to_file(all_clienti)
        return client        



class FilmRepoFile:
    def __init__(self,filename):
        self.__filename=filename


    def __load_from_file(self):
        f=open(self.__filename,"r")

        films=[]
        lines=f.readlines()
        for line in lines:
            film_id,film_name,film_descriere,film_inchirieri=[token.strip() for token in line.split(" ")]
            fil=film(film_id,film_name,film_descriere,film_inchirieri)
            films.append(fil)

        f.close()
        return films

    def __save_to_file(self,filme_list):
        with open(self.__filename,"w") as f:
            for film in filme_list:
                film_string=str(film.getid())+" "+str(film.getname())+" "+str(film.getdescriere())+" "+str(film.getinchirieri())+"\n"
                f.write(film_string)

    def find(self,id):
        all_filme=self.__load_from_file()
        for film in all_filme:
            if film.getid()==id:
                return film
        return None

    def __find_by_index(self,all_filme,id):
        index=-1
        for i in range(len(all_filme)):
            if all_filme[i].getid()==id:
                index=i
        return index

    def store(self,film):
        """
        Adauga film in lista
        :param product: filmul de adaugat
        :type product: film
        :return: -; lista de produse se modifica prin adaugarea filmului dat
        :rtype:
        :raises:
        
        """

        all_filme=self.__load_from_file()
        if film in all_filme:
            raise DuplicateIDException()

        all_filme.append(film)
        self.__save_to_file(all_filme)

    def update(self,id,new_film):
        """
        Modifica un film
        :param id: id-ul filmului de modificat
        :type id: str
        :return: filmul modificat
        :rtype: film
        :raises: ValueError daca nu exista film cu identificator id in lista
        
        """
        all_filme=self.__load_from_file() 
        index=self.__find_by_index(all_filme,id)
        if index==-1:
            raise FilmnotfoundException()

        all_filme[index]=new_film
        self.__save_to_file(all_filme)
        return new_film


    def delete(self,id):
        """
        Sterge filmul cu id dat
        :param id: id dat
        :type id: str
        :return: filmul sters
        :rtype: film
        """ 
        
        all_filme=self.__load_from_file() 
        index=self.__find_by_index(all_filme,id)
        if index==-1:
            raise FilmnotfoundException()

        d=all_filme.pop(index)
        self.__save_to_file(all_filme)
        return d   

    def size(self):
        return len(self.__load_from_file())

    def delete_all(self):
        self.__save_to_file([])

    def get_all(self):
        return self.__load_from_file()

    def inchiriat(self,film):
        
        all_filme=self.__load_from_file()

        try:
            film.getid()
        except ValueError :
            print("Nu exista filmul .")
            return
        
        f=film.getinchirieri()
        f=int(f)
        f=f+1
        film.setinchiriere(f)
        id=film.getid()
        index=self.__find_by_index(all_filme,id)
        if index==-1:
            raise FilmnotfoundException()

        all_filme[index]=film
        self.__save_to_file(all_filme)
        return film        