var friendID;
$('.friend').click(function() {
	$('#message').css('visibility', 'visible');
	friendID = $(this).data('friend');
});

/* JQuery Ajax calls referenced from:
 * http://api.jquery.com/jquery.ajax/
 *
 * https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
 */
$('#bop-btn').click(function() {
	var message = $('#bopmessage').val();
	$.ajax({
		url: '/ajax/bop_someone/',
		type: 'POST',
		data: {
			'friend': friendID,
			'msg' : message
		},
		success: function(r) {
			window.location.assign('');
		}
	});
});