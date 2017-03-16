$(document).ready(function(){
  function loop(i){
    $("#progressbar li").eq(0).addClass("active");
    setTimeout(function(){
      $("#progressbar li").eq(4-i).addClass("active");
      if(--i)
      loop(i);
    },1000*i)
  }

    $("#submit").click(function(){
      for(i = 0; i < 5; i++)
        $("#progressbar li").eq(i).removeClass("active");

        // var p = document.getElementById('result');
        // p.innerHTML = "";

      if($("#file_to_upload").val() != "")
      {
        var file_data = $('#file_to_upload').prop('files')[0];
        var form_data = new FormData();
        form_data.append('file', file_data);
        $.ajax({
          url: 'http://localhost:8000/upload',
          dataType: 'text',
          cache: false,
          contentType: false,
          processData: false,
          data: form_data,
          type: 'post',
          success: function(data){
            loop(3);
            $(".load").show();
            $.ajax({
              url: 'http://localhost:8000/analyze',
              dataType: 'text',
              cache: false,
              contentType: false,
              processData: false,
              type: 'post',
              success: function(data){
                if (data === "extractionfailed") {

                }
                $("#progressbar li").eq(4).addClass("active");
                $(".load").hide();
                // var p = document.getElementById('result');
                // p.innerHTML = data;
              }
            });
          }
        });
      }
      else
      {
        alert('Please Upload File');
      }
    });
  });
