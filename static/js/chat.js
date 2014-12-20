$("document").ready(function () {
    username = $("#home").text().slice(4),
    counter = 0,
    first = true;
    setInterval(t, 1000);

    function t() {
        $.ajax({
            type: "get", 
            url: "chat",
            data: {
                "counter": counter
            }
        }).done(function(msg) {
            var div, 
            i,
            msg = $.parseJSON(msg);
            if (counter<msg.counter) {
                counter = msg.counter;
                $("#test").val("");
                for (i = 0; i < msg.output.length; i++) {
                    if (first) {
                        $("#test div:first").remove();
                        first = false;
                    }
                    div = $("<div class=\"removeMe\">");

                    div.text(
                        msg.output[i].username + ": " +
                        msg.output[i].message
                        );  
                    div.appendTo($("#test"));
                }
                //$("#test").scrollTop($("#test div:last").offset().top);
            }
        });
    }
    $("#send").click(function(){
        var input = $("#message");
        if ($.trim(input.val())!=="") {
            if (first) {
                $("#test div:first").remove();
                first = false;
            }               
            $.ajax({
            type: "post",
            url: "chat",
            data: {
                "username": username,
                "message": input.val()
                }
            }).done(function(msg){
                input.val("");
                $('.removeMe').remove();
            });
        }
    });
});