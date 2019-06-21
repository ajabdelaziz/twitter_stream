# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jwt
from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, Http404
from django.urls import reverse_lazy
from django.views import generic

from tweetconsumer.utils import query_json


class JWTLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        # override instance of form being processed and if is valid attach jwt to cookie
        form = self.get_form()
        if form.is_valid():
            request.session['jtw'] = jwt.encode(
                {'user': request.POST.get("username")}, "secret", algorithm='HS256'
            ).decode()
        return super(JWTLoginView, self).post(request, *args, **kwargs)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    # use reverse_lazy to load the generic class based views after the redirect
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        # override instance of form being processed and if is valid attach jwt to cookie
        form = self.get_form()
        if form.is_valid():
            request.session['jtw'] = jwt.encode(
                {'user': request.POST.get("username")}, "secret", algorithm='HS256'
            ).decode()
        return super(SignUp, self).post(request, *args, **kwargs)


@login_required
@render_to('tweet.html')
def tweets(request):
    try:
        jwt.decode(request.session['jtw'], 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise Http404
    return locals()


@login_required
def tweets_filtered(request):
    try:
        jwt.decode(request.session['jtw'], 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise Http404
    filter = request.GET.get('filter', False)
    q = request.GET.get('q', False)

    data = []
    if filter and q:
        data = query_json(filter, q)
    return JsonResponse(data, safe=False)
