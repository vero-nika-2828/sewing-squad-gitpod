$(document).ready(function () {
    $('.sidenav').sidenav({edge:"right"});
    $('.password-req').tooltip();
    $('select').formSelect();
    $('.modal').modal();
    $('.collapsible').collapsible();
});


$('#year').html(new Date().getFullYear());