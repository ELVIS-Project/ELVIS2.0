from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
import database.views as views
from database.views import front_end_views
from database.views.person import CreatePersonView
from database.views.genre import CreateGenreView
from database.views.instrument import CreateInstrumentView
from database.views.institution import CreateInstitutionView
from database.views.archive import CreateArchiveView
from database.views.collection_of_sources import CreateCollectionOfSourcesView
from database.views.musical_work import CreateMusicalWorkView
from database.views.audio_file import CreateAudioFileView
from database.views.contributed_to import CreateContributedToView
from database.views.encoder import CreateEncoderView
from database.views.geographic_area import CreateGeographicAreaView
from database.views.image_file import CreateImageFileView
from database.views.part import CreatePartView
from database.views.research_corpus import CreateResearchCorpusView
from database.views.section import CreateSectionView
from database.views.software import CreateSoftwareView
from database.views.symbolic_music_file import CreateSymbolicMusicFileView
router = DefaultRouter()
router.register(r'instruments', views.InstrumentViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'geographicareas', views.GeographicAreaViewSet)
router.register(r'sections', views.SectionViewSet)
router.register(r'musicalworks', views.MusicalWorkViewSet)
router.register(r'parts', views.PartViewSet)
router.register(r'sources', views.SourceViewSet)
router.register(r'collections', views.CollectionOfSourcesViewSet)
router.register(r'institutions', views.InstitutionViewSet)
router.register(r'symbolicmusicfiles', views.SymbolicMusicFileViewSet)
router.register(r'extractedfeatures', views.ExtractedFeatureViewSet)
router.register(r'encoders', views.EncoderViewSet)
router.register(r'archives', views.ArchiveViewSet)
router.register(r'audiofiles', views.AudioFileViewSet)
router.register(r'contributions', views.ContributedToViewSet)
router.register(r'corpora', views.ResearchCorpusViewSet)
router.register(r'software', views.SoftwareViewSet)
router.register(r'imagefiles', views.ImageFileViewSet)
router.register(r'textfiles', views.TextFileViewSet)
router.register(r'validators', views.ValidatorViewSet)

urlpatterns = [
    url(r'^$', front_end_views.HomeView.as_view(), name='home'),
    url(r'^about/$', front_end_views.AboutView.as_view(), name='about'),
    url(r'^piece/new/$', front_end_views.CreatePieceView.as_view(), name='piece_new'),
    url(r'^signup/$', front_end_views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        front_end_views.activate, name='activate'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^', include(router.urls)),
    url(r'^search/$', views.search.TestFacet.as_view(),
        name='search'),
    url(r'^person/new/$', CreatePersonView.as_view(), name='person_new'),
    url(r'^genre/new/$', CreateGenreView.as_view(), name='genre_new'),
    url(r'^instrument/new/$', CreateInstrumentView.as_view(), name='instrument_new'),
    url(r'^institution/new/$', CreateInstitutionView.as_view(), name='institution_new'),
    url(r'^archive/new/$', CreateArchiveView.as_view(), name='archive_new'),
    url(r'^collectionofsources/new/$', CreateCollectionOfSourcesView.as_view(), name='collectionofsources_new'),
    url(r'^musicalwork/new/$', CreateMusicalWorkView.as_view(), name='musicalwork_new'),
    url(r'^audiofile/new/$', CreateAudioFileView.as_view(), name='audiofile_new'),
    url(r'^contributedto/new/$', CreateContributedToView.as_view(), name='contributedto_new'),
    url(r'^encoder/new/$', CreateEncoderView.as_view(), name='encoder_new'),
    url(r'^geographicarea/new/$', CreateGeographicAreaView.as_view(), name='geographicarea_new'),
    url(r'^imagefile/new/$', CreateImageFileView.as_view(), name='imagefile_new'),
    url(r'^part/new/$', CreatePartView.as_view(), name='part_new'),
    url(r'^researchcorpus/new/$', CreateResearchCorpusView.as_view(), name='researchcorpus_new'),
    url(r'^section/new/$', CreateSectionView.as_view(), name='section_new'),
    url(r'^software/new/$', CreateSoftwareView.as_view(), name='software_new'),
    url(r'^symbolicmusicfile/new/$', CreateSymbolicMusicFileView.as_view(), name='symbolicmusicfile_new'),
]
