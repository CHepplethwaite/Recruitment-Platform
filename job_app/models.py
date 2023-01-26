from django.db import models

class job(models.Model):
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    post_date = models.DateField(auto_now=False, auto_now_add=True)
    closing_date = models.DateField()
    location = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return self.job_title+" - "+self.company