/**
 * Created by dmitro on 28.03.16.
 */
function ajax_divs_list_after(selector){
    $.ajax('fact/divs-list/',{
        success: function(divs_list_html){
            $(selector).after(divs_list_html)
        }
    })
}