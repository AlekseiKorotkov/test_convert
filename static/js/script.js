$(document).ready(function() {
       $("#test").submit(function(event){
           event.preventDefault();
           event.stopPropagation();
            $.ajax({
                 type:"POST",
                 url:"/my_ajax_request/",
                 data: {
                        'number': $('#numberField').val()
                        },
                 dataType: 'json',
                success: function(data){
                     $('#result_convert').val(data.value)
                 }
            });

       });

});