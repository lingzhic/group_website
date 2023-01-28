from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

# from pure_pagination.mixins import PaginationMixin

from .models import Category, Post, Tag


class IndexView(ListView):
    model = Post
    template_name = "index.html"


class ResearchView(ListView):
    model = Post
    template_name = "Research.html"


class MemberView(ListView):
    model = Post
    template_name = "Group_members.html"


class PubView(ListView):
    model = Post
    template_name = "Publications.html"


class OppView(ListView):
    model = Post
    template_name = "Opportunities.html"

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
