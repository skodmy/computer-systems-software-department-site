(function($){
    $(function(){
		$('.slider').slider();
		$('#technologies-carousel').carousel({dist: 0, padding:10});
		$('#partners-carousel').carousel({dist:0, padding: 10});
	  	$('.mobile-dropdown-button').dropdown({alignment: 'right', belowOrigin: true});
		$('#mobile-login-btn').sideNav();
	    $('#mobile-nav-btn').sideNav();
		$('#user-menu-btn').dropdown({belowOrigin: true, constrain_width : false, hover: false});
	  	$('#mobile-user-menu-btn').dropdown({belowOrigin: true, constrain_width : false, hover: false});
		$('#up_button').click(function(){$('html, body').animate({scrollTop:0},800)});
		$('#logout-btn').click(function(){$.get('/logout/', function(){location.reload()})});
		$('.modal-trigger').leanModal();
		$('.error-alert').hide();

		$(window).scroll(function(){var up_btn=$('#up_button'); $(this).scrollTop()>100?up_btn.fadeIn():up_btn.fadeOut()});
	    window.setInterval(function(){$('.carousel').carousel('next')}, 3000);

		$('#login_modal_form').submit(login_form_submit_handler);
		$('#login_mobile_form').submit(login_form_submit_handler);
    }); // end of document ready
})(jQuery); // end of jQuery name space


function login_form_submit_handler(event){
	var form_alert = $(this).attr('id')=='login_modal_form'?$('#login_modal_error_alert'):$('#login_mobile_error_alert');
	$.post('/login/', $(this).serialize(),
		function(json_response_data){
			var show_form_alert = function(message){form_alert.text(message); form_alert.show()};
			if(json_response_data['exists']){
				json_response_data['is_active']?location.reload():show_form_alert('Your account is disabled!');
			}else{show_form_alert('Wrong username or password!')}
		}
	);
	event.preventDefault()
}