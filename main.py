
from domain.validare import FilmValidator,ClientValidator, Inchireirevalidator
from repository.gestionare import InMemoryRepositoryClienti,InMemoryRepositoryFilme
from repository.inchiriere import InchireireRepoMemory,RentItemRepoFile
from repository.magazin_service_file import ClientRepoFile,FilmRepoFile

from service.inchireie_service import RentItemService
from service.magazin_service import MoviesService,ClientsService
from ui.consola import Consola

val1=FilmValidator()
val2=ClientValidator()
val3=Inchireirevalidator()
repo1=InMemoryRepositoryFilme()
repo2=InMemoryRepositoryClienti()
repo3=InchireireRepoMemory()

repo_file_film=FilmRepoFile("data/filme.txt")
repo_file_client=ClientRepoFile("data/clienti.txt")

inchiriere_repo_file=RentItemRepoFile("data/inchirieri.txt")



srv1=MoviesService(repo_file_film,val1)
srv2=ClientsService(repo_file_client,val2)
srv_rent_item=RentItemService(inchiriere_repo_file,val3,repo_file_film,repo_file_client)
ui=Consola(srv1,srv2,srv_rent_item)
ui.show_ui()