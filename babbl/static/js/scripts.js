$(document).ready(function(){

	$("a").click(function(){
		var href = $(this).attr("href");
		if (href.indexOf('#') == -1)
		{
			$(".loading").show();
		}
	})

})