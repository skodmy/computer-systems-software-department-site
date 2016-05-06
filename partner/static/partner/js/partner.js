/**
 * Created by dmitro on 28.03.16.
 */
function ajax_partner_carousel_items_list_append(selector, init_partner_carousel){
    $.ajax('partner/carousel-items-list/', {
        success: function(carousel_inner_html){
            $(selector).append(carousel_inner_html);
         	init_partner_carousel();
        }
    })
}