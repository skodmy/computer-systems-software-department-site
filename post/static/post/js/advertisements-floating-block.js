(function($){
  $(function(){
  	var currentBlock;
  	if (!$('#raiting_large_floating').is(":visible") && !$('#raiting_med_floating').is(":visible")) {
  		currentBlock = -1;
  	} else {
  		if ($('#raiting_large_floating').is(":visible")) {
  			currentBlock = $('#raiting_large_floating');
  		} else {
  			currentBlock = $('#raiting_med_floating');
  		}
  	}

  	if (currentBlock != -1) {
  		var footerHeight = $('.page-footer').height();
		var advertismentsWidth = currentBlock.width();
		var currentTopValue = currentBlock.position().top;
  		$(window).scroll(function(){
			//Block floating script
			if ($(this).scrollTop() > currentTopValue) {
				startBlockFloating(advertismentsWidth, currentBlock);
			} else {
				stopBlockFloating(currentBlock);
			}
			//Stop floating script
			if ($(this).scrollTop() +  $(window).height() + footerHeight > $(document).height()) {
				currentBlock.fadeOut();
			} else {
				if (!currentBlock.is(":visible")) {
					currentBlock.fadeIn();
				}
			}

		
		});
  	}
  	
  }); // end of document ready
})(jQuery); // end of jQuery name space

function startBlockFloating(width, currentBlock) {
	
	currentBlock.addClass('float-block');
	currentBlock.width(width);
}

function stopBlockFloating(currentBlock) {
	currentBlock.removeClass('float-block');
}