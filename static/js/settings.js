$(function () {
   $("#submit").click(function (event) {
       event.preventDefault();
       var usernameE = $("input[name='username']");
       var emailE = $("input[name='email']");

       var username = usernameE.val();
       var email = emailE.val();

       zlajax.post({
           'url':'/settings/',
           'data':{
               'username':username,
               'email':email
           },
           'success':function (data) {
               if(data['code'] === 200){
                   window.location = '/profile/';
               }else{
                   var message = data['message'];
                   $("#message-p").html(message);
                   $("#message-p").show();
                   usernameE.val("");
                   emailE.val("");
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