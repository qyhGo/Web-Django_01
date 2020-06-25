$('#addteacher').click(function () {
        addTeacher();
})
function addTeacher() {
    $('#shadow,#loading').removeClass('hide');
    $.ajax({
        url:'/get_class_list/',
        type:'GET',
        dataType:'JSON',
        success:function (data) {
            $.each(data,function (i,row) {
                var tag = document.createElement('option');
                tag.innerHTML=row.title;
                tag.setAttribute('value',row.id);
                $('#classIDs').append(tag);
            });
            $('#loading').addClass('hide');
            $('#addTmodal').removeClass('hide');
        }
    });
}
$('#cancleaddT').click(function () {
    $('#shadow,#addTmodal').addClass('hide');
})
$('#addTbut').click(function () {
    addTbut();
})
function addTbut() {
    var name = $('#addT_name').val();
    var class_id_list = $('#classIDs').val();
    $.ajax({
        url:'/modal_add_teacher/',
        type:'POST',
        data:{'name':name,'class_ids':class_id_list},
        traditional:true,
        dataType:'JSON',
        success:function (data) {
            if(data.status)
                location.reload();
            else
                $('#addTerror').text(data.message);
        }
    })
}