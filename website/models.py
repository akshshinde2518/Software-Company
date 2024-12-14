from django.db import models

# Create Your Model Here


class Feature(models.Model):
    feature_image = models.ImageField(upload_to='static/')
    feature_title = models.CharField(max_length=100)
    feature_details = models.TextField()

class About(models.Model):
    about_heading = models.CharField(max_length=100)
    about_details = models.TextField()
    about_image = models.ImageField(upload_to='static/')
    about_point_1_title = models.CharField(max_length=100)
    about_point_1_details = models.TextField()
    about_point_2_title = models.CharField(max_length=100)
    about_point_2_details = models.TextField()
    about_point_3_title = models.CharField(max_length=100)
    about_point_3_details = models.TextField()
    about_point_4_title = models.CharField(max_length=100)
    about_point_4_details = models.TextField()

class Counter(models.Model):
    counter_image = models.ImageField(upload_to='static/')
    count_1_title = models.CharField(max_length=100)
    count_1_value = models.IntegerField()
    count_2_title = models.CharField(max_length=100)
    count_2_value = models.IntegerField()
    count_3_title = models.CharField(max_length=100)
    count_3_value = models.IntegerField()
    count_4_title = models.CharField(max_length=100)
    count_4_value = models.IntegerField()

class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_details = models.TextField()
    service_image = models.ImageField(upload_to='static/')

class Challenge(models.Model):
    challenge_title = models.CharField(max_length=100)
    challenge_image = models.ImageField(upload_to='static/')
    challenge_1_title = models.CharField(max_length=100)
    challenge_1_details = models.TextField()
    challenge_2_title = models.CharField(max_length=100)
    challenge_2_details = models.TextField()
    challenge_3_title = models.CharField(max_length=100)
    challenge_3_details = models.TextField()
    challenge_4_title = models.CharField(max_length=100)
    challenge_4_details = models.TextField()

class Project(models.Model):
    project_image = models.ImageField(upload_to='static/')
    project_title = models.CharField(max_length=100)
    project_details = models.TextField()

class WhyChooseUs(models.Model):
    wcu_title = models.CharField(max_length=100)
    wcu_details = models.TextField()
    wcu_image = models.ImageField(upload_to='static/')

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_image = models.ImageField(upload_to='static/')
    client_position = models.CharField(max_length=100)
    client_review = models.TextField()

class Blog(models.Model):
    blog_image = models.ImageField(upload_to='static/')
    blog_sub_title = models.CharField(max_length=100)
    blog_title = models.CharField(max_length=100)
    blog_date = models.DateField()
    blog_details = models.TextField()

class Partner(models.Model):
    partner_logo = models.ImageField(upload_to='static/')

class Slider(models.Model):
    slider_subtitle = models.CharField(max_length=100)
    slider_title = models.CharField(max_length=100)
    slider_details = models.TextField()
    slider_image = models.ImageField(upload_to='static/')
    slider_video_link = models.URLField()

class Member(models.Model):
    member_name = models.CharField(max_length=100)
    member_position = models.CharField(max_length=100)
    member_image = models.ImageField(upload_to='static/' ,default=" ")


   
