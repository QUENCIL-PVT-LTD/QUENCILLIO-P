from django.shortcuts import render
from .models import Quengame,GameDate
from moviepy.editor import *
import os.path

# Create your views here.
def home(request):
    x = []
    mydata = Quengame.objects.all().order_by('-release_date').values()[:5]
    card1 = GameDate.objects.filter(game_category__icontains="Action")
    card2 = GameDate.objects.filter(game_category__icontains="3D")
    card3 = GameDate.objects.filter(game_category__icontains="Racing")
    card4 = GameDate.objects.filter(game_category__icontains="Arcade")
    if len(card1) == 0:
        print("Empty card1")
    else:
        print("Card1 Loaded Properly")
    if len(card2) == 0:
        print("Empty card2")
    else:
        print("Card 2 Loaded Properly")
    if len(card3) == 0:
        print("Empty card 3")
    else:
        print("Card 3 Loaded Properly")
    if len(card4) == 0:
        print("Empty Card 4")
    else:
        print("Card 4 Loaded Properly")
    for i in mydata:
        x.append(i['yt'])
    print(x)
    try:
        if os.path.abspath("../gameslist/media/video/merged.mp4"):
            pass
        else:
            clip1=VideoFileClip("./gameslist/media/video/crisiscore/crisiscore1.mp4")
            clip2=VideoFileClip("./gameslist/media/video/cyberpunk2077/Cyberpunk 20772.mp4")
            clip3=VideoFileClip("./gameslist/media/video/Lunistice/lunistice2.mp4")
            clip4=VideoFileClip("./gameslist/static/games/images/ChainedEchoes/gallery/movie480_bf4.mp4")
            clip5=VideoFileClip("./gameslist/static/games/images/Foodlandimg/FloodlandVid.mp4")
            clip11=clip1.subclip(0,8)
            clip22=clip2.subclip(0,8)
            clip33=clip3.subclip(0,8)
            clip44=clip4.subclip(0,8)
            clip55=clip5.subclip(0,8)
            final=concatenate_videoclips([clip11,clip22,clip33,clip44,clip55])
            final.write_videofile("../gameslist/media/video/merged.mp4")
    except Exception as e:
        print("Videos not found / readable")

    data = '' # Declare unknown variable
    context = {'late_rele':mydata,'vids':x,'action':card1,'3d':card2,'racing':card3,'arcade':card4}
    if request.method == 'POST':
        data = request.POST.get('games')
        # print(data)
        queryset = GameDate.objects.filter(game_category__icontains=data)
        # for i in queryset:
        #     print(i.game_category.split(','))
        context_form = {'late_rele':mydata,'vids':x,'querys':queryset}
        return render(request,'index.html',context_form)
    return render(request,'index.html',context)

# Carousel redirects

def action_games(request):
    card1 = GameDate.objects.filter(game_category__icontains="Action")
    return render(request,'action.html',{'action_games':card1})

def threed_games(request):
    card1 = GameDate.objects.filter(game_category__icontains="3D")
    return render(request,'3d.html',{'3d_games':card1})

def racing_games(request):
    card1 = GameDate.objects.filter(game_category__icontains="Racing")
    return render(request,'racing.html',{'racing_games':card1})

def arcade_games(request):
    card1 = GameDate.objects.filter(game_category__icontains="Arcade")
    return render(request,'arcade.html',{'arcade_games':card1})

# Header and Footer Links

def about(request):
    return render(request,"about.html")

def reviews(request):
    return render(request,"reviews.html")

def news(request):
    return render(request,"news.html")

def gallery(request):
    return render(request,"gallery.html")

def mail(request):
    return render(request,"mail.html")

def footer(request):
    return render(request,"footer.html")

def header(request):
    return render(request,'header_nav.html')

# Games List

def resident(request):
    return render(request,"Games/Resident Evil Village.html")

def witcher(request):
    return render(request,"Games/The Witcher 3.html")

def battlefield4(request):
    return render(request,"Games/Battlefield4.html")

def battlefield1(request):
    return render(request,"Games/Battlefield.html")

def battlefield2(request):
    return render(request,"Games/Battlefield2.html")

def battlefield3(request):
    return render(request,"Games/Battlefield3.html")

def battlefield5(request):
    return render(request,"Games/Battlefield5.html")

def plaguetale(request):
    return render(request,"Games/A Plague Tale.html")

def assettocorsa(request):
    return render(request,"Games/Assetto Corsa.html")

def beamng(request):
    return render(request,"Games/BeamNG drive.html")

def chainedecho(request):
    return render(request,"Games/Chained Echoes.html")

def crisiscore(request):
    return render(request,"Games/CRISIS CORE-FINAL FANTACY VII-REUNION.html")

def cyberpunk(request):
    return render(request,"Games/Cyberpunk 2077.html")

def dyinglight(request):
    return render(request,"Games/Dying Light.html")

def dyinglighthell(request):
    return render(request,"Games/Dying Light - Hellraid.html")

def f122(request):
    return render(request,"Games/F1® 22.html")

def floodland(request):
    return render(request,"Games/Floodland.html")

def forzahorizon(request):
    return render(request,"Games/Forza Horizon 5.html")

def frostpunk(request):
    return render(request,"Games/Frostpunk.html")

def gow(request):
    return render(request,"Games/God of war.html")

def marvelmilesmorale(request):
    return render(request,"Games/Marvels SpiderMan _Miles Morales .html")

def jurassicworld(request):
    return render(request,"Games/Jurassic World Evolution 2.html")

def lunistice(request):
    return render(request,"Games/Lunistice.html")

def nba2023(request):
    return render(request,"Games/NBA 2K23.html")

def road96(request):
    return render(request,"Games/Road 96.html")

def snowrunner(request):
    return render(request,"Games/SnowRunner.html")

def lastofusp1(request):
    return render(request,"Games/The last of us partI.html")

def surge2(request):
    return render(request,"Games/The Surge 2.html")

def unchartedlegacy(request):
    return render(request,"Games/UNCHARTE_Legacy of Thieves Collection .html")

def lastofus(request):
    return render(request,"Games/Thelastofus.html")