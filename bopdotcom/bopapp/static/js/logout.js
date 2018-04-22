
$('#logout').click(function() {
	console.log("logging user out");
	$.ajax({
		url: '/ajax/logout/',
		type: 'POST',
		success: function(resp) {
			window.location.assign('');
		}
	});
});