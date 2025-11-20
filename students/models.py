from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    YEAR_CHOICES = [
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    ]
    
    DEPARTMENT_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EC', 'Electronics & Communication'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
    ]
    
    # Link to Django's built-in User model for authentication
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Student Information Fields (10+ fields)
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES)
    year_of_study = models.CharField(max_length=1, choices=YEAR_CHOICES)
    enrollment_date = models.DateField(auto_now_add=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(validators=[phone_regex], max_length=17)
    # profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    profile_picture = models.CharField(max_length=200, null=True, blank=True, help_text="Profile picture path")
    
    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['student_id']