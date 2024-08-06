import time

from django.shortcuts import render, redirect, reverse
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, StreamingHttpResponse, \
    FileResponse, Http404, JsonResponse
from django.views.generic import RedirectView, TemplateView, ListView, DetailView
from .models import PersonInfo, Vocation, createNewTab
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .form import PersonInfoForm, VocationForm
from django.db.models import F
from django.db import transaction


# def index(request):
#     # c = ContentType.objects.values_list().all()
#     # print(c)
#     # value = {'title': 'Hello World!'}
#     # content = {'content':'This is content'}
#     value = 'Hello Python'
#     return render(request, 'index.html', locals())
#     # return HttpResponse(f'路由地址之外的变量{month}')
#     # return redirect(reverse('index:myvariable', args=[2024, 7, 24]))
#     # return redirect('index:shop', permanent=True)
#     # url = reverse('index:shop')
#     # 设置302重定向
#     # return HttpResponseRedirect(url)
#     # 设置301重定向
#     # return HttpResponsePermanentRedirect(url)
#     # if request.method == 'GET':
#     #     # WSGIRequest类方法的使用
#     #     print(request.is_secure())
#     #     print(request.is_ajax())
#     #     print(request.get_host())
#     #     print(request.get_full_path())
#     #     print(request.get_raw_uri())
#     #     # WSGIRequest类属性的使用
#     #     print(request.COOKIES)
#     #     print(request.content_type)
#     #     print(request.META)
#     #     print(request.GET.get('user', ''))
#     #     return render(request, 'index.html')
#     # else:
#     #     print(request.POST.get('user', ''))
#     #     return render(request, 'index.html')


def shop(request):
    return render(request, 'shop.html')


def myvariable(request, year, month, day):
    return HttpResponse(f'{year}/{month}/{day}')


def mydate(request, year, month, day):
    return HttpResponse(f'正则路由：{year}/{month}/{day}')


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def page_error(request):
    return render(request, '500.html', status=500)


def download_file1(request):
    file_path = 'static/file1.jpg'
    try:
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read())
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="file1.jpg"'
            return response
    except FileNotFoundError:
        raise FileNotFoundError('文件不存在')


def download_file2(request):
    file_path = 'static/file2.png'
    try:
        with open(file_path, 'rb') as f:
            response = StreamingHttpResponse(f.read())
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="file2.png"'
            return response
    except FileNotFoundError:
        raise FileNotFoundError('文件不存在')


def download_file3(request):
    file_path = 'static/file3.png'
    try:
        f = open(file_path, 'rb')
        response = FileResponse(f, as_attachment=True, filename='file3.png')
        return response
    except FileNotFoundError:
        raise FileNotFoundError('文件不存在')


def upload(request):
    if request.method == 'POST':
        file = request.FILES.get('file', None)
        if file:
            file_name = file.name
            with open(f'static/{file_name}', 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            return HttpResponse('上传成功')
        else:
            return HttpResponse('上传失败')
    else:
        return render(request, 'upload.html')


def create(request):
    r = redirect(reverse('index:index'))
    r.set_cookie('uid', 'Cookie_value')
    r.set_signed_cookie('uid', 'Signed_Cookie_value', salt='salt', max_age=30)
    return r


def myCookie(request):
    cookie_exist = request.COOKIES.get('uid', None)
    if cookie_exist:
        request.get_signed_cookie('uid', salt='salt')
        return HttpResponse(f'Cookie存在,当前Cookie为：{cookie_exist}')
    else:
        raise Http404('Cookie不存在')


def getHeader(request):
    header = request.META.get('HTTP_SIGN', None)
    if header:
        value = {'header': header}
    else:
        value = {'header': 'Header不存在'}
    return JsonResponse(value)


class turnTo(RedirectView):
    permanent = False
    url = None
    pattern_name = 'index:index'

    # 重写get_redirect_url方法
    def get_redirect_url(self, *args, **kwargs):
        print('This is get_redirect_url')
        return super().get_redirect_url(*args, **kwargs)

    # 重写get方法
    def get(self, request, *args, **kwargs):
        print('This is get')
        print(request.META.get('HTTP_USER_AGENT'))
        return super().get(request, *args, **kwargs)


# class index(DetailView):
#     template_name = 'index.html'
#     # template_engine = None
#     # content_type = None
#     extra_context = {'title':'人员信息表'}
#     # paginate_by = 1
#     slug_field = 'age'
#     slug_url_kwarg = 'age'
#     pk_url_kwarg = 'pk'
#     model = PersonInfo
#     queryset = PersonInfo.objects.all()
#     context_object_name = 'personinfo'
#     query_pk_and_slug = False
#     # 重写父类ContextMixin的get_context_data方法
#     # def get_context_data(self, **kwargs):
#     #     print('This is get_context_data')
#     #     context = super().get_context_data(**kwargs)
#     #     context['value'] = 'I am django'
#     #     return context
#     # def post(self, request, *args, **kwargs):
#     #     self.extra_context = {'title':'This is Post'}
#     #     context = super().get_context_data(**kwargs)
#     #     return self.render_to_response(context)
def result(request):
    return HttpResponse('SUCCESS')


# class index(CreateView):
#     initial = {'name':'Betty','age':18}
#     template_name = 'index.html'
#     success_url = '/result'
#     extra_context = {'title':'人员信息表'}
#     # 表单生成方式一
#     # form_class = PersonInfoForm
#     # 表单生成方式二
#     model = PersonInfo
#     fields = ['name','age']

# class index(UpdateView):
#     initial = {'name':'Betty','age':18}
#     template_name = 'index.html'
#     success_url = '/result'
#     extra_context = {'title':'人员信息表'}
#     model = PersonInfo
#     fields = ['name','age']
#     slug_field = 'age'
#     slug_url_kwarg = 'age'

# class index(DeleteView):
#     template_name = 'index.html'
#     success_url = '/result'
#     extra_context = {'title':'人员信息表'}
#     model = PersonInfo
#     context_object_name = 'personinfo'
# 在视图函数中使用事务
# @transaction.atomic
# def index(request):
#     # 开启事务
#     sid = transaction.savepoint()
#     try:
#         id = request.GET.get('id', None)
#         if id:
#             v = Vocation.objects.filter(id=id)
#             v.update(payment=F('payment') + 1)
#             print('Done')
#             # 提交事务
#             transaction.savepoint_commit(sid)
#         else:
#             Vocation.objects.update(payment=F('payment') - 1)
#             # 回滚事务
#             transaction.savepoint_rollback(sid)
#     except Exception as e:
#         # 回滚事务
#         transaction.savepoint_rollback(sid)
#     return render(request, 'index.html', locals())


def indexView(request):
    today = time.localtime(time.time())
    model_name = f'sales{time.strftime("%Y%m%d", today)}'
    model_class = createNewTab(model_name)
    model_class.objects.create(
        product='Django', sales=666)
    return HttpResponse('SUCCESS')


def index(request):
    v = VocationForm()
    return render(request, 'index.html', locals())