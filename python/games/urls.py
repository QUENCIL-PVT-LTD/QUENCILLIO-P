from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home"),
# Carousel Paths
    path('action/',views.action_games,name="action"),
    path('3d/',views.threed_games,name="3d"),
    path('arcade/',views.arcade_games,name="arcade"),
    path('racing/',views.racing_games,name="racing"),
# # Header Options Paths
#     path('about/',views.about,name="about"),
#     path('reviews/',views.reviews,name="reviews"),
#     path('news/',views.news,name="news"),
#     path('gallery/',views.gallery,name="gallery"),
#     path('mail/',views.mail,name="mail"),
# # Header and Footer Paths
#     path('footer/',views.footer,name="footer"),
#     path('header/',views.header,name="header"),
# # Games Paths
#     path('resident/',views.resident,name="resident"),
#     path('witcher/',views.witcher,name="witcher"),
#     path('battlefield4/',views.battlefield4,name="battlefield4"),
#     path('battlefield1/',views.battlefield1,name="battlefield1"),
#     path('battlefield2/',views.battlefield2,name="battlefield2"),
#     path('battlefield3/',views.battlefield3,name="battlefield3"),
#     path('battlefield5/',views.battlefield5,name="battlefield5"),
#     path('jurassicworld/',views.jurassicworld,name="jurassicworld"),
#     path('cyberpunk/',views.cyberpunk,name="cyberpunk"),
#     path('road96/',views.road96,name="road96"),
#     path('floodland/',views.floodland,name="floodland"),
#     path('frostpunk/',views.frostpunk,name="frostpunk"),
#     path('plaguetale/',views.plaguetale,name="plaguetale"),
#     path('assettocorsa/',views.assettocorsa,name="assettocorsa"),
#     path('beamng/',views.beamng,name="beamng"),
#     path('chainedecho/',views.chainedecho,name="chainedecho"),
#     path('crisiscore/',views.crisiscore,name="crisiscore"),
#     path('dyinglight/',views.dyinglight,name="dyinglight"),
#     path('dyinglighthell/',views.dyinglighthell,name="dyinglighthell"),
#     path('f122/',views.f122,name="f122"),
#     path('forzahorizon/',views.forzahorizon,name="forzahorizon"),
#     path('gow/',views.gow,name="gow"),
#     path('marvelmilesmorale/',views.marvelmilesmorale,name="marvelmilesmorale"),
#     path('lunistice/',views.lunistice,name="lunistice"),
#     path('nba2023/',views.nba2023,name="nba2023"),
#     path('road96/',views.road96,name="road96"),
#     path('snowrunner/',views.snowrunner,name="snowrunner"),
#     path('lastofusp1/',views.lastofusp1,name="lastofusp1"),
#     path('surge2/',views.surge2,name="surge2"),
#     path('unchartedlegacy/',views.unchartedlegacy,name="unchartedlegacy"),
#     path('lastofus/',views.lastofus,name="lastofus"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

