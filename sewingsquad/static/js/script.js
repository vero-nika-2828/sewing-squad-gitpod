$(document).ready(function () {
    $('.sidenav').sidenav({edge:"right"});
    $('.password-req').tooltip();
    $('select').formSelect();
    $('.modal').modal();
    $('.collapsible').collapsible();  
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
});

    
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


$('.next').on("click", function(){
    $('.carousel.carousel-slider').carousel("next")
})

$('.prev').on("click", function(){
    $('.carousel.carousel-slider').carousel("prev")
})

//Display the current year in footer's copyright
$('#year').html(new Date().getFullYear());