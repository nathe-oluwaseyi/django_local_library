from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookList.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserList.as_view(), name='my-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),

]

