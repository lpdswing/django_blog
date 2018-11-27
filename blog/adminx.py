import xadmin
from .models import Banner, Category, Tag, Tui, Article, Link
from xadmin import views

class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    #整体配置
    site_title = '博客后台管理系统'
    site_footer = 'lpdswing\'s blog'
    menu_style = 'accordion'    #菜单折叠

class LoginSettings(object):
    title = '博客后台管理系统'

class ArticleAdmin(object):
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time')
    list_per_page = 50
    ordering = ('-created_time',)
    list_display_links = ('id', 'title')
    style_fields = {"body": "ueditor"}

class BannerAdmin(object):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


class CategoryAdmin(object):
    list_display = ('id', 'name', 'index')


class TagAdmin(object):
    list_display = ('id', 'name')


class TuiAdmin(object):
    list_display = ('id', 'name')


class LinkAdmin(object):
    list_display = ('id', 'name', 'linkurl')


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(views.LoginView,LoginSettings)

xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Tui,TuiAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Link,LinkAdmin)
