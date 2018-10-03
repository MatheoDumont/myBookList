from myBookList_app.models import Book


def search(string):
    """
    Algo pour champ de recherche à l'index

    :param string: Peut être le nom d'un livre, d'un auteur
        retourne le livre s'il est trouvé,
            retourne des livres du même genre
            retourne des livres du même auteur
            retourne des auteurs de ce genre
    :return:
    """
    return Book.objects.filter(name__contains=string)
