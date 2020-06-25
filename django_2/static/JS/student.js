$(function () {
    $('#addClass').click(function () {
        $('#addShadow,#addModal').removeClass('hide');
    });
    $('#cancleadd').click(function () {
        $('#addShadow,#addModal').addClass('hide');
    });
    $('#butid').click(function () {
        $.ajax({
            url:'/modal_add_student/',
            type:'POST',
            data:{'class_id':$('#classID').val(),'name':$('#addname').val()},
            success:function (data) {
                data = JSON.parse(data);
                if(data.status)
                    location.reload();
                else
                    $('#addError').val(data.message)
            }
        })
    });

    $('#edit_student').click(function () {
        $('#editShadow,#editModal').removeClass('hide');
        var row = $(this).parent().prevAll();
        var nid = $(row[2]).text();
        var name = $(row[1]).text();
        var class_id = $(row[0]).attr('clsid');
        $('#editname').val(name);
        $('#nameId').val(nid);
        $('#classId').val(class_id);
    });
    $('#cancleedit').click(function () {
        $('#editShadow,#editModal').addClass('hide');
    });
    $('#editbut').click(function () {
        $.ajax({
            url:/modal_edit_student/,
            type:'POST',
            data:{
                'nid':$('#nameId').val(),
                'name':$('#editname').val(),
                'class_id':$('#classId').val()
            },
            dataType:'JSON',
            success:function (data) {
                if(data.status)
                    location.reload();
                else
                    $('#editError').val(data.message);
            }
        })
    })

    $('#del_student').click(function () {
        $('#addShadow,#delModal').removeClass('hide');
        var row = $(this).parent().prevAll();
        var nid = $(row[2]).text();
        var name = $(row[1]).text();
        var class_id = $(row[0]).attr('clsid');
        $('#delnameId').val(nid);
    });
    $('#cancledel').click(function () {
        $('#addShadow,#delModal').addClass('hide');
    });
    $('#delbut').click(function () {
        $.ajax({
            url:'/modal_del_student/',
            type:'POST',
            data:{'nid':$('#delnameId').val()},
            dataType:'JSON',
            success:function (data) {
                if(data.status)
                    location.reload();
                else
                    $('#delError').val(data.message);
            }
        })
    })
})