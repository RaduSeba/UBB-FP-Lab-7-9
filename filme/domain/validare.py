from domain.entitati import film,client

class ValidationException(Exception) :
    pass

class FilmValidator:
    """

    clasa pentru incapsularea algoritmului de validare
    (validate putea fi metoda in clasa Film - choice of design)

    """
    def validate(self,film):
        errors=[]

        if film.getname()=='':
            errors.append("Denumirea filmului nu poate fi vida")
        if int(film.getid())<0 :
            errors.append("ID ul nu poate fi negativ")
        if film.getdescriere()=='':
            errors.append("Descrierea trebuie sa existe")
    

        if len(errors) > 0:
            #error_string = '\n'.join(errors)
            #raise ValueError(error_string)
            raise ValidationException(errors)    

class ClientValidator:

    def validate(self,client):
        errors=[]

        if client.getname()=='':
            errors.append("Numele clientului nu poate fi vid")

        try:
            int(client.getcnp())
            int(client.getid())
        except ValueError  as ve :
            errors.append("ID/CNP nu sunt numere")   



        if int(client.getid())<0 :
            errors.append("ID ul nu poate fi negativ")
        if int(client.getcnp())<=0:
            errors.append("CNP-ul este obligatoriu")
        if int(client.getcnp())>10000000000000 and int(client.getcnp())<100000000000000:
            errors.append("CNP-ul nu este corespunzator") 
        #if int(client.getcnp())<10000000000000:
           # errors.append("CNP-ul nu este corespunzator")        

        if len(errors) > 0:
            #error_string = '\n'.join(errors)
            #raise ValueError(error_string)
            raise ValidationException(errors)    

class Inchireirevalidator:
    pass



def test_validate_film():
    validator = FilmValidator()
    f = film(1234, "pulp fiction", "unul dintre cele mai bune filme","quentin tarantino")
    validator.validate(f)

    f1 = film(-1, "", "unul dintre cele mai bune filme","quentin tarantino")
    try:
        validator.validate(f1)
        assert False
    except ValidationException:
        assert True

    f2 = film(1234, "pulp fiction", "unul dintre cele mai bune filme","")

    try:
        validator.validate(f2)
        assert False
    except ValidationException:
        assert True

def test_validate_client():
    validator = ClientValidator()
    c= client(1234, "Radu Sebastian", 5020822890212)
    validator.validate(c)

    c1= client(1234, "Radu Sebastian",0)
    try:
        validator.validate(c1)
        assert False
    except ValidationException:
        assert True

    c2= client(1234, "", 5020822890212)

    try:
        validator.validate(c2)
        assert False
    except ValidationException:
        assert True




#test_validate_client()
#test_validate_film()

