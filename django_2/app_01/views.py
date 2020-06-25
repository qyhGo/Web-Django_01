from django.shortcuts import render,redirect,HttpResponse
from pymysql import *
import pymysql
import json
import time

class SQL(object):
    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def multiple_insert(self,sql,args):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def create(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()
        return self.cursor.lastrowid

    def update(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()

    def delete(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:

        user = request.POST.get('UserName')
        pad = request.POST.get('Password')
        if user == '3160101299@zju.edu.cn' and pad == 'qyh10086':
            obj = HttpResponse('OK')
            obj.set_cookie('ticket','3160101299')
            return obj
        else:
            return HttpResponse('用户名或密码错误')

def layout(request):
    ck = request.COOKIES.get('ticket')
    if not ck:
        return redirect('/login/')
    return render(request,'layout.html')

def teacher(request):
    ck = request.COOKIES.get('ticket')
    if not ck:
        return redirect('/login/')
    class_list = classes(request)
    teachers_list = teachers(request)
    result = {}
    for item in teachers_list:
        tid = item['tid']
        if tid in result:
            result[tid]['titles'].append(item['title'])
        else:
            result[tid] = {'tid': tid, 'name': item['name'], 'titles': [item['title'], ]}
    return render(request, 'teacher.html', {
        'class_list': class_list,
        'teachers_list': result.values(),
    })

def manage(request):
    ck = request.COOKIES.get('ticket')
    if not ck:
        return redirect('/login/')
    class_list = classes(request)
    return render(request, 'classes.html', {
        'class_list': class_list,
    })

def classes(request):
    conn = connect(host='localhost',port=3306,\
                   database='django_01',user='root',\
                   password='qyh10086',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select id,title from class;')
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return class_list

def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html')

    else:
        value = request.POST.get('title')
        if len(value)!=0 and value!='添加班级':
            conn = connect(host='localhost', port=3306, \
                           database='django_01', user='root', \
                           password='qyh10086', charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute('insert into class (title) values(%s);',[value,])
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/manage/')
        else:
            return render(request,'add_class.html',{'msg':'错误输入',})

def modal_add_class(request):
    value = request.POST.get('title')
    if len(value) != 0 and value != '添加班级':
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('insert into class (title) values(%s);', [value, ])
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponse('OK')
        # return redirect('/manage/')
    else:
        # return redirect('/manage/')
        return HttpResponse('班级标题不能为空')

def del_class(request):
    id = request.GET.get('nid')
    print(id)
    conn = connect(host='localhost', port=3306, \
                   database='django_01', user='root', \
                   password='qyh10086', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('delete from class where id="{}";'.format(id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/manage/')

def modal_del_class(request):
    nid = request.POST.get('nid')
    print(id)
    conn = connect(host='localhost', port=3306, \
                   database='django_01', user='root', \
                   password='qyh10086', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('delete from class where id=%s;',[nid,])
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponse('OK')

def edit_class(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('select id,title from class where id={};'.format(nid))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request,'edit_class.html',{
            'result':result,
        })
    else:
        nid = request.POST.get('nid')
        title = request.POST.get('title')
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('update class set title=%s where id=%s;',[title,nid,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/manage/')

def modal_edit_class(request):
    ret = {'states':True,'msg':None}
    nid = request.POST.get('nid')
    title = request.POST.get('title')
    # print(nid,title)
    if len(title)!=0:
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('update class set title=%s where id=%s;', [title, nid, ])
        conn.commit()
        cursor.close()
        conn.close()
        import json
        return HttpResponse(json.dumps(ret))
    else:
        ret['states']=False
        ret['msg']='内容不能为空'
        return HttpResponse(json.dumps(ret))

def teachers(request):
    conn = connect(host='localhost',port=3306,\
                   database='django_01',user='root',\
                   password='qyh10086',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("""
        select teacher.id as tid,teacher.name,class.title 
        from teacher LEFT JOIN teacher_class on teacher_class.teacher_id=teacher.id 
        LEFT JOIN class on teacher_class.class_id = class.id;
    """)
    teachers_list = cursor.fetchall()
    cursor.close()
    conn.close()
    # print(teachers_lists)
    return teachers_list

def add_teacher(request):
    if request.method == 'GET':
        class_list = classes(request)
        return render(request,'add_teacher.html',{'class_list':class_list})
    else:
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_ids')
        obj = SQL()
        teacher_id = obj.create('insert into teacher (name) values(%s);',[name,])
        # print(teacher_id)
        # print(class_ids)
        data = []
        for i in class_ids:
            item = (teacher_id,i)
            data.append(item)
        obj.multiple_insert('insert into teacher_class (teacher_id,class_id) values(%s,%s);',data)
        obj.close()
        return redirect('/manage/')

def modal_add_teacher(request):
    ret = {'status':True,'message':None}
    try:
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_ids')
        obj = SQL()
        teacher_id = obj.create('insert into teacher (name) values(%s);',[name,])
        # print(teacher_id)
        # print(class_ids)
        data = []
        for i in class_ids:
            item = (teacher_id,i)
            data.append(item)
        obj.multiple_insert('insert into teacher_class (teacher_id,class_id) values(%s,%s);',data)
        obj.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = '执行错误'
    return HttpResponse(json.dumps(ret))

def del_teacher(request):
    nid = request.GET.get('nid')
    conn = connect(host='localhost', port=3306, \
                   database='django_01', user='root', \
                   password='qyh10086', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('delete from teacher where id="{}";'.format(nid))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/manage/')

def edit_teacher(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('select id,name from teacher where id=%s;',[nid,])
        result = cursor.fetchone()
        class_list = classes(request)
        cursor.execute('select class_id from teacher_class where teacher_id=%s;',[nid,])
        class_id_list = cursor.fetchall()
        cursor.close()
        conn.close()
        class_list_ids=[]
        for item in class_id_list:
            class_list_ids.append(item['class_id'])
        # print(class_ids)
        return render(request,'edit_teacher.html',{
            'result':result,
            'class_list':class_list,
            'class_list_ids':class_list_ids,
        })
    else:
        nid = request.POST.get('nid')
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_ids')
        # print(class_ids)
        obj = SQL()
        data = []
        for i in class_ids:
            item = (nid,i)
            data.append(item)
        obj.update('update teacher set name=%s where id=%s;',[name,nid,])
        obj.delete('delete from teacher_class where teacher_id=%s;',[nid,])
        obj.multiple_insert('insert into teacher_class (teacher_id,class_id) values(%s,%s);',data)
        obj.close()
        return redirect('/manage/')

def student(request):
    ck = request.COOKIES.get('ticket')
    if not ck:
        return redirect('/login/')
    conn = connect(host='localhost', port=3306, \
                   database='django_01', user='root', \
                   password='qyh10086', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select student.id,student.name,class.title,student.class_id from student left JOIN class on student.class_id=class.id;')
    student_list = cursor.fetchall()
    cursor.close()
    conn.close()
    class_list = classes(request)
    return render(request,'student.html',{
        'student_list':student_list,
        'class_list':class_list,
    })

def add_student(request):
    if request.method == 'GET':
        class_list = classes(request)
        return render(request,'add_student.html',{
            'class_list':class_list
        })
    else:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('insert into student (name,class_id) values(%s,%s);',[name,class_id,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/student/')

def modal_add_student(request):
    ret = {'status':True,'message':None}
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('insert into student (name,class_id) values(%s,%s);', [name, class_id, ])
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        ret['status']=False
        ret['message']=str(e)
    return HttpResponse(json.dumps(ret))

def edit_student(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(
            'select id,name,class_id from student where id=%s;',[nid,])
        student_list = cursor.fetchone()
        cursor.close()
        conn.close()
        class_list = classes(request)
        return render(request,'edit_student.html',{
            'student_list':student_list,
            'class_list':class_list,
        })
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(
            'update student set name=%s,class_id=%s where id=%s;', [name,class_id,nid,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/student/')

def modal_edit_student(request):
    ret = {'status':True,'message':None}
    try:
        nid = request.POST.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(
            'update student set name=%s,class_id=%s where id=%s;', [name, class_id, nid, ])
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        ret['states'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))

def modal_del_student(request):
    ret = {'status':True,'message':None}
    try:
        nid = request.POST.get('nid')
        # print(nid)
        conn = connect(host='localhost', port=3306, \
                       database='django_01', user='root', \
                       password='qyh10086', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute('delete from student where id="{}";'.format(nid))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        ret['states'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))

def get_class_list(request):
    class_list = classes(request)
    # time.sleep(1)
    return HttpResponse(json.dumps(class_list))