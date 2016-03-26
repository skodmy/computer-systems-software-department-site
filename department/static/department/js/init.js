(function($){
  $(function(){
  	$('.dropdown-button').dropdown();
    $('.button-collapse').sideNav();
    $('.slider').slider({indicators:false});

    // TODO
    $.ajax('/partner/partners-carousel', {
      method: 'GET',
      success: function(carousel_items){
        $('.carousel').html(carousel_items)
      }
    });

    $('.carousel').carousel({dist: 0});
  }); // end of document ready
})(jQuery); // end of jQuery name space