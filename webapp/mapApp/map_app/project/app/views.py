from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import MapInfoModel
from .forms import MapInfoModelAdd
from tkinter import messagebox
from app.food_select import pred

def index(request):
    infodata = MapInfoModel.objects.all()
    header =['店名','ジャンル','所在地','作成日','','','画像データ']
    table_list = {
        'title' : 'テスト',
        'val'   : infodata,
        'header': header,
    }
    return render(request,'webapp/index.html',table_list)

def info(request):
    infodata = MapInfoModel.objects.all()
    header =['店名','ジャンル','所在地','作成日','','','画像データ']
    table_list = {
        'title' : '登録リスト一覧',
        'val'   : infodata,
        'header': header,
    }
    return render(request,'webapp/info.html',table_list)

def create(request,lat_int,lat_flo,lng_int,lng_flo):
    # messagebox.showinfo('check','create呼び出し');
    lat = lat_int + (lat_flo / 1000.0);
    lng = lng_int + (lng_flo / 1000.0);
    obj = MapInfoModel(lat=lat,lng=lng);
    if (request.method == 'POST'):
        # messagebox.showinfo('check','create呼び出し');
        # info = MapInfoModelAdd(request.POST,request.FILES);
        mapinfo = MapInfoModel()
        mapinfo.photo = request.FILES['photo']
        mapinfo.location = request.POST['location']
        mapinfo.lat = request.POST['lat']
        mapinfo.lng = request.POST['lng']
        mapinfo.created_at = request.POST['created_at']
        # 一度保存する(error回避)
        mapinfo.save()
        genre = pred(mapinfo.photo.path)
        new_mapinfo = MapInfoModel.objects.get(id=mapinfo.id)
        new_mapinfo.name = genre
        new_mapinfo.genre = genre
        new_mapinfo.save()
        return redirect(to='/')
    modelform_dict = {
        'title' : 'マップマーカーリスト追加',
        'lat'   : lat,
        'lng'   : lng,
        'form'  : MapInfoModelAdd(instance=obj),
    }
    return render(request,'webapp/create.html',modelform_dict)

def update(request,num):
    obj = MapInfoModel.objects.get(id=num)
    if (request.method == 'POST'):
        # info = MapInfoModelAdd(request.POST);
        # mapinfo = MapInfoModel()
        # mapinfo.name = request.POST['name']
        # mapinfo.genre = request.POST['genre']
        # mapinfo.location = request.POST['location']
        # mapinfo.lat = request.POST['lat']
        # mapinfo.lng = request.POST['lng']
        # mapinfo.photo = request.FILES['photo']
        # mapinfo.created_at = request.POST['created_at']
        # mapinfo.save()
        # return redirect(to='/')
        info = MapInfoModelAdd(request.POST,instance=obj)
        info.save()
        return redirect(to='/')
    update_dict = {
        'title' : 'マップマーカー編集画面',
        'id'    : num,
        'form'  : MapInfoModelAdd(instance=obj),
        'pred'  : pred(obj.photo.path),
    }
    return render(request,'webapp/update.html',update_dict)

def delete(request,num):
    obj = MapInfoModel.objects.get(id=num)
    if (request.method == 'POST'):
        obj.delete()
        return redirect(to='/')
    delete_dict = {
        'title' : 'マーカー登録削除画面',
        'id'    : num,
        'obj'   : obj,
    }
    return render(request,'webapp/delete.html',delete_dict)

