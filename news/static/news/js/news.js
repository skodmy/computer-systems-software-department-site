/**
 * Created by dmitro on 28.03.16.
 */
function ajax_news_cards_list_append(selector) {
    $.ajax('news/cards-list/', {
        success: function (cards_list_html) {
            $(selector).append(cards_list_html)
        }
    });
}