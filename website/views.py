from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from project.settings import (
    APP_NAME,
    MAX_AGE_COOKIE,
    USER_COOKIE_NAME
)
from question_answer.models import (
    Theme,
    Duel,
    Member
)
from uuid import uuid4
from accounts.models import User


def home(req):
    if req.method == 'POST':
        return create_duel(req)

    app_name = APP_NAME
    themes = Theme.objects.all()
    user_cookie = req.COOKIES.get(USER_COOKIE_NAME)
    if not user_cookie:
        resp = render(req, 'website/home.html', locals())
        resp.set_cookie(USER_COOKIE_NAME, str(uuid4()),
                        max_age=MAX_AGE_COOKIE, httponly=True)
        return resp

    user = User.get_or_create_by_token(user_cookie)
    active_duels = Member.get_active_duels(user)
    return render(req, 'website/home.html', locals())


def create_duel(req):
    user_cookie = req.COOKIES.get(USER_COOKIE_NAME)
    if not user_cookie:
        return redirect('/')

    duel_token = str(uuid4())
    creator = User.get_or_create_by_token(user_cookie)
    duel = Duel.objects.create(theme_id=req.POST['theme'],
                               token=duel_token, creator=creator)
    duel.add_member(creator, is_creator=True)
    return redirect(reverse('website:duel',
                            kwargs={'duel_token': duel_token}))


def duel(req, duel_token):
    duel = get_object_or_404(Duel, token=duel_token)
    duel_is_full = duel.is_full()

    user_cookie = req.COOKIES.get(USER_COOKIE_NAME)
    if user_cookie:
        user = User.get_or_create_by_token(user_cookie)
        is_member = duel.is_member(user)
        is_creator = duel.is_creator(user)

        if not duel_is_full:
            if not is_creator and not is_member:
                duel.add_member(user)
        else:
            if not is_creator and not is_member:
                full = True
                return render(req, 'website/duel.html', locals())

        return render(req, 'website/duel.html', locals())

    if duel_is_full:
        full = True
        return render(req, 'website/duel.html', locals())

    user_cookie = str(uuid4())
    user = User.create_by_token(user_cookie)
    duel.add_member(user)

    resp = render(req, 'website/duel.html', locals())
    resp.set_cookie(USER_COOKIE_NAME, user_cookie,
                    max_age=MAX_AGE_COOKIE, httponly=True)

    return resp
