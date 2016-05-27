(function($){
    $(function(){
		$.get('/slides/', function(slides_html){$('.slides').append(slides_html); $('.slider').slider()});
		$.get('/fact/rows/', function(facts_html){$('.interesting-facts').append(facts_html); create_charts()});
		$('#technologies-carousel').load('/technology/carousel-items-list/', function(){$(this).carousel({dist: 0, padding : 10})});
		$('#advertisements-row').load('/advertisement/cards-list/');
		$('#partners-carousel').load('/partner/carousel-items-list/', function(){$(this).carousel({dist: 0, padding : 10})});

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

function create_charts(){
	Chart.defaults.global.legend.display = false;
	$.getJSON('/fact/facts-arguments-json/', function(json_data){
		$.each(json_data, function(key, value){
			new Chart($('#fact-chart-area-'+key.toString())[0].getContext('2d'),
				{
					type: 'doughnut',
					data: {
						labels: value['labels'],
						datasets:[{
							data: value['data'],
							backgroundColor: Please.make_color({
								base_color: 'lightblue',
								colors_returned: value['data'].length,
								format: 'hex'
							})
						}]
					},
					options: {responsive: true}
				}
			)
		})
	});
}