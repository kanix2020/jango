# from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import View
from .models import Post
# from .forms import PostForm
# from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):
    def get(self, request, *args, **kwargs):
      post_data = Post.objects.order_by('-id')
      return render(request, 'app/index.html', {
          'post_data': post_data
      })


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_detail.html', {
            'post_data': post_data
        })


# class CreatePostView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         form = PostForm(request.POST or None)
#         return render(request, 'app/post_form.html', {
#             'form': form
#         })
        