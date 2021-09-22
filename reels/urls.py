
from django.urls import path
from .views import GetVideos,GetUsers,GetInfluencers,GetVideoById,UpdateVideoById,DeleteVideoById

urlpatterns = [
   path('view_videos/<int:pg>/',GetVideos.as_view(),name='all-videos'),
   path('view_users/<int:pg>/',GetUsers.as_view(),name='all-users'),
   path('view_influencers/<int:pg>/',GetInfluencers.as_view(),name='all-influencers'),
   path('view_video/<int:id>/',GetVideoById.as_view(),name='video-by-id'),
   path('update_video/<int:id>/',UpdateVideoById.as_view(),name='update-video-by-id'),
   path('delete_video/<int:id>/',DeleteVideoById.as_view(),name='delete-video-by-id'),
]