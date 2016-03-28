/**
 * Created by dmitro on 28.03.16.
 */
function ajax_technology_divs_list_after(selector){
    $.ajax('technology/divs-list/',{
        success: function(divs_list_html){
            $(selector).after(divs_list_html)
        }
    })
}