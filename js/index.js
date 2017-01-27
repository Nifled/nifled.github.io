if ($(window).width() <= 768) {
  var videoElement = document.getElementById('wrapper');
  videoElement.pause();
  videoElement.src =""; // empty source
  videoElement.load();
} else {
  var videoElement = document.getElementById('wrapper');
  videoElement.pause();
  videoElement.src ="vids/header.mp4";
  videoElement.load();
}

  $('.booty').click(function() {
      $('input[type=checkbox]').trigger('click');
  });
  $('.hamburger').click(function() {
      $('input[type=checkbox]').trigger('click');
  });



  var $nav = $('.navbar');
  var $navHead = $('.navbar-default');
  var $logo = $('.navbar-brand img')
  $(window).scroll(function() {
      if ($(this).scrollTop() > $(window).height() - $logo.height()) {
          $nav.addClass('show');
          $navHead.addClass('show');
          $logo.addClass('smallLogo');
          $logo.addClass('animated');
          $logo.addClass('rubberBand');
          $logo.removeClass('hvr-wobble-to-bottom-right');
      } else {
          $nav.removeClass('show');
          $navHead.removeClass('show');
          $logo.removeClass('smallLogo');
          $logo.removeClass('animated');
          $logo.removeClass('rubberBand');
          $logo.addClass('hvr-wobble-to-bottom-right');
      }

      //aboutme-img
      var aboutImage = $(".aboutme-img").offset().top;
      var scrollY = $(window).scrollTop();
      if (scrollY + scrollY/1.1 > aboutImage) {
        $(".aboutme-img").addClass('colorize');
      }

  });on("resize", function() { // If the user resizes the window
      $(window).height() = $(this).height(); // the new height value
  });
