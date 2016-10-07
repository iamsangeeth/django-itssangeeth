from django.db import models
from django.utils import timezone

TAG_COLOR_CHOICE = (
    ('bg-red', 'red'),
    ('bg-yellow', 'yellow'),
    ('bg-aqua', 'aqua'),
    ('bg-blue', 'blue'),
    ('bg-light blue', 'light-blue'),
    ('bg-green', 'green'),
    ('bg-navy', 'navy'),
    ('bg-teal', 'teal'),
    ('bg-olive', 'olive'),
    ('bg-lime', 'lime'),
    ('bg-orange', 'orange'),
    ('bg-fuchsia', 'fuchsia'),
    ('bg-purple', 'purple'),
    ('bg-maroon', 'maroon'),
    ('bg-black', 'black'),
    ('bg-red-archive', 'red-active'),
    ('bg-yellow-active', 'yellow-active'),
    ('bg-aqua-active', 'aqua-active'),
    ('bg-blue-active', 'blue-active'),
    ('bg-light-blue-active', 'light-blue-active'),
    ('bg-green-active', 'green-active'),
    ('bg-navy-active', 'navy-active'),
    ('bg-teal-active', 'teal-active'),
    ('bg-olive-active', 'olive-active'),
    ('bg-lime-active', 'lime-active'),
    ('bg-orange-active', 'orange-active'),
    ('bg-fuchsia-active', 'fuchsia-active'),
)
# Create your models here.
class Posts(models.Model):
    def save(self, *args, **kwargs):
        self.post_url = self.post_default()
        super(Posts, self).save(*args, **kwargs)

    def post_default(self):
        s = self.post_head
        return s.replace(" ","-")


    post_id = models.AutoField(
        primary_key=True,
    )
    post_url = models.CharField(
        max_length=50,
        default=False,
    )
    post_head = models.CharField(
        max_length=50,
        default=False,
    )
    post_text = models.TextField(
        max_length=5000,
        default=False,
    )
    post_created_on = models.DateTimeField(
        default=timezone.now,
    )
    post_likes = models.IntegerField(
        default= 0,
    )
    post_views = models.IntegerField(
        default=0,
    )
    post_shares = models.IntegerField(
        default=0,
    )

    class Meta:
        ordering = ['-post_created_on']

    def __str__(self):
        return self.post_head

class Comments(models.Model):
    post_commented = models.ForeignKey(Posts, blank=True, null=True)
    commented_by = models.CharField(max_length=40,default=False)
    commented_on = models.DateTimeField(default=timezone.now)
    commenter_mail_id = models.EmailField(max_length=40,default=False)
    comment_text=models.CharField(max_length=300,default=False)

    class Meta:
        ordering = ['-commented_on']

    def __str__(self):
        return str(self.post_commented.post_id) +  str(self.comment_text)

class Tagging(models.Model):
    post_of_tag = models.ForeignKey(Posts,blank=True,null=True)
    name_of_tag = models.CharField(max_length=30)
    color_choice=models.CharField(max_length=30,choices=TAG_COLOR_CHOICE,default='.bg-red')

    def __str__(self):
        return str(self.post_of_tag.post_head) + str(self.name_of_tag)