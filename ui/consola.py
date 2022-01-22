from domain.validare import Inchireirevalidator, ValidationException
from exceptions.exceptii import ClientnotfoundException, DuplicateIDException, FilmAlreadyAssingedException, FilmnotfoundException


class Consola:
    def __init__(self,srv1,srv2,srvRentItem):
        self.__srv1=srv1
        self.__srv2=srv2
        self.__srv_rent_item=srvRentItem

    def __show_all_movies(self,filme):
        #filme=self.__srv1.get_all_movies()
        if len(filme)==0:
            print("Nu exista filme in lista") 
        else : 
            print("Lista de filme este :")
            for film in filme:
                print("Denumire :",film.getname(),"ID:",film.getid(),"Descriere:",film.getdescriere(),"inchirieri:",film.getinchirieri())    

    def __show_all_clients(self,clienti):
        #clienti=self.__srv2.get_all_clients()
        if len(clienti)==0:
            print("Nu exista clienti in lista") 
        else : 
            print("Lista de clienti este :")
            for client in clienti:
                print("Denumire :",client.getname(),"ID:",client.getid(),"CNP:",client.getcnp(),"Inchirieri:",client.getinchirieri())     
    
    def __show_all_rent_items(self,rent_items):
        if len(rent_items)==0:
            print("Nu exista inchieri")
        else:
            print("Lista de inchireiri este :")
            for rent_item in rent_items:
                print("Clientul :"+str(rent_item.getClient().getname())+";"+"Filmul :"+str(rent_item.getFilm().getname()))    



    def __add_film(self):
        
        denumire=input("Denumirea filmului:")
        try :
            id=int(input("ID ul filmului :"))
        except ValueError :
            print("ID ul este invalid")
            return
        descreiere=input("Descrierea filmului:")
        inchirieri=0
        try:
            added_film = self.__srv1.add_film(id,denumire,descreiere,inchirieri)
            print('Filmul :', added_film , '\n a fost adaugat cu succes.')
        except ValidationException as  ve:
            print(str(ve))
        except DuplicateIDException:
            print("Exista deja un film cu id dat")    

    def __add_client(self):
        
        nume=input("Numele clientului:")
        try :
            id=int(input("ID ul clienetului :"))
            cnp=int(input("CNP ul clientului:"))
        except ValueError :
            print("ID/CNP ul este invalid")
            return
        inchiriere=0    
        try:
            added_client = self.__srv2.add_client(id,nume,cnp,inchiriere)
            print('Clientul', added_client , 'a fost adaugat cu succes.')
        except ValidationException as ve:
            print(str(ve))  
        except DuplicateIDException:
            print("Exista deja un client cu id dat")          

    def __delete_film(self):
        id=input("ID film:")

        try:
            deleted_film = self.__srv1.delete_by_id(id)
            print("Filmul",deleted_film,"a fost sters cu succes")
        except ValueError as ve:
            print(str(ve)) 

    def __delete_client(self):
        id=input("ID Client :")
        try :
            deleted_client=self.__srv2.delete_by_id(id)
            print("Clientul",deleted_client,"A fost sters cu succes")
        except ValueError as ve:
            print(str(ve))

    def __update_film(self):
        id=input("ID film:")
        denumire =input("Denumire film :")
        descriere=input("Descrierea filmului:")
        inchirieri=0
        try:
            updated_film=self.__srv1.update_film(id,denumire,descriere,inchirieri)
            print("Filmul",updated_film,"a fost modificat cu succes")
        except ValueError as ve :
            print(str(ve))

    def __update_client(self):
        id=input("ID client :")
        denumire=input("Nume client:")
        cnp=input("CNP client :")
        inchirieri=0
        try:
            updated_client=self.__srv2.update_client(id,denumire,cnp,inchirieri)
            print("Clientul",updated_client,"a fost modificat cu succes")
        except ValueError as ve:
            print(str(ve))

    def __cauta_film(self):
        string=input("Cautati dupa nume, descriere sau autor :")
        l=self.__srv1.filter_by_name(string)
        self.__show_all_movies(l)

    def __cauta_client(self):
        string=input("Cauta client dupa nume :")
        l=self.__srv2.filter_by_name(string)
        self.__show_all_clients(l)

    def __random1(self):
        times=input("Nr de clienti random:")
        l1=self.__srv2.generateclient(times)
        l1=self.__srv1.get_all_clients()
        self.__show_all_clients(l1)

    def __random2(self):
        times=input("Nr de filme random:")
        l1=self.__srv1.generatefilm(times)
        l1=self.__srv1.get_all_movies()
        self.__show_all_movies(l1)

    def __add_rent_item(self):
        """
        Adauga rent item 
        """    
        client_id=input("Id Client:")
        film_id=input("Id film:")
        try :
            rent_item=self.__srv_rent_item.add_rent_item(film_id,client_id)
            print("Inchiriere realizata cu succes.")
        except ValidationException as ve:
            print(str(ve))   
        except FilmnotfoundException as e:
            print(str(e))
        except ClientnotfoundException as ve:
            print(str(ve))
        except FilmAlreadyAssingedException as ve:  
            print(str(ve))          

    def __delete_rent_item(self):
        client_id=input("Id Client:")
        film_id=input("Id film:")
        try :
            rent_item=self.__srv_rent_item.delete_rent_item(film_id,client_id)
            print("film returnat")
        except ValidationException as ve:
            print(str(ve))   
        except FilmnotfoundException as e:
            print(str(e))
        except ClientnotfoundException as ve:
            print(str(ve))
        except FilmAlreadyAssingedException as ve:  
            print(str(ve))

    def __topfilme(self):
        l=self.__srv_rent_item.topfilme()
        self.__show_all_movies(l) 

    def __topclienti(self):
        c=self.__srv_rent_item.topclienti() 
        self.__show_all_clients(c) 

    def __fidelitate(self):
        c=self.__srv_rent_item.clientifideli()
        self.__show_all_clients(c)     


    def __quicksort(self):
        l=self.__srv2.get_all_clients()
        self.__srv_rent_item.quickSortRec(l, 0, len(l)-1 , lambda x: x.getinchirieri() ,reversed=False )
        self.__show_all_clients(l)   

    def __gnomclient(self):
        l=self.__srv2.get_all_clients()
        c=self.__srv_rent_item.gnomsortclient(l,len(l),lambda x, y: x.getinchirieri() >= y.getinchirieri())  
        self.__show_all_clients(c)



    def show_ui(self):
        while True:
            print('Comenzi disponibile: add,delete_by_id,show_all,cauta,update,random,exit,inchriere,all_inchirieri,top_filme,top_clienti,fidelitate,quick_client,gnom_client')
            cmd = input('Comanda este: ')
            cmd = cmd.lower().strip()
            if cmd == 'add':
                cmd1=input("Client sau Film :")
                
                if cmd1=="Client":
                    self.__add_client()
                elif cmd1=="Film":
                    self.__add_film()    
            elif cmd == 'show_all':
                cmd2=input("Client sau Film:")
                if cmd2=="Client":
                    self.__show_all_clients(self.__srv2.get_all_clients())
                elif cmd2=="Film":
                    self.__show_all_movies(self.__srv1.get_all_movies())   
            elif cmd=="delete_by_id":
                cmd3=input("Client sau Film :")
                if cmd3=="Client":
                    self.__delete_client()
                elif cmd3=="Film":
                    self.__delete_film()  
            elif cmd=="update":
                cmd4=input("Film sau Client:")  
                if cmd4=="Client":
                    self.__update_client()  
                if cmd4=="Film":
                    self.__update_film() 
            elif cmd=="cauta":
                cmd5=input("Film sau Client:")
                if cmd5=="Client":
                    self.__cauta_client()
                if cmd5=="Film":
                    self.__cauta_film()                              
            elif cmd == 'random':
                cmd6=input("Clienti sau Filme:")
                if cmd6=="Clienti":
                    self.__random1()
                elif cmd6=="Filme":  
                    self.__random2() 
            elif cmd=="exit":
                return 
            elif cmd=="inchiriere" :
                self.__add_rent_item()
            elif cmd=="returnare":
                self.__delete_rent_item()    
            elif cmd=="all_inchirieri":
                self.__show_all_rent_items(self.__srv_rent_item.get_all())
            elif cmd=="top_filme":
                self.__topfilme()   
            elif cmd=="top_clienti":
                self.__topclienti()    
            elif cmd=="fidelitate" :
                self.__fidelitate()  
            elif cmd=="quick_client":
                self.__quicksort() 
            elif cmd=="gnom_client":
                self.__gnomclient()                         
            else:
                print('Comanda invalida')
