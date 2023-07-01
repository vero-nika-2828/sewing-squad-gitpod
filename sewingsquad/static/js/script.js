$(document).ready(function () {
    $('.sidenav').sidenav({edge:"right"});
    $('.password-req').tooltip();
    $('select').formSelect();
    $('.modal').modal();
    $('.collapsible').collapsible();

    
});

$('.primary-image').on("mouseenter", function(){ 
    $(this).hide();
    $(this).siblings('.secondary-image').show();
}).on("mouseleave", function(){
    var current_image = this

    setTimeout(function(){
        $(current_image).show();
        $(current_image).siblings('.secondary-image').hide();
    },100);
});


//Display the current year in footer's copyright
$('#year').html(new Date().getFullYear());