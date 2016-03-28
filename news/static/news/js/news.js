/**
 * Created by dmitro on 28.03.16.
 */
function ajax_news_cards_list_after(selector) {
    $.ajax('news/cards-list/', {
        success: function (cards_list_html) {
            $(selector).after(cards_list_html)
        }
    });
}