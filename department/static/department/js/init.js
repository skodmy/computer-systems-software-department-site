(function($){
    $(function(){
		$.get('slides/', function(slides_html){$('.slides').append(slides_html); $('.slider').slider()});
		// TODO place facts loading code here
		$('#technologies-carousel').load('technology/carousel-items-list/', function(){$(this).carousel({dist: 0})});
		$('#advertisements-row').load('advertisement/cards-list/');
		$('#news-row').load('news/cards-list/');
		$('#partners-carousel').load('partner/carousel-items-list/', function(){$(this).carousel({dist: 0})});

		$('.nav-dropdown-button').dropdown({hover: true});
	  	$('.mobile-dropdown-button').dropdown({hover: false});
		$('#mobile-login-btn').sideNav();
	    $('#mobile-nav-btn').sideNav();
		$('#user-menu-btn').dropdown({belowOrigin: true, constrain_width : false, hover: false});
	  	$('#mobile-user-menu-btn').dropdown({belowOrigin: true, constrain_width : false, hover: false});
		$('#up_button').click(function(){$('html, body').animate({scrollTop:0},800);/*return false*/});
		$('#logout-btn').click(function(){$.get('logout/', function(){location.reload()});});
		$('.modal-trigger').leanModal();
		$('.error-alert').hide();

		$(window).scroll(function(){var up_btn=$('#up_button'); $(this).scrollTop()>100?up_btn.fadeIn():up_btn.fadeOut()});
	    window.setInterval(function(){$('.carousel').carousel('next')}, 3000);

		$('#login_modal_form').submit(login_form_submit_handler);
		$('#login_mobile_form').submit(login_form_submit_handler);

		var ctx1 = $("#fact-chart-area1")[0].getContext('2d');
		var data1 = {
		    labels: [
		        "Arg1",
		        "Arg2",
		        "Arg3"
		    ],
		    datasets: [
		        {
		            data: [30, 50, 20],
		            backgroundColor: [
		                "#057dc8",
		                "#d9e7ef",
		                "#063c5e"
		            ],
		            hoverBackgroundColor: [
		                "#057dc8",
		                "#d9e7ef",
		                "#063c5e"
		            ]
		        }
		    ]
		};
		Chart.defaults.global.legend.display = false;
		var fact1 = new Chart(ctx1, {
		    type: 'doughnut',
		    data: data1,
		    options: {
	            responsive: true
	        }
		});

		var ctx2 = $("#fact-chart-area2")[0].getContext('2d');
		var data2 = {
		    labels: [
		        "Arg1",
		        "Arg2",
		        "Arg3"
		    ],
		    datasets: [
		        {
		            data: [30, 50, 20],
		            backgroundColor: [
		                "#057dc8",
		                "#d9e7ef",
		                "#063c5e"
		            ],
		            hoverBackgroundColor: [
		                "#057dc8",
		                "#d9e7ef",
		                "#063c5e"
		            ]
		        }
		    ]
		};
		var fact2 = new Chart(ctx2, {
		    type: 'doughnut',
		    data: data2,
		    options: {
	            responsive: true
	        }
		});
    }); // end of document ready
})(jQuery); // end of jQuery name space

function login_form_submit_handler(event){
	var form_alert = $(this).attr('id')=='login_modal_form'?$('#login_modal_error_alert'):$('#login_mobile_error_alert');
	alert($(this).serialize());
	$.post('login/', $(this).serialize(),
		function(json_response_data){
			var show_form_alert = function(message){form_alert.text(message); form_alert.show()};
			if(json_response_data['exists']){
				json_response_data['is_active']?location.reload():show_form_alert('Your account is disabled!');
			}else{show_form_alert('Wrong username or password!')}
		}
	);
	event.preventDefault()
}