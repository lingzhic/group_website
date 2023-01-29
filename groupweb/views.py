from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

# from pure_pagination.mixins import PaginationMixin
from .instance_models import GroupMember, Publication

from .models import Category, Post, Tag


def index_view(request):
    context = {}
    return render(request, 'index.html', context)


def research_view(request):
    context = {}
    return render(request, 'Research.html', context)


def member_view(request):
    context = {}
    member_list = []
    lingzhi = GroupMember(name='lingzhi', position='student', bio='Hi, I am lingzhi')
    member_list.append(lingzhi)
    context = {'member_list': member_list}
    return render(request, 'Group_members.html', context)


def publication_view(request):
    context = {}
    publication_list = []
    with open('groupweb/static/txt_info/Publications/Soft_mat') as f:
        soft_mat_pulication_list = f.readlines()
    # pub1 = Publication(title='test title', journal='test journal', doi='test doi')
    # publication_list.append(pub1)
    context = {'soft_mat_pulication_list':soft_mat_pulication_list, 'publication_list': publication_list}
    return render(request, 'Publications.html', context)


def opportunities_view(request):
    context = {}
    return render(request, 'Opportunities.html', context)

# class IndexView(ListView):
#     model = Post
#     template_name = "index.html"

#
# # 记得在顶部导入 DetailView
# class PostDetailView(DetailView):
#     # 这些属性的含义和 ListView 是一样的
#     model = Post
#     template_name = "groupweb/detail.html"
#     context_object_name = "post"
#
#     def get(self, request, *args, **kwargs):
#         # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
#         # get 方法返回的是一个 HttpResponse 实例
#         # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
#         # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
#         response = super().get(request, *args, **kwargs)
#
#         # 将文章阅读量 +1
#         # 注意 self.object 的值就是被访问的文章 post
#         self.object.increase_views()
#
#         # 视图必须返回一个 HttpResponse 对象
#         return response
