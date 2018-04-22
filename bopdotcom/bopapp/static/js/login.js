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
		success: function(resp) {
			if(resp['return'] == 'err') {
				$('#username').css('background-color', 'red');
				$('#password').css('background-color', 'red');
			} else {
				window.location.assign('');
			}
		}
	});
});