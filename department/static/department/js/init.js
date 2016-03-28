(function($){
    $(function(){
        ajax_cards_list_after('#advertisments-start');
        ajax_divs_list_after('#facts-start');
        ajax_news_cards_list_after('#news-start');
        ajax_partner_carousel_items_list_append('#carousel-items-list-container');
        ajax_technology_divs_list_after('#technologies-start');
        $('.dropdown-button').dropdown();
        $('.button-collapse').sideNav();
        $('.slider').slider({indicators:false});
        $('.carousel').carousel({dist: 0});
    }); // end of document ready
})(jQuery); // end of jQuery name space