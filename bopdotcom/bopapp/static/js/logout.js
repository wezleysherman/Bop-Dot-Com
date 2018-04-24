/* JQuery Ajax calls referenced from:
 * http://api.jquery.com/jquery.ajax/
 *
 * https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
 */
$('#logout').click(function() {
	console.log("logging user out");
	$.ajax({
		url: '/ajax/logout/',
		type: 'POST',
		success: function(r) {
			window.location.assign('http://127.0.0.1:8000');
		}
	});
});