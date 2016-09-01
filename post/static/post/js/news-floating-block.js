(function($){
  $(function(){
  	var currentBlock;
  	if (!$('#advertisments_block').is(":visible") && !$('#advertisments_medium_block').is(":visible")) {
  		currentBlock = -1;
  	} else {
  		if ($('#advertisments_block').is(":visible")) {
  			currentBlock = $('#advertisments_block');
  		} else {
  			currentBlock = $('#advertisments_medium_block');
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