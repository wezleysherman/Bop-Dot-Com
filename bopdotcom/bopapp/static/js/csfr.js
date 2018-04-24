/* CSFR Code utilized from:
 *
 * https://stackoverflow.com/questions/19333098/403-forbidden-error-when-making-an-ajax-post-request-in-django-framework
 *
 * CREDIT: Fivef
 *
 * We DO NOT claim ownership of the following code.
 * Fivef wrote this code -- not us.
 * 
 *
 * CSFR Token is used for ajax calls (Communicating frontend with the backend).
 * This code utilizes jquery.cookie library to generate a CSRF token to allow POST access.
 * This code is very generic and is utilized in any Django web app that utilizes ajax calls.
 *
 * All credit goes to Fivef for the following snippet:
 */
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
////////////////////////////////////////////
