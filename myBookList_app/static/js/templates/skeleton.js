
$(document).ready(function () {
    // On attache les fonctions pour l'animation de la barre de recherche
    $('#searchBar').focusin(onFocusInSearch);
    $('#searchBar').focusout(onFocusOutSearch);
    $('#searchBar').on('input',onInput);
});

function onFocusInSearch()
{
    $('#searchBar').animate({width:'300px'}, "medium");
}

function onFocusOutSearch()
{
    $('#searchBar').animate({width:'180px'}, "medium");
}

function onInput(e) {
    // On permet de submit seulement si l'input n'est pas vide

    if(e.target.value == '')
    {
        document.getElementById('submitButton').disabled = true
    }
    else if(e.target.value != '')
    {
        document.getElementById('submitButton').disabled = false
    }
}
