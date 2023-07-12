$(document).ready(function () {
    //Side nav opens on right
    $('.sidenav').sidenav({edge:"right"});
    //Show tooltip with password specification  when hovered over
    $('.password-req').tooltip();
    //Form dropdown
    $('select').formSelect();
    //Delete modal
    $('.modal').modal();
    $('.collapsible').collapsible();  
    //Display and swap pictures
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
});

    
});

//Swap picture when mouse is on card image
$('.primary-image').on("mouseenter", function(){ 
    $(this).hide();
    $(this).siblings('.secondary-image').show();
});

//Return to primary picture when mouse leaves card image
$('.secondary-image').on("mouseleave", function(){
    var current_image = this;
        $(current_image).hide();
        $(current_image).siblings('.primary-image').show();

});

// Move to next picture
$('.next').on("click", function(){
    $('.carousel.carousel-slider').carousel("next");
});

// Move to previous picture picture
$('.prev').on("click", function(){
    $('.carousel.carousel-slider').carousel("prev");
});

//Display the current year in footer's copyright
$('#year').html(new Date().getFullYear());