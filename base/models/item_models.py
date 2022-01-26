from django.db import models
from django.utils.crypto import get_random_string #ランダムな文字を生成する
import os

def created_id():
  return get_random_string(22)

def upload_image_to(instance, filename): #アイテムが作成されたとき
    item_id = instance.id
    return os.path.join('static', 'items', item_id, filename)

class Category(models.Model):
    slug = models.CharField(max_length=32, primary_key=True) #URLに表示するためidを変数に
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Item(models.Model): #Djangoが用意している、Modelを持ってきている
    id = models.CharField(default=create_id, primary_key=True, max_length=22, editable=False) #default=create_idにて上の関数を呼び出しランダムな数字をIDに入力する
    name = models.CharField(default='', max_length=50) #アイテム名 CharField＝少ない文字
    price = models.PositiveIntegerField(default=0) #価格 integerにする Positiveは0以下にしない処理
    stock = models.PositiveIntegerField(default=0) #在庫
    description = models.TextField(default='', blank=True) #説明 空文字でもいいようにblank=Trueの設定
    sold_count = models.PositiveIntegerField(default=0) #アイテムの販売数 いくら売れたのか管理する
    is_published = models.BooleanField(default=False) #管理画面でアイテムを作成 booleanで公開か下書き状態かにする
    created_at = models.DateTimeField(auto_now_add=True) #作成された日
    updated_at = models.DateTimeField(auto_now=True) #アイテムの情報が更新された日
    image = models.ImageField(default="", blank=True,upload_to=upload_image_to)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True) # models.SET_NULL 参照されるアイテムが消されるとアイテムを参照できなくなるため、nullにする

    def __str__(self):
        return self.name