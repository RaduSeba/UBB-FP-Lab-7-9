class FilmMagazinExceptie(Exception):
    pass

class ValidationException(FilmMagazinExceptie):
    def __init__(self,msgs):
        """
        :param msg:lista de mesaje de eroare
        :type msg:msgs
        """
        self.__err_msgs=msgs

    def getmessage(self):
        return self.__err_msgs

    def __str__(self) :
        return "Validation exception :"+str(self.__err_msgs)

class RepositoryException(FilmMagazinExceptie):
    def __init__(self,msg):
        self.__msg=msg

    def getMessage(self):  
        return self.__msg
 
    def  __str__(self) -> str:
        return "Repository exception :"+str(self.__msg) 


class DuplicateIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"ID duplicat")

class FilmAlreadyAssingedException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Filmul a fost deja inchiriat")

class FilmnotfoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Filmul nu a fost gasit")

class ClientnotfoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"clientul nu exista")



