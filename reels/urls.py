
from django.urls import path
from .views import GetVideos,CheckUser,CreateUser,GetUsers,GetVideoById,UpdateVideoById,DeleteVideoById,CreateVideo ,MlModel 

urlpatterns = [
   path('view_videos/',GetVideos.as_view(),name='all-videos'),
   path('view_users/',GetUsers.as_view(),name='all-users'),
   # signup
   path('create_user/',CreateUser.as_view(),name='create-user'),
   # login
   path('check_user/<str:name>/',CheckUser.as_view(),name='check-user'),
   # path('view_influencers/',GetInfluencers.as_view(),name='all-influencers'),
   path('view_video/<int:id>/',GetVideoById.as_view(),name='video-by-id'),
   path('create_video/',CreateVideo.as_view(),name='create-video'),
   path('update_video/<int:pk>/',UpdateVideoById.as_view(),name='update-video-by-id'),
   path('delete_video/<int:id>/',DeleteVideoById.as_view(),name='delete-video-by-id'),

   # path('recommendation/', Nlp.as_view(), name= 'recommendation'),
   path('analyse/', MlModel.as_view(), name= 'ml')
]