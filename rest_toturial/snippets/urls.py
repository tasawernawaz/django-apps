from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from snippets.views import SnippetViewSet, UserViewSet, api_root


router = DefaultRouter()
router.register(r"snippets", SnippetViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'delete'
# })
#
# snippet_highlight = SnippetViewSet.as_view(
#     {'get': 'highlight'},
#     renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = [
#     url(r"^$", api_root),
#     url(r"^snippets/$", snippet_list, name="snippet-list"),
#     url(r"^snippets/(?P<pk>\d+)/$", snippet_detail, name="snippet-detail"),
#     url(r"^snippets/(?P<pk>[0-9]+)/highlight/$", snippet_highlight, name="snippet-highlight"),
#     url(r"^users/$", user_list, name="user-list"),
#     url(r"^users/(?P<pk>\d+)/$", user_detail, name="user-detail")
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)