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
		success: function(resp) {
			window.location.assign('');
		}
	});
});