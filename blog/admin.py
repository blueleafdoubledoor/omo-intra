from django.contrib import admin
from .models import Post

# Post モデルを admin ページで見れるように登録する
admin.site.register(Post)
