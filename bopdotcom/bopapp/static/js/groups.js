$("#joingroup").click(function() {
	$('#addgroup').css('visibility', 'visible');
});

/* JQuery Ajax calls referenced from:
 * http://api.jquery.com/jquery.ajax/
 *
 * https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
 */
$("#ngroup").click(function() {
	$.ajax({
		url: '/ajax/join_group/',
		type: 'POST',
		data: {
			'id': $(this).data("id")
		},
		success: function(r) {
			window.location.assign('');
		}
	});
});

$(".exit").click(function() {
	$('#addgroup').css('visibility', 'hidden');
})