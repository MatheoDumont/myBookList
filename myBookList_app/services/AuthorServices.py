from django.db.models import QuerySet

from myBookList_app.models import Author


def search_author(stringname):
    """
    Cherche dans la table Author l'auteur donné dans stringname et retourne le résultat formatté avec 'format_result'
    :param stringname:
    :return: QuerySet
    """

    # Il serait intéressant de généraliser cet algorithme pour pouvoir l'utiliser ailleur si besoin

    # Vérifier si il y a plus de 1 mot si oui, faire la recherche en comptant le premier mot
    # comme le prénom puis le second comme le nom et faire la recherche adaptée

    # Comme mécanisme pour être sûr d'être le plus éxhaustif, faire la recherche ci-dessus et croiser les
    # résultats obtenus ci-dessus pour maximiser les chances de trouver l'auteur rechercher

    # Si un seul mot recherche les auteur par ce mot pour le nom et le forename puis croiser les résultats
    stringnameSplited = stringname.split(' ')
    author_by_name = None
    author_by_forename = None

    if len(stringnameSplited) == 1:
        # Un mot dans la recherche
        name = stringnameSplited[0]

        author_by_name = Author.objects.filter(name__contains=name)
        author_by_forename = Author.objects.filter(forename__contains=name)

    elif len(stringnameSplited) == 2:
        # Deux mot donc normalement sous le format 'prénom nom'
        name = stringnameSplited[0]
        forename = stringnameSplited[1]

        author_by_name = Author.objects.filter(name__contains=name)
        author_by_forename = Author.objects.filter(forename__contains=forename)

    else:
        # Trois mots et plus

        name = stringnameSplited[0]
        forename = ''

        stringnameSplited.pop(0)

        for string in stringnameSplited:
            forename = forename + ' ' + string

        author_by_name = Author.objects.filter(name__contains=name)
        author_by_forename = Author.objects.filter(forename__contains=forename)

    # On regarde si les resultats sont vides et on sauvegarde les résultats pour faciliter la suite
    abn_is_empty = True if len(author_by_name) == 0 else False
    abf_is_empty = True if len(author_by_forename) == 0 else False

    if not abn_is_empty and not abf_is_empty:
        intersection = author_by_name.intersection(author_by_forename)
    elif not abn_is_empty and abf_is_empty:
        intersection = author_by_name
    elif abn_is_empty and not abf_is_empty:
        intersection = author_by_forename
    else:
        intersection = Author.objects.none()

    return format_result(intersection)


def format_result(queryset):
    """
    Return une liste d'author avec la forme:
    authorslist : [
        1: {
            'id': ...
            'name': ...
            'forename': ...
        }
        2: ...
    ]
    :param queryset:
    :return:
    """
    # Si le résultat est vide, on retourne une liste pour pouvoir le JSON serialize
    if not queryset.exists():
        return []

    # On garde seulement les valeurs 'id', 'name' et 'forename'
    try:
        authors_st = queryset.values('id', 'name', 'forename')
    except AttributeError:
        return []

    # On transforme le QuerySet en liste
    authorslist = list(authors_st)

    return authorslist
