from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth import views as auth_views
from database.views import (
    AboutView,
    HomeView,
    PostgresSearchView,
    SignUpView,
    CollectionOfSourcesDetailView,
    FileDetailView,
    GenreAsInStyleDetailView,
    GenreAsInTypeDetailView,
    InstrumentDetailView,
    MusicalWorkDetailView,
    PartDetailView,
    PersonDetailView,
    SectionDetailView,
    SourceDetailView,
)


urlpatterns = [
    url(r"^$", front_end_views.HomeView.as_view(), name="home"),
    url(r"^about/$", front_end_views.AboutView.as_view(), name="about"),
    url(
        r"^search/$", postgres_search.PostgresSearchView.as_view(), name="search"
    path(
        "collectionsofsources/<int:pk>",
        CollectionOfSourcesDetailView.as_view(),
        name="collectionofsources-detail",
    ),
    path("files/<int:pk>", FileDetailView.as_view(), name="file-detail"),
    ),
    url(r"^auto-fill/$", front_end_views.AutoFillView.as_view(), name="auto-fill"),
]