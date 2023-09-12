from django.urls import path
from .views import AcivityTrackerView


urlpatterns = [
    path('activity-tracker/list', AcivityTrackerView.as_view(), name='ActivityTrackerSerializer'),
]

