function showModal() {
    document.getElementById('shadow').classList.remove('hide');
    document.getElementById('modal').classList.remove('hide');

}
function cancleModal() {
    document.getElementById('shadow').classList.add('hide');
    document.getElementById('modal').classList.add('hide');

}
function Ajaxsend() {
    $.ajax({
        url:'/modal_add_class/',
        type:'POST',
        data:{'title':$('#title').val()},
        success:function (data) {
            console.log(data);
            if(data=='OK')
                location.href='/manage/';
            else
                $('#errormsg').text(data);
        }
    })
}
// {#对话框编辑班级#}
/*function editClass(nid,title) {
    document.getElementById('edit_shadow').classList.remove('hide');
    document.getElementById('edit_modal').classList.remove('hide');
    $(document).ready(function () {
        $('#edit_nid').val(nid);
        $('#edit_title').val(title);
        alert($('#edit_title').val());
    })
}*/
function editClass(ths) {
    document.getElementById('edit_shadow').classList.remove('hide');
    document.getElementById('edit_modal').classList.remove('hide');
    var row = $(ths).parent().prevAll();
    var title = $(row[0]).text();
    var nid = $(row[1]).text();
    $('#edit_title').val(title);
    $('#edit_nid').val(nid);
}
function cancle_editModal() {
    document.getElementById('edit_shadow').classList.add('hide');
    document.getElementById('edit_modal').classList.add('hide');
}
function Edit_Ajaxsend() {
    $.ajax({
        url: '/modal_edit_class/',
        type: 'POST',
        data: {'title': $('#edit_title').val(), 'nid': $('#edit_nid').val()},
        success: function (data) {
            console.log(data);
            data = JSON.parse(data);
            if (data.states)
                location.reload();
            else
                $('#editerror').text(data.msg);
        }
    })
}
// {#对话框删除班级#}
function delClass(ths) {
    document.getElementById('del_shadow').classList.remove('hide');
    document.getElementById('del_modal').classList.remove('hide');
    var row = $(ths).parent().prevAll();
    var nid = $(row[1]).text();
    $('#del_nid').val(nid)
}
function cancleDel() {
    document.getElementById('del_shadow').classList.add('hide');
    document.getElementById('del_modal').classList.add('hide');
}
function delAjaxsend() {
    $.ajax({
        url:'/modal_del_class/',
        type:'POST',
        data:{"nid":$('#del_nid').val()},
        success:function (data) {
            console.log(data);
            location.reload();
        }
    })
}