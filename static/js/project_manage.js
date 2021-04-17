$(function () {
   $("#submit").click(function (event) {
       event.preventDefault();
       var project = $("select[name='project']").val();
       var user_id = $("#user-data").attr('data-id');

       zlajax.post({
           'url':'/manage/',
           'data':{
               'project': project,
               'user_id': user_id
           },
           'success':function (data) {
               if(data['code'] === 200){
                   window.location = '/manage/';
               }else{
                   var message = data['message'];
                   $("#message-p").html(message);
                   $("#message-p").show();
                }
           },
       })
   })
});


$(function () {
    $('#reset').click(function (event) {
        event.preventDefault();
        var usernameE = $("input[name='username']");
        var emailE = $("input[name='email']");
        usernameE.val("");
        emailE.val("");
    })
});