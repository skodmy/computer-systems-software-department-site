(function($){
    $(function(){
        ajax_cards_list_after('#advertisments-row');
        //ajax_divs_list_after('#facts-start');
        ajax_news_cards_list_append('#news-row');
        ajax_partner_carousel_items_list_append('#partners-carousel', init_partner_carousel);
        //ajax_technology_divs_list_after('#technologies-start');
        $('.dropdown-button').dropdown();
	    $('.button-collapse').sideNav();
	    $('.slider').slider();

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
		$('.modal-trigger').leanModal();

		//Delete this line after connect technologies models from DB
		init_technologies_carousel();


		init_up_button();
		
    }); // end of document ready
})(jQuery); // end of jQuery name space

function init_partner_carousel() {
	$('#partners-carousel').carousel({dist: 0});
}

function init_technologies_carousel() {
	$('#technologies-carousel').carousel({dist: 0});
}

function init_up_button() {
	//Check to see if the window is top if not then display button
	$(window).scroll(function(){
		if ($(this).scrollTop() > 100) {
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
}