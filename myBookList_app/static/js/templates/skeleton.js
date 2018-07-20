
$(document).ready(function () {
    // On attache les fonctions pour l'animation de la barre de recherche
    $('#searchBar').focusin(onFocusInSearch);
    $('#searchBar').focusout(onFocusOutSearch);

});

function onFocusInSearch()
{
    $('#searchBar').animate({width:'300px'},"medium");
}

function onFocusOutSearch()
{
    $('#searchBar').animate({width:'180px'},"medium");
}
