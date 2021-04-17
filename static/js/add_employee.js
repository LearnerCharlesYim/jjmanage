$(function () {
   $("#submit").click(function (event) {
       event.preventDefault();
       var name = $("input[name='name']").val();
       var age = $("input[name='age']").val();
       var sex = $('input[name="gender"]:checked').val();
       var hometown = $("input[name='hometown']").val();
       var working_age = $("input[name='working_age']").val();
       var education = $("select[name='education']").val();
       var certificate = $("input[name='certificate']").val();
       var resume_score = $("input[name='resume_score']").val();
       var interview_score = $("input[name='interview_score']").val();
       var project = $("select[name='project']").val();


       zlajax.post({
           'url':'/employee/add/',
           'data':{
               'name':name,
               'age':age,
               'sex':sex,
               'hometown':hometown,
               'working_age':working_age,
               'education':education,
               'certificate':certificate,
               'resume_score':resume_score,
               'interview_score':interview_score,
               'project':project,
           },
           'success':function (data) {
               if(data['code'] === 200){
                   window.location = '/employee/';
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
       $("input[name='name']").val("");
       $("input[name='age']").val("");
       $("input[name='hometown']").val("");
       $("input[name='working_age']").val("");
       $("input[name='certificate']").val("");
       $("input[name='resume_score']").val("");
       $("input[name='interview_score']").val("");

    })
});