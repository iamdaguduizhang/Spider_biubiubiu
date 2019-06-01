# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response

from TestModel.models import Test


def add_task(request):
    return render_to_response('add_task.html')


# 数据库操作
def testdb(request):
    print(request.GET)
    name = request.GET['name']
    keyword = request.GET['keyword']
    platform = request.GET['platform']
    print(name, keyword, platform)
    test1 = Test(name=name, search_engine=keyword, keyword_search=platform, page_num='1')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


# 数据库操作
def test_show(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    print(list)
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")
    list2 = {
        'list': list
    }
    # 输出所有数据
    for var in list:

        print(type(var), '===')
        response1 = str(var.id) + "|" + var.name + '|' + var.search_engine + '|' + var.keyword_search + \
                     '|' + str(var.page_num) + '|' + str(var.status)

    response = response1
    return render_to_response('show_task.html', list2)


def updatetestdb(request):

    return render_to_response('update_task.html')


# 数据库操作
def updatetestdb2(request):
    try:
        task_id = request.GET['task_id']
        test1 = Test.objects.get(id=task_id)
        test1.name = request.GET['name']
        test1.search_engine = request.GET['search_engine']
        test1.keyword_search = request.GET['keyword']
        test1.page_num = request.GET['page_num']
        test1.status = request.GET['status']
        test1.save()

        # 另外一种方式
        # Test.objects.filter(id=1).update(name='Google')

        # 修改所有的列
        # Test.objects.all().update(name='Google')
    except Exception as e:
        return HttpResponse("<p>修改失败</p>")
    else:
        return HttpResponse("<p>修改成功</p>")


def del_task(request):
    return render_to_response('del_task.html')


# 数据库操作
def del_task2(request):

    try:
        print(request.GET)
        task_id = request.GET['task_id']
        print(task_id, type(task_id))
        test1 = Test.objects.get(id=task_id)
        test1.delete()

        # 另外一种方式
        # Test.objects.filter(id=1).delete()

        # 删除所有数据
        # Tst.objects.all().delete()

    except Exception as e:
        return HttpResponse("<p>删除失败</p>")
    else:
        return HttpResponse("<p>删除成功</p>")


# 数据库操作
def get_task(request):

    list = Test.objects.filter(status=1)
    task = list[0]
    task_content = {
        'id':task.id,
        'name': task.name,
        'search_engine': task.search_engine,
        'keyword': task.keyword_search,
        'pagenum': task.page_num,
        'status': task.status
    }

    task.status = 0
    task.save()

    return HttpResponse(json.dumps(task_content))