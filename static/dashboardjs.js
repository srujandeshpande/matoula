$(function(){

  $.ajax({
    url: '/get_items',
    type: 'POST',
    data: "",
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    async: true,
    success: function(msg) {
      var count = msg['count'];
      $('#alertcount').html(count);
      var r = "record";
      for (var i=0;i<count;i++){
            $("#clothestable").append('<tr><td>'+msg[r+i]['index']+"</td><td>"+msg[r+i]['name']+'</td><td>'+msg[r+i]['type']+'</td><td>'+msg[r+i]['color']+'</td><td>'+msg[r+i]['lastworn']+"</td><td><button class='markWorn' data-email="+msg[r+i]['email']+"data-index="+msg[r+i]['index']+">Mark As Worn Today</button></td></tr>");
          }
          $('.markWorn').unbind().click(function(event) {
            email = $(this).data('email');
            index = $(this).data('index');
            event.preventDefault()
          });
      }
    });

});
