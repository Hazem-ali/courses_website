from django.urls import path, include
from courses_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courselist', views.CourseViewSet)
router.register('categorylist', views.CategoryViewSet)
router.register('articlelist', views.ArticleViewSet)
router.register('partnerlist', views.PartnerViewSet)

# router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('courses/', views.CoursesView.as_view()),
    path('categories/', views.CategoriesView.as_view()),
    path('articles/', views.ArticlesView.as_view()),
    path('partners/', views.PartnersView.as_view()),
    path('', include(router.urls))



]
