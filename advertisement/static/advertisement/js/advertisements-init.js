(function($){
  $(function(){
  	$('.nav-dropdown-button').dropdown({hover: true});
  	$('.mobile-dropdown-button').dropdown({hover: false});
  	$('#user-menu-btn').dropdown({belowOrigin: true, constrain_width : false, hover: false});
  	$('#mobile-user-menu-btn').dropdown({belowOrigin: true, constrain_width : false, hover: false});
    $('#mobile-nav-btn').sideNav();
    $('#mobile-login-btn').sideNav();
	Materialize.updateTextFields();

	$('.modal-trigger').leanModal();

	$(window).scroll(function(){
		// Up button show and hide
		if ($(this).scrollTop() > 200) {
			$('#up_button').fadeIn();
		} else {
			$('#up_button').fadeOut();
		}	
	});

	//Click event to scroll to top
	$('#up_button').click(function(){
		$('html, body').animate({scrollTop : 0},800);
		return false;
	});
  }); // end of document ready
})(jQuery); // end of jQuery name space