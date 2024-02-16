from django.db import models
from products.models import TagModel

# Create your models here.

class AuthorModel(models.Model):
    full_name = models.CharField(max_length=36)
    avatar = models.ImageField(upload_to="posts/authors")
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class PostModel(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    short_description = models.TextField()
    image = models.ImageField(upload_to="posts/")
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagModel)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_previous(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class CommentModel(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    text = models.TextField()
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name="comments")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.post.title} | {self.name} | {self.text}"
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"