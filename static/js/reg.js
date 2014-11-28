$(document).ready(function(){
    $('#user-email').bind("change paste keyup", function(event){
        $('#user-id').val(event.target.value.split('@')[0]);
    });
});