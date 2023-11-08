from django.db import models
from django.db.models.query import QuerySet
#Import the timezone to determine the time of the user's system
from django.utils import timezone

#Import the User from the authentication module in order to access system users
from django.contrib.auth.models import User

#CANONICAL URL, FOR RE-USING A URL WITH ALTERNATING PARAMETERS
from django.urls import reverse

#Implement the Tagging Manager
from taggit.managers import TaggableManager

#Objects is the default manager of every model that handles all CRUD Operations
"""
IT MAKES SENSE TO DEVELOP A SEPERATE MANAGER TO HANDLE ONLY THE PUBLISHED CALLS

1. YOU COULD ADD EXTRA MANAGER METHODS TO AN EXISTING MANAGER 
2. YOU COULD CREATE A NEW MANAGER BY MODIFYING THE INITIAL QUERYSET THAT THE MANAGER RETURNS

IN THIS CASE WE WILL USE OPTION 2
""" 

#OUR CUSTOM OBJECT MANAGER
class PublishedArticlesManager(models.Manager):
    def get_queryset(self):
        return super(PublishedArticlesManager, self).get_queryset().filter(status='published')

#Hold the Posted Articles
class Article(models.Model):
    #CREATE A TUPLE TO HOST THE Published and drafted versions
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    #Create the title for the article
    title = models.CharField(max_length=250)
    #Url Slug
    slug = models.SlugField(max_length=250)
    #Get the name of the author
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='article_posts')
    #Create the textArea for collecting the names
    body = models.TextField()
    #Time when the article is published
    publish = models.DateTimeField(default=timezone.now)
    #TIME THE ARTICLE IS CREATED
    created = models.DateTimeField(auto_now_add=True)
     #Updated
    updated = models.DateTimeField(auto_now=True)
    #Set the default status
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
   

    
    # DEFAULT MANAGER
    objects = models.Manager()

    # OUR CUSTOM
    publishedArticles = PublishedArticlesManager()
    
    #Instantiate the Manager
    tags = TaggableManager()
    """
            TAGS MANAGER ALLOWS
    1. Add
    2. Retrieve
    3. Remove Tags from Objects
    
    """

    #Call the specific post 
    def get_absolute_url(self):
        return reverse("newsApp:article_details", 
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug
                             ]
                       )
    

    #Create a meta class that contains the metadata for the model
    class Meta:
        #Sort the Articles by descending order, hence the negative prefix
        ordering = ('-publish',)

    #Create the method that will return the specific information that we will need
    def __str__(self) -> str:
        return self.title

#Hold the Comment System
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self) -> str:
        return f'Comment by {self.name} on {self.article}'


