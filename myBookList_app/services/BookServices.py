# https://docs.djangoproject.com/fr/2.0/topics/http/file-uploads/

from uuid import uuid4




def handle_image_upload(file):
    """
    Voir si besoin, donc pour plus tard
    :param file:
    :return:
    """
    pass


def generate_path_for_save(instance, filename):
    """
    instance et filename sont deux paramètres obligatoire reçu par l'appelant
    :param instance:
    :param filename:
    :return:
    """

    if instance.pk:
        new_filename = '{}-{}'.format(instance.pk, filename)
    else:
        # uuid4 génère un nombre aléatoire
        new_filename = '{}-{}'.format(uuid4().hex, filename)

    return new_filename


def build_post(request):
    """
    On set le post notament en remplacant le nom de l'author par son id
    :param request:
    :return:
    """
    # Import local sinon circular import dependency entre models et ce fichier
    from myBookList_app.models import Author

    # On copy l'objet
    post = request.POST.copy()

    # On prend l'author
    dataAuthor = post['author']

    # On le recherche dans la bd
    author = Author.objects.get(name=dataAuthor.split(' ')[0], forename=dataAuthor.split(' ')[1])

    # Et on remplace son nom par l'id pour que le save du form créé avec les request.POST ne lève pas d'erreur
    post['author'] = author.id

    return post

