# https://docs.djangoproject.com/fr/2.0/topics/http/file-uploads/
from myBookList.settings import FRONT_PAGE_BOOK_COVER
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

    return FRONT_PAGE_BOOK_COVER + new_filename
