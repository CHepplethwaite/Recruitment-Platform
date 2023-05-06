from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
import datetime
import uuid
from django.conf import settings


class job(models.Model):
    ACADEMIA = "EDU"
    ACCOUNTANCY = "ACC"
    ADMINISTRATION = "ADM"
    AGRICULTURE = "AGR"
    BANKING_AND_FINANCE = "BF"
    DEVELOPMENT = "DEV"
    ENGINEERING_AND_CONSTRUCTION = "ENG"
    HEALTH = "HTH"
    HUMAN_RESOURCE = "HR"
    ICT_AND_TELCO = "ICT"
    LAW = "LAW"
    MANUFACTURING_FMCG = "MAN"
    OTHER = "MISC"
    PUBLIC_SECTOR = "PUB"
    RETAIL_AND_SALES = "SAL"
    TRANSPORT_AND_LOGISTICS = "TRA"
    FULL_TIME = "FT"
    PART_TIME = "PT"
    CONTRACT = "CT"
    TEMPORARY = "TMP"
    INTERNSHIP = "INT"
    industry_choices = [
        ("ACADEMIA","Academia"),
        ("ACCOUNTANCY","Accountancy"),
        ("ADMINISTRATION","Administration"),
        ("AGRICULTURE","Agriculture"),
        ("BANKING_AND_FINANCE","Banking and Finance"),
        ("DEVELOPMENT","Development"),
        ("ENGINEERING_AND_CONSTRUCTION","Engineering and Construction"),
        ("HEALTH","Health"),
        ("HUMAN_RESOURCE","Human Resource"),
        ("ICT_AND_TELCO","ICT and Telco"),
        ("LAW","Law"),
        ("MANUFACTURING_FMCG","Manufacturing/FMCG"),
        ("OTHER","Other"),
        ("PUBLIC_SECTOR","Public Sector"),
        ("RETAIL_AND_SALES","Retail and Sales"),
        ("TRANSPORT_AND_LOGISTICS","Transport and Logistics"),
    ]
    approval_choices = [
        (True,"Approved"),
        (False,"Pending"),
    ]
    employment_choices = [
        ("FULL_TIME","Full-time"),
        ("PART_TIME","Part-time"),
        ("CONTRACT","Contract"),
        ("TEMPORARY","Temporary"),
        ("INTERSHIP","Internship"),
    ]
    status = models.BooleanField(choices=approval_choices,default=False)
    employment_type = models.CharField(
        choices=employment_choices,
        default=FULL_TIME,
        max_length=15,
        )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.CharField(max_length=50)
    url = models.URLField(max_length=200, default="www.tumpetech.com")
    email = models.EmailField(default = 'info@tumpetech.com')
    job_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=False, unique_for_date='post_date', default="")
    post_date = models.DateField(auto_now=False, auto_now_add=True)
    closing_date = models.DateField()
    location = models.CharField(max_length=50)
    details = models.TextField()
    industry = models.CharField(choices=industry_choices,
                                max_length=30,
                                default=ACADEMIA,
                                )

    def __str__(self):
        return self.job_title+" - "+self.company
        
    def get_absolute_url(self):
        return reverse("job_detail", kwargs={'uuid':self.id,"slug": self.slug})

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
        delta =  (todays_date - post_date1).days - 0
        return delta
    
    @property
    def posted_today(self):
        today = datetime.date.today()
        margin = datetime.timedelta(days = 1)
        return today - margin <= self.post_date <= today + margin