from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)  # create a model

        user.set_password(password)  # Hashes the password
        user.save(using=self._db)  # Important to save to db

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email
# Create your models here.


class Category(models.Model):
    # Category(id, name)
    name = models.CharField(max_length=255)


class Person (models.Model):
    # Person (id, name, image, email,phone)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    image = models.TextField()

class Instructor(models.Model):
    # Insturctor(id, name, image, description, rate)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.TextField()

class Student(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

class Rate(models.Model):
    
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    rate = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

class Course(models.Model):
    # Course(id, category_id, name, details, price, updated_at, created_at, language)
    name = models.CharField(max_length=255)
    details = models.TextField()
    language = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    category_id = models.ForeignKey(Category, on_delete=CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    instructors = models.ManyToManyField(Instructor)
    students = models.ManyToManyField(Student)




class CourseImage(models.Model):
    # CourseImage(id, image_path, course_id, )
    image_path = models.TextField()
    course_id = models.ForeignKey(Course, on_delete=CASCADE)

class CourseVideo(models.Model):
    # CourseVideo(id, video_path, course_id, name, description,subtitle_path)
    image_path = models.TextField()
    description = models.TextField()
    subtitle_path = models.TextField()
    course_id = models.ForeignKey(Course, on_delete=CASCADE)
