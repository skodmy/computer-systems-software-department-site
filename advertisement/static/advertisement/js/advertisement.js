/**
 * Created by dmitro on 28.03.16.
 */
function ajax_cards_list_after(selector){
    $.ajax('advertisement/actual-cards-list/', {
        success: function(actual_cards_list){
            $(selector).after(actual_cards_list)
        }
    })
}