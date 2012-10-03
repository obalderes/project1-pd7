$(document).ready(function(){
    var hash = window.location.hash;
    $('header ul li a[href="'+hash+'"]').addClass('selected');
    $('body>div'+hash).addClass('selected');

    $('header ul li a').click(function(){
	var hash = $(this).attr('href');
	$('header ul li a').removeClass('selected');
	$('body>div').removeClass('selected');
	$('header ul li a[href="'+hash+'"]').addClass('selected');
	$('div'+hash).addClass('selected');
    });
});