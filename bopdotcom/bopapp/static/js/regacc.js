var friendID;
$('#register_btn').click(function() {
	$('#message').css('visibility', 'visible');
	friendID = $(this).data('friend');
});