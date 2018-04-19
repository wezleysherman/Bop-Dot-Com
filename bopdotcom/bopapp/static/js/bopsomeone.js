/* CSFR Code utilized from:
 * https://stackoverflow.com/questions/19333098/403-forbidden-error-when-making-an-ajax-post-request-in-django-framework
 * Credit: Fivef
 * We do not claim ownership of the following code.
 *
 * CSFR Token is used for ajax calls (Communicating frontend with the backend).
 * This code utilizes jquery.cookie library to generate a CSRF token to allow POST access.
 * This code is very generic and is utilized in any Django web app that utilizes ajax calls.
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

var friendID;
$('.friend').click(function() {
	$('#message').css('visibility', 'visible');
	friendID = $(this).data('friend');
});

$('#bop-btn').click(function() {
	var message = $('#bopmessage').val();
	$.ajax({
		url: '/ajax/bop_someone/',
		type: 'POST',
		data: {
			'friend': friendID,
			'msg' : message
		},
		success: function(resp) {
			window.location.assign('');
		}
	});
});