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

	initGoogleMap();
  }); // end of document ready
})(jQuery); // end of jQuery name space

function initGoogleMap() {
	var width = $("#map_frame").width();
	$("#map_frame").html("<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2655.817709295214!2d25.911583415653585!3d48.267882479234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47340f527f1c6c67%3A0x36d194a60811cabb!2zOCDQutC-0YDQv9GD0YEg0KfQndCj!5e0!3m2!1suk!2sua!4v1472918942384' width='" + width + "' height='" + width + "' frameborder='0' style='border:0' allowfullscreen></iframe>")
}