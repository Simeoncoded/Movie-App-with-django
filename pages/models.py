from django.db import models

# Create your models here.


class Categorie(models.Model):
    name  = models.CharField(max_length=20)

    def __str__(self):
        return self.name

movies_choices=(('Action','Action'),('Horror','horror'),('Thriller','Thriller'))

class Film(models.Model):
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    tags=models.CharField(choices=movies_choices,max_length=20)
    R_rating=models.CharField(max_length=20)
    Description=models.TextField()
    image_url=models.ImageField(null=True,blank=True)
    is_series=models.BooleanField(default=True)
    movie_rating=models.CharField(max_length=30,null=True)
    running_time=models.CharField(max_length=30,null=True)
    release_year=models.CharField(max_length=30,null=True)
    country=models.CharField(max_length=30,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name+" "+ str(self.is_series)

class Season(models.Model):
    film=models.ForeignKey('Film',on_delete=models.CASCADE)
    description=models.TextField()
    season_number=models.CharField(max_length=200)

    def __str__(self):
        return self.film.name+" season "+self.season_number

class Episode(models.Model):
    season=models.ForeignKey('Season',on_delete=models.CASCADE)
    description=models.TextField()
    episode_number=models.CharField(max_length=200)
    episode_name=models.CharField(max_length=200,null=True)
    episode_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.season.film.name+ " episode "+ self.episode_number