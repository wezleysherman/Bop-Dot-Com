/* JQuery Ajax calls referenced from:
 * http://api.jquery.com/jquery.ajax/
 *
 * https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
 */
$('#register-btn').click(function() {
	var username = $('#username').val();
	var password = $('#password').val();
	var email = $('#email').val();
	$.ajax({
		url: '/ajax/register_ajax/',
		type: 'POST',
		data: {
			'username': username,
			'password' : password,
			'email' : email
		},
		success: function(r) {
			window.location.assign('http://127.0.0.1:8000');
		}
	});
});