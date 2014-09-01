from django.conf.urls import patterns, include, url

from django.contrib import admin
from Recipe.views import RecipeDetail, RecipeCreate, RecipeList, custom_404_view
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MadeTech.views.home', name='home'),
    # url(r'^/', include('blog.urls')),
    # Django admin site urls
    url(r'^admin/', include(admin.site.urls)),
    #Public views
    url(r'^all/', RecipeList.as_view()),
    url(r'^add/', RecipeCreate.as_view()),
    url(r'^recipe/(?P<pk>\d+)', RecipeDetail.as_view())
)

#Include custom error handlers here. A 404 hander was set up as an example. 
handler404 = custom_404_view