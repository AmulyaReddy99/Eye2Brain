$(document).ready(function() {
    var frm = $('#input_form');
    frm.submit(function(e) {
        e.preventDefault();        
        $.ajax({
            type: 'POST',
            url: '/models',
            data: {
                name: $('#name').val(),
                img: $('#id').val()
            },
            success: function(data) {
                // data = JSON.parse(data); // converts string of json to object
                console.log("================",data);
                $('#photo').html("<p>Done right</p>");
                alert("Done"); 
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) { 
                alert("Status: " + textStatus); alert("Error: " + errorThrown); 
            }
        });
        return false;
    });
});