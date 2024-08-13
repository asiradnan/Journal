from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

class create(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title","maincontent","is_private"]
    template_name = "create.html"
    success_url = "/"

    def form_valid(self,form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class publicPosts(ListView):
    model = Post
    template_name = "publicposts.html"

class update(UpdateView):
    model = Post
    template_name = "create.html"
    fields = ["title","maincontent","is_private"]
    success_url = "/"

class delete(DeleteView):
    model = Post
    success_url = reverse_lazy("publicposts")
    template_name="delete.html"
