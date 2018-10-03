
$(document).ready(function () {
    // On attache les fonctions pour l'animation de la barre de recherche
    $('#id_search').focusin(onFocusInSearch);
    $('#id_search').focusout(onFocusOutSearch);
    $('#id_search').on('input',onInput);
});

function onFocusInSearch()
{
    $('#id_search').animate({width:'300px'}, "medium");
}

function onFocusOutSearch()
{
    $('#id_search').animate({width:'180px'}, "medium");
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
