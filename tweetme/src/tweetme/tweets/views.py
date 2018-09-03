from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Tweet
from .forms import TweetModelForm
from django.forms.utils import ErrorList
from django import forms
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
# Create your views here.


class TweetCreateView( FormUserNeededMixin, CreateView):
    #queryset= Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"



class TweetUpdateView( LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    #success_url = "/tweet/"

class TweetDeleteView( LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete_comfirm.html"
    success_url = reverse_lazy("tweet:list")

class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()


def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
        return context
        
    return render(request, "tweets/list_view.html", context)
