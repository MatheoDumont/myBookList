
$(document).ready(function () {
    // On attache les fonctions pour l'animation de la barre de recherche
    $('#searchBar').focusin(onFocusInSearch);
    $('#searchBar').focusout(onFocusOutSearch);

    // On attache la fonction pour la modal d'inscription ou connexion
    $("#signOrLoginBtn").click(function () {
            $('#signOrLoginModal').modal('show');
    });
});

function onFocusInSearch()
{
    $('#searchBar').animate({width:'300px'},"medium");
}

function onFocusOutSearch()
{
    $('#searchBar').animate({width:'180px'},"medium");
}
