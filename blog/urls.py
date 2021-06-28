from django.urls import path
from django.views.generic.edit import DeleteView
from blog.views import(

	create_blog_view,
	detail_blog_view,
	edit_blog_view,
	delete,
	cross_off,
	uncross,
	

)

app_name = 'blog'

urlpatterns = [
	path('create/', create_blog_view, name="create"),
	path('<slug>/', detail_blog_view, name="detail"),
	path('<slug>/edit', edit_blog_view, name="edit"),
	path('delete/<list_id>', delete, name = 'delete'),
    path('cross_off/<list_id>', cross_off, name = 'cross_off'),
    path('uncross/<list_id>', uncross, name = 'uncross'),
	#path('<slug>/delete',DeletePostView(),name='delete_post'),
]	