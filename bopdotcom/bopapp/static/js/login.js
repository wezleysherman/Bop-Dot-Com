/* JQuery Ajax calls referenced from:
 * http://api.jquery.com/jquery.ajax/
 *
 * https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
 */
$("#login-btn").click(function() {
	var username = $('#username').val();
	var password = $('#password').val();
	$.ajax({
		url: '/ajax/login_ajax/',
		type: 'POST',
		data: {
			'username': username,
			'password' : password,
		},
		success: function(r) {
			if(r['return'] == 'err') {
				$('#username').css('background-color', 'red');
				$('#password').css('background-color', 'red');
			} else {
				window.location.assign('http://127.0.0.1:8000');
			}
		}
	});
});