function loginbut() {
        $.ajax({
            url:'/login/',
            type:'POST',
            data:{'UserName':$('#inputEmail3').val(),'Password':$('#inputPassword3').val()},
            success:function (data) {
                if(data=='OK')
                    location.href='/layout/';
                else
                    $('#loginerror').text(data);
            }
        })
        return false;
}