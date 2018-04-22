$("#joingroup").click(function() {
	$('#addgroup').css('visibility', 'visible');
});

$("#ngroup").click(function() {
	$.ajax({
		url: '/ajax/join_group/',
		type: 'POST',
		data: {
			'id': $(this).data("id")
		},
		success: function(resp) {
			window.location.assign('');
		}
	});
});

$(".exit").click(function() {
	$('#addgroup').css('visibility', 'hidden');
})