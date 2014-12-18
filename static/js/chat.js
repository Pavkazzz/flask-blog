$("document").ready(function () {
//	var first = true,
	username = $("#home").text().slice(4),
	counter = 0;
	console.log(username);
/*
	$("#message").hide();
	$("#send").hide();

	$("#login").click(function(){
		var input = $.trim($("#username").val());
		if (input !== "") {
			$("#login").hide();
			$("#username").hide();
			$("#message").show();
			$("#send").show();
			username = input;
			$("#test").animate({
				height: "200px"
			}, 500, function(){
				setInterval(t, 1000);
			});
		}
	});
*/

	function t() {
		$.ajax({
			type: "get", 
			url: "server/read.php",
			data: {
				"counter": counter
			}

		}).done(function(msg) {
			var div, 
			i,
			msg = $.parseJSON(msg);
			//console.log(msg);
			if (counter<msg.counter) {
				counter = msg.counter;
				for (i = 0; i < msg.output.length; i++) {
					if (first) {
						$("#test div:first").remove();
						first = false;
					}
					div = $("<div>");

					div.text(
						msg.output[i].username + ": " +
						msg.output[i].message
						);	
					div.appendTo($("#test"));
				}
			}
		});
	}
	$("#send").click(function(){
		var input = $("#message");
		if ($.trim(input.val())) {
			if (first) {
				$("#test div:first").remove();
				first = false;
			}				
			$.ajax({
			type: "post",
			url: "server/write.php",
			data: {
				"username": username,
				"message": input.val()
				}
			}).done(function(msg){
				input.val("");
			});
		}
	});
});