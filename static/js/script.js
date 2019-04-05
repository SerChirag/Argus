(function() {
$(document).ready(function() {
    var x  = document.getElementById("cur_img").src.split('/')
    document.getElementById("hidden_img").value = x[x.length-1]
    var counter = 0;
    $('form').on('submit', function(event){
        $.ajax({
            data : {
                name : $('#name').val(),
                hidden_img : $('#hidden_img').val()
            },
            type : 'POST',
            url : '/process'
        })
        .done(function(data){
            if(data.error){
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            }
            else{
                console.log(data.name)
                document.getElementById("cur_img").src='http://localhost:5000/static/img/'+data.name
                document.getElementById("hidden_img").value = data.name
                console.log(data.flag);
                console.log(counter);
                if(data.flag) {
                    $('#successAlert').text(data.name).show();
                    $('#errorAlert').hide();
                    if(counter==4){
                        console.log("Your vision acuity is perfect for this eye");
                        document.getElementById("testBox").innerHTML = "Your vision acuity is perfect for this eye";
                    }
                }
                else{
                    $('#errorAlert').text(data.error).show();
                    $('#successAlert').hide();
                    console.log("Your Vision Acuity is "+counter);
                    document.getElementById("testBox").innerHTML = ("Your Vision Acuity is "+counter);                    
                }
                counter = counter+1;
            }
        });
        event.preventDefault();
    });
});
}).call(this);
