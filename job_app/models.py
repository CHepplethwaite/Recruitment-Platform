from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
import datetime
import uuid


class job(models.Model):
    ACCOUNTANCY = "ACC"
    ADMINISTRATION = "ADM"
    BANKING_AND_FINANCE = "BF"
    DEVELOPMENT = "DEV"
    EDUCATION = "EDU"
    ENGINEERING_AND_CONSTRUCTION = "ENG"
    HEALTH = "HTH"
    HUMAN_RESOURCE = "HR"
    ICT_AND_TELECO = "ICT"
    LEGAL = "LG"
    MANUFACTURING_FMCG = "MAN"
    OTHER = "MISC"
    PUBLIC_SECTOR = "PUB"
    RETAIL_AND_SALES = "SAL"
    TRANSPORT_AND_LOGISTICS = "TRA"
    industry_choices = [
        ("ACCOUNTACY","Accountancy"),
        ("ADMINISTARTION","Administration"),
        ("AGRICULTURE","Agriculture"),
        ("BANKING_AND_FINANCE","Banking and Finance"),
        ("DEVELOPMENT","Development"),
        ("EDUCATION","Education"),
        ("ENGINEERING_AND_CONSTRUCTION","Engineering and Construction"),
        ("HEALTH","Health"),
        ("HUMAN_RESOURCE","Human Resource"),
        ("ICT_AND_TELECO","ICT and Telco"),
        ("LEGAL","Legal"),
        ("MANUFACTURING_FMCG","Manufacturing/FMCG"),
        ("OTHER","Other"),
        ("PUBLIC_SECTOR","Public Sector"),
        ("RETAIL_AND_SALES","Retail and Sales"),
        ("TRANSPORT_AND_LOGISTICS","Transport and Logistics"),
    ]
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=False, unique_for_date='post_date', default="")
    post_date = models.DateField(auto_now=False, auto_now_add=True)
    closing_date = models.DateField()
    location = models.CharField(max_length=50)
    details = models.TextField()
    industry = models.CharField(choices=industry_choices,
                                max_length=255,
                                default=ACCOUNTANCY,
                                )

    def __str__(self):
        return self.job_title+" - "+self.company
        
    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"slug": self.slug})

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug  = slugify(self.job_title+" - "+self.company)
        return super().save(*args,**kwargs)
    
    @property
    def is_closed(self):
        return datetime.date.today() > self.closing_date
    
    @property
    def closing_soon(self):
        today = datetime.date.today()
        margin = datetime.timedelta(days = 1)
        return today - margin <= self.closing_date <= today + margin
    
    @property
    def get_x_days_ago(self):
        today = str(datetime.date.today())
        post_date = str(self.post_date)
        todays_date = datetime.datetime.strptime(today, "%Y-%m-%d").date()
        post_date1 = datetime.datetime.strptime(post_date, "%Y-%m-%d").date()
        delta =  (todays_date - post_date1).days - 1
        return delta
    

    
