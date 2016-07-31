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

	  //initializing pagination
	  $('.disabled.edge + li').addClass('active');
	  
	  $('li.waves-effect > a').click(function (e) {
		  e.preventDefault();
		  $.get('page_number' + $(this).text() + '/', function (data) {
				  $('li.waves-effect.active').removeClass('active');
			  	  $('.news-record').remove();
			  	  $('#news-start').after(data);
			  }
		  )
	  });

	  $('li.edge > a').click(function (e) {
		  e.preventDefault();
		  var active_page_number = $('li.active > a').text();
		  active_page_number = parseInt(active_page_number);
		  ($(this).text()=='chevron_right')? active_page_number++: active_page_number--;
		  active_page_number = active_page_number.toString();
		  $('li.waves-effect > a[href="'+active_page_number+'"]').click();
	  });
	  //end of pagination's initialization
  }); // end of document ready
})(jQuery); // end of jQuery name space