from domain.entitati import client, rentitem
from exceptions.exceptii import FilmAlreadyAssingedException,FilmnotfoundException,FilmMagazinExceptie,ClientnotfoundException
from repository.inchiriere import InchireireRepoMemory

class RentItemService :
    def __init__(self,rent_repo,rent_val,film_repo,client_repo) :
        self.__rent_repo=rent_repo
        self.__rent_val=rent_val
        self.__film_repo=film_repo
        self.__client_repo=client_repo

    def add_rent_item(self,film_id,client_id):
        """
        Adauga un RENT Item
        :param film_id:id-ul filmului
        :type product_id:str
        :param client_id:id-ul clientului
        :type shop_id:str
        :return: RentItem adaugat
        :rtype: RentItem
        :raises: FilmNotFoundException daca nu exista film cu id dat
                 ClientNotFoundException daca nu exista client cu id dat
                 ValidationException daca item-ului nu e valid
                 
        """   
        film=self.__film_repo.find(film_id)
        self.__film_repo.inchiriat(film)
        if film is None:
            raise FilmnotfoundException()

        client=self.__client_repo.find(client_id)
        self.__client_repo.inchiriat(client)
        if client is None:
            raise ClientnotfoundException()

        rent_item=rentitem(film,client)
        self.__rent_repo.store(rent_item)
        #self.__rent_val.validate(rent_item)
        return rent_item

    def get_all(self):
        return self.__rent_repo.get_all() 

    def delete_rent_item(self,film_id,client_id):
        film=self.__film_repo.find(film_id)
        if film is None:
            raise FilmnotfoundException()

        client=self.__client_repo.find(client_id)
        if client is None:
            raise ClientnotfoundException()

        rent_item=rentitem(film,client)
        d=self.__rent_repo.find(rent_item)  
        self.__rent_repo.returnare(d)
        return rent_item  

    def topfilme(self):
        t=self.__film_repo.get_all()
        t.sort(key=lambda i: i.getinchirieri(),reverse=True) 
        return t     

    def topclienti(self):
        c=self.__client_repo.get_all()
        c.sort(key= lambda i: i.getinchirieri(),reverse=True)
        return c        

    def clientifideli(self):
        """
        functia returneaza o lista cu primii 30% cei mai fideli clienti
        vom studia complexitatea :
        Caz favorabil:
        lista contine un singur element: T(n) = 1 ∈ 𝛩(1)
        Caz defavorabil:
        lista contine un numar foarte mare de elemente: T(n) = n/3 ∈ 𝛩(n)
        Caz mediu:
        While poate fi executat 1,2,..n ori (același probabilitate) in functie de lungimea listei.
        Numărul de pași = numărul mediu de iterații
        T(n) = (1 + 2+. . . +n)/n*3 = (n + 1)/6 → T(n) ∈ 𝛩(n)
        
        Complexitate O(n)
        
        """

        c=self.__client_repo.get_all()
        c.sort(key= lambda i: i.getinchirieri(),reverse=True)
        r=int(len(c))*3/10
        while(len(c)>r):
            c.pop(-1)
        return c     
                 


    def partition1(self,array, start, end, compare_func):
        pivot = array[start]
        low = start + 1
        high = end

        while True:
            while low <= high and compare_func(array[high], pivot):
             high = high - 1

            while low <= high and not compare_func(array[low], pivot):
                low = low + 1

            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break

        array[start], array[high] = array[high], array[start]

        return high

    def partition(self,lista,l,r,key,reversed):
        pivot=key(lista[l])
        i=l
        j=r
        while i<j:
            if not reversed:
                while i<=r and key(lista[i])<=pivot:
                    i=i+1
                while j>=0 and  key(lista[j])>=pivot:
                    j=j-1
            else :
                while i<=r and key(lista[i])>=pivot:
                    i=i+1
                while j>=0 and key(lista[j])<=pivot:
                    j=j-1
            if i<j:
                lista[i],lista[j]=lista[j],lista[i]
        lista[l],lista[j]=lista[j],lista[l]
        return j





    def quickSortRec(self,list,l,r,key,reversed=False):

        if l<r:
            j=self.partition(list,l,r,key,reversed)
            self.quickSortRec(list,l,j-1,key,reversed)
            self.quickSortRec(list,j+1,r,key,reversed)
        return list           

    def quick_sort(self,array, start, end, compare_func):
        if start >= end:
            return

        p = self.partition1(array, start, end, compare_func)
        self.quick_sort(array, start, p-1, compare_func)
        self.quick_sort(array, p+1, end, compare_func)


    def gnomsortclient(self,arr,n,compare_fun):
        index = 0
        while index < n:
            if index == 0:
                index = index + 1
            if compare_fun(arr[index], arr[index - 1]):
                index = index + 1
            else:
                arr[index], arr[index-1] = arr[index-1], arr[index]
                index = index - 1
        return arr
                   
        
  
