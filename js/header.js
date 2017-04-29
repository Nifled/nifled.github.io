new WOW().init();

$(window).on('load', function() { // makes sure the whole site is loaded
    $('#status').fadeOut(); // will first fade out the loading animation
    $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
    $('body').delay(350).css({'overflow':'visible'});

    //Banner elements
    $('.animate-e').addClass("animated rollIn");
    $('.animate-r').addClass("animated rollIn");
    $('.animate-i').addClass("animated rollIn");
    $('.animate-c').addClass("animated rollIn");
    $('.animate-k').addClass("animated rollIn");
    $('.animate-k').addClass("animated rollIn");
    $('.animate-ee').addClass("animated rollIn");
    $('.animate-rr').addClass("animated rollIn");
    $('.animate-ii').addClass("animated rollIn");
    $('.animate-cc').addClass("animated rollIn");
    $('.animate-kk').addClass("animated rollIn");
    $('.animate-k').addClass("animated rollIn");
    $('.animate-sub').addClass("animated fadeInUp");
    $('.animate-btn').addClass("animated flipInX");
});

$(document).ready(function(){

    // scrollspy
    $("body").scrollspy({
        target: "#myNavbar",
        offset: 80
    });

    // Add smooth scrolling to all links
    $(".scrollAnchor").on('click', function(event) {
        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
            // Prevent default anchor click behavior
            event.preventDefault();
            // Store hash
            var hash = this.hash;
            // For mobile
            if($(window).innerWidth() <= 765) {
                $('input[type=checkbox]').trigger('click');
            }
            // Using jQuery's animate() method to add smooth page scroll
            // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800);
        } // End if
    });

    // For home button and hire-me btn
    $(".scrollAnchor2").on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800);
        } // End if
    });
});
