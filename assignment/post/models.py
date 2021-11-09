from django.db.models import Model, DateTimeField, CharField, ForeignKey, CASCADE
from django.contrib.auth.models import User

class Post(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    text = CharField(max_length=500, blank=True)
    created_at = DateTimeField(auto_now_add=True, editable=False)
    updated_at = DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


