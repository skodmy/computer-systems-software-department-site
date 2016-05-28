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
	$("#map_frame").html("<iframe src='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1327.2458731933987!2d25.92969268342978!3d48.29339312788115!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0000000000000000%3A0x974c4f797f290a9b!2z0KTQsNC60YPQu9GM0YLQtdGCINC80LDRgtC10LzQsNGC0LjQutC4INGC0LAg0ZbQvdGE0L7RgNC80LDRgtC40LrQuA!5e0!3m2!1suk!2sua!4v1464466479235' width='" + width + "' height='" + width + "' frameborder='0' style='border:0' allowfullscreen></iframe>")
}