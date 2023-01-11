$("#sort_title").on("input",function(){
    $.ajax({
		type: "post",
		url: "/main/",
		data: {"filter_title":$(this).val()},
		cache: false,
		success: function(response) {
			if (response.title == "") {
				$("#gallery div").css("display", "block")
			} else {
				$("#gallery div").css("display", "none")
				element = $("#gallery").find("div[data-title *=" + response.title + "]")
				element.each(function () {
					$(this).css("display", "block")
				});
			}
		}
	})
})