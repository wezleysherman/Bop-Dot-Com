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