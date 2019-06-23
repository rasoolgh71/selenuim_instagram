from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View,TemplateView,HttpResponse,HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from website.forms import Logininsta

import datetime
# Create your views here.


class Home(TemplateView):
    template_name = 'website/home.html'


class LoginView(FormView):
    """
    Login user and redirect to setting page

    """

    template_name = 'website/view_login.html'
    success_url = 'website/login_insta/'
    form_class = AuthenticationForm


    def post(self, request):

        try:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            print(username)
            print(password)
            user = authenticate(password=password, username=username)
            if user is not None:
                login(request, user)
                print("login is true")
                return HttpResponseRedirect('/login_insta')
            else:
                return HttpResponseRedirect('/view_login')
            return render(request, 'website/view_login.html')
        except Exception as e:
            print(e)


class Login_instagram(FormView):
    form_class = Logininsta
    template_name = 'website/login.html'
    def post(self,request):
        last_login=datetime.datetime.now()
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print('username:', username)
        print('password:', password)
        if (username):
            return HttpResponseRedirect('/panel/home')

        else:
            return HttpResponseRedirect('/login_insta')






# @login_required(login_url='/view_login')
# def login_insta(request):
#     global tem
#     last_login=datetime.datetime.now()
#     print("time is:",last_login)
#     form = Logininsta(request.POST)
#     if request.method == "POST":
#         try:
#             username = request.POST.get('username','')
#             password = request.POST.get('password','')
#             print('username:',username)
#             print('password:',password)
#             tem = bot.Bot()
#             request.session["username"]=username
#             check_login = tem.login(username=username,password=password)
#             if (check_login ==True):
#                 user_id=tem.get_user_id_from_username(username)
#                 #print("user_id",user_id)
#                 profil_pic_url=tem.get_profile_pic_url(user_id)
#                 #print("profil_pic_url",profil_pic_url)
#                 follower_count=tem.get_follower_count(user_id)
#                 #print("follower_count",follower_count)
#                 following_count=tem.get_following_count(user_id)
#                 #print("following_count",following_count)
#                 total_follows=tem.total['follows']
#                 #print("totol",total_follows)
#                 get_bio=tem.get_biography(user_id)
#                 count_media=len(tem.get_total_user_medias(user_id))
#                 #print("count_media:",count_media)
#
#
#
#                 new_login = Instagarm_login(username=username, password=password, last_login=last_login,
#                                             following_count=following_count, follower_count=follower_count,
#                                             profil_pic_url=profil_pic_url, total_follows=total_follows,
#                                             user_id=user_id,biogrphi=get_bio,count_media=count_media)
#
#                 created=Instagarm_login.objects.filter(user_id=user_id).exists()
#                 print("created:",created)
#                 if created:
#
#                     print(" user exisit,update user ")
#                     Instagarm_login.objects.filter(username=username).update(username=username, password=password,
#                                                                              last_login=last_login,
#                                                                              following_count=following_count,
#                                                                              follower_count=follower_count,
#                                                                              profil_pic_url=profil_pic_url,
#                                                                              total_follows=total_follows,
#                                                                              user_id=user_id,biogrphi=get_bio,
#                                                                              count_media=count_media)
#                 else:
#                     print("user no exixit,new user create")
#                     new_login.save()
#                     new_setting = Setting(follow=False, unfollow=False, like=False, comment=False,
#                                           userid=Instagarm_login.objects.get(username=username))
#                     new_setting.save()
#                 return HttpResponseRedirect('/insta')
#
#             else:
#                 return HttpResponseRedirect('/login')
#         except Exception as e:
#             print(e)
#
#     return render(request, 'task/login.html')

class LogoutView(FormView):
    try:
        template_name = '/login'

        def get(self, request):
            logout(self.request)
            user_logout=self.request.user.username
            return HttpResponseRedirect('/')
    except Exception as e:
        print(e)
