from domain.entitati import client, rentitem
from exceptions.exceptii import FilmAlreadyAssingedException,ClientnotfoundException,FilmMagazinExceptie,FilmnotfoundException

class InchireireRepoMemory:
    def __init__(self) :
        self.__items=[]

    def find(self,rent_item):
       """
        Cauta un rent item in lista
        :param rent_item: rent item cautat
        :type rent_item: RentItem
        :return: RentItem daca exista in lista, None altfel
        :rtype: RentItem
       """    
       for item in self.__items :
           if item==rent_item:
                return item
       return None      

    def store(self,rent_item):
        """
        Adauga un rent item
        :param rent_item: rent item de adaugat
        :type rent_item: SaleItem
        :return:-; se adauga Rentitem in lista
        :raises: FilmAlreadyAssignedException daca exista deja item pentru film
        """  
        s=self.find(rent_item)
        if s is not None:
            raise FilmAlreadyAssingedException()

        self.__items.append(rent_item)


    def get_all(self):
        """
        Returneaza toti itemi din lista
        :return:lista de itemi
        :rtype:list of RentItem objects

        """     
        return self.__items


class RentItemRepoFile(InchireireRepoMemory):
    def __init__(self,filename):
        InchireireRepoMemory.__init__(self)
        self.__filename=filename
        #self.__load_from_file()

    def __save_to_file(self):
        all_items=InchireireRepoMemory.get_all(self)
        f=open(self.__filename,"w")
        for item in all_items:
            item_string=str(item.getFilm().getname())+" "+str(item.getClient().getname())+"\n"
            f.write(item_string)

    def store(self, rent_item):
        """
        Adauga un rent item
        :param sale_item: rent item de adaugat
        :type sale_item: RentItem
        :return:-; se adauga RentItem in lista si in fisier
        t
        """
        InchireireRepoMemory.store(self, rent_item)
        self.__save_to_file()            
        
    def find(self, rent_item):
        # TO DO: add specification
        return InchireireRepoMemory.find(self, rent_item)

    def delete_all(self):
        """
        Sterge toti sale items din lista (si fisier)
        """
        InchireireRepoMemory.delete_all(self)
        self.__save_to_file()      

        