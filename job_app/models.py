from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
import datetime
import uuid
from django.conf import settings


class job(models.Model):
    #Job categories
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

    #Job type
    FULL_TIME = "FT"
    PART_TIME = "PT"
    CONTRACT = "CT"
    TEMPORARY = "TMP"
    INTERNSHIP = "INT"

    #Provinces
    CENTRAL = "CP"
    COPPERBELT = "CB"
    EASTERN = "EP"
    LUAPULA = "LP"
    LUSAKA_P = "LSKP"
    NORTHERN = "NP"
    NORTH_WESTERN = "NW"
    MUCHINGA = "MP"
    WESTERN ="WP"
    SOUTHERN = "SP"

    #Towns
    LUSAKA = "LSK"
    KITWE = "KT"
    NDOLA = "ND"
    KABWE = "KB"
    CHINGOLA = "CHG"
    MUFULIRA = "MF"
    LIVINGSTONE = 'LS'
    LUANSHYA = "LN"
    KASAMA = "KS"
    CHIPATA = "CHT"
    CHADIZA = "CHD"
    CHAMA = "CHM"
    CHANDESI = "CHND"
    CHAVUMA = "CHV"
    CHEMBE = "CHMB"
    CHIBOMBO = "CHIB"
    CHIENGI = "CHIE"
    CHILUBI = "CHIL"
    CHILILABOMBWE = "CHLI"
    CHINSALI = "CHNS"
    CHINYINGI =  "CHNY"
    CHIRUNDU = "CHR"
    CHISAMBA = "CHS"
    CHOMA = "CHMA"
    GWEMBE = "GW"
    ISOKA = "IS"
    KABOMPO = "KB"
    KAFUE = "KF"
    KAFULWE = "KFL"
    KALABO = "KLB"
    KALENE = "KH"
    KALOMO = "KL"
    KALULUSHI = "KLSH"
    KANYEMBO = "KNY"
    KAOMA = "KMA"
    KAPIRI = "KP"
    KASEMPA = "KSP"
    KASHIKISHI = "KSHK"
    KATABA = "KTB"
    KATETE = "KTT"
    KAWAMBWA = "KW"
    KAZEMBE = "KZ" #Mwansabombwe
    KAZUNGULA = "KZG"
    KIBOMBOMENE = "KIB"
    LUANGWA = "LG"
    LUFWANYAMA = "LF"
    LUKULU = "LK"
    LUNDAZI = "LD"
    MACHA = "MC"
    MAKENI = "MK"
    MANSA = "MN"
    MAZABUKA = "MZ"
    MBALA = "MB"
    MBERESHI = "MBE"
    MFUWE = "MF"
    MILENGE =  "ML"
    MISISI = "MIS"
    MKUSHI = "MKS"
    MONGU = "MG"
    MONZE = "MON"
    MPIKA = "MPK"
    MPOROKOSO = "MPO"
    MPULUNGU = "MPL"
    MUMBWA = "MUM"
    MUYOMBE = "MUY"
    MWINILUNGA = "MWI"
    NCHELENGE = "NCH"
    NGOMA = "NGO"
    NKANA = "NK"
    NSELUKA = "NS"
    PEMBA = "PM"
    PETAUKE = "PT"
    SAMFYA = "SM"
    SENANGA = "SEN"
    SERENJE = "SER"
    SESHEKE = "SESH"
    SHIWANG_ANDU = "SHN"
    SIAVONGA = "SV"
    SIKALONGO = "SK"
    SINAZONGWE = "SNZ"
    SOLWEZI = "SOL"
    VENTURE = "VN"
    ZAMBEZI = "ZMB"
    ZIMBA = "ZMB"

    #Copperbelt districts
    CHILILABOMBWE_D = "CHLD"
    CHINGOLA_D = "CHGD"
    KALULUSHI_D = "KALD"
    KITWE_D = "KTD"
    LUANSHYA_D = "LSHD"
    LUFWANYAMA_D = "LFD"
    MASAITI_D = "MSD"
    MPONGWE_D = "MPG"
    MUFULIRA_D = "MFD"
    NDOLA_D = "NDL"

    #Eastern districts 
    CHADIZA_D = "CHAD"
    CHAMA_D = "CHMD"
    CHASEFU_D = "CHSD"
    CHIPANGALI_D = "CHPD"
    CHIPATA_D = "CHTD"
    KASENENGWA_D = "KSND"
    KATETE_D = "KATD"
    LUMEZI_D = "LMD"
    LUNDAZI_D = "LND"
    LUSANGAZI_D = "LSGD"
    MAMBWE_D = "MAMD"
    NYIMBA_D = "NYD"
    PETAUKE_D = "PTD"
    SINDA_D = "SND"
    VUBWI = "VBD"

    #Luapula districts
    CHEMBE_D = "CHBD"
    CHIENGI_D = "CHID"
    CHIFUNABULI_D = "CHFD"
    CHIPILI_D = "CPD" 
    KAWAMBWA_D = "KWD"
    LUNGA_D = "LNGD"
    MANSA_D = "MAND"
    MILENGE_D = "MILD"
    MWANSABOMBWE_D = "MWND"
    MWENSE_D = "MWED"
    NCHEKENGE_D = "NCHD"
    SAMFYA_D = "SAMD"

    #Lusaka districts
    CHILANGA_D = "CHLD"
    CHONGWE_D = "CHND"
    KAFUE_D = "KAFD"
    LUANGWA_D = "LUGD"
    LUSAKA_D = "LSKD"
    RUFUNSA_D = "RFD"

    #Muchinga districts
    CHINSALI_D = "CSLD"
    ISOKA_D = "ISD"
    KANCHIBIYA_D = "KD"
    LAVUSHIMANDA_D = "LVD"
    MAFINGA_D = "MFD"
    MPIKA_D = "MPKD"
    NAKONDE_D = "NKD"
    SHIWANG_ANDU_D = "SHGD"

    #Northern districts
    CHILUBI_D = "CHBD"
    KAPUTA_D = "KPTD"
    KASAMA_D = "KSMD"
    LUNTE_D = "LNTD"
    LUPOSOSHI_D = "LPD"
    LUWINGU_D = "LWD"
    MBALA_D = "MBLD"
    MPOROKOSO_D = "MPOD"
    MPULUNDU_D = "MPUD"
    MUNGWI_D = "MGWD"
    NSAMA = "NSMD"
    SENGA_D = "SND"

    #North-western districts
    CHAVUMA_D = "CHVD"
    IKELENGE_D = "IKED"
    KABOMPO_D = "KABD"
    KASEMPA_D = "KASD"
    KALUMBILA_D = "KLBD"
    MANYINGA_D = "MNYD"
    MUFUMBWE_D = "MFBD"
    MUSHINDAMO_D = "MUSH"
    MWINILUNGA_D = "MWID"
    SOLWEZI_D = "SOLWD"
    ZAMBEZI_D = "ZMBZD"

    #Southern province districts
    CHIKANKATA_D = "CHIKD"
    CHIRUNDU_D = "CHIRD"
    CHOMA_D = "CHMD"
    GWEMBE_D = "GWEMD"
    ITEZHI_TEZHI_D = "ITZHD"
    KALOMO_D = "KLOD"
    KAZUNGULA_D = "KZNGD"
    LIVINGSTONE_D = "LSTND"
    MAZABUKA_D = "MZBKD"
    MONZE_D = "MNEZD"
    NAMWALA_D = "NAMD"
    PEMBA_D = "PMBD"
    SIAVONGA_D = "SVNGD"
    SINAZONGWE_D = "SNZWD"
    ZIMBA_D = "ZMBD"

    #Western province districts
    KALABO_D = "KLBOD"
    KAOMA_D = "KOMAD"
    LIMULUNGA_D = "LMGAD"
    LUAMPA_D = "LMPD"
    LUKULU_D = "LKUD"
    MITETE_D = "MTTD"
    MONGU_D = "MONGD"
    MULOBEZI_D = "MLBZD"
    MWANDI_D = "MNDD"
    NALOLO_D = "NLLD"
    NKEYEMA_D = "NKYMD"
    SENANGA_D = "SENGD"
    SESHEKE_D = "SSHKD"
    SHANG_OMBO_D = "SHNBD"
    SIKONGO_D = "SKGO"
    SIOMA_D = "SIOMD"
 
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
    province_choices = [
        ("CENTRAL","Central"),
        ("COPPERBELT","Copperbelt"),
        ("EASTERN","Eastern"),
        ("LUAPULA","Luapula"),
        ("LUSAKA_P","Lusaka"),
        ("NORTHERN","Northern"),
        ("NORTH_WESTERN","North Western"),
        ("MUCHINGA","Muchinga"),
        ("WESTERN","Western"),
        ("SOUTHERN","Southern"),
    ]

    towns_choices = [
        ("LUSAKA","Lusaka"),
        ("KITWE","Kitwe"),
        ("NDOLA","Ndola"),
        ("KABWE","Kabwe"),
        ("CHINGOLA","Chingola"),
        ("MUFULIRA","Mufulira"),
        ("LIVINGSTONE","Livingstone"),
        ("LUANSHYA","Luanshya"),
        ("KASAMA","Kasama"),
        ("CHIPATA","Chipata"),
        ("CHADIZA","Chadiza"),
        ("CHAMA","Chama"),
        ("CHANDESI","Chandesi"),
        ("CHAVUMA","Chavuma"),
        ("CHEMBE","Chembe"),
        ("CHIBOMBO","Chibombo"),
        ("CHIENGI","Chiengi"),
        ("CHILUBI","Chilubi"),
        ("CHILILABOMBWE","Chililabombwe"),
        ("CHINSALI","Chinsali"),
        ("CHINYINGI","Chinyingi"),
        ("CHIRUNDU","Chirundu"),
        ("CHISAMBA","Chisamba"),
        ("CHOMA","Choma"),
        ("GWEMBE","Gwembe"),
        ("ISOKA","Isoka"),
        ("KABOMPO","Kabompo"),
        ("KAFUE","Kafue"),
        ("KAFULWE","Kafulwe"),
        ("KALABO","Kalabo"),
        ("KALENE","Kalene Hills"),
        ("KALOMO","Kalomo"),
        ("KALULUSHI","Kalulushi"),
        ("KANYEMBO","Kanyembo"),
        ("KAOMA","Kaoma"),
        ("KAPIRI","Kapiri Mposhi"),
        ("KASEMPA","Kasempa"),
        ("KASHIKISHI","Kashikishi"),
        ("KATABA","Kataba"),
        ("KATETE","Katete"),
        ("KAWAMBWA","Kawambwa"),
        ("KAZEMBE","Kazembe"),
        ("KAZUNGULA","Kazungula"),
        ("KIBOMBOBENE","Kibombomene"),
        ("LUANGWA","Luangwa"),
        ("LUFWANYAMA","Lufwanyama"),
        ("LUKULU","Lukulu"),
        ("LUNDAZI","Lundazi"),
        ("MACHA","Macha"),
        ("MAKENI","Makeni"),
        ("MANSA","Mansa"),
        ("MAZABUKA","Mazabuka"),
        ("MBALA","Mbala"),
        ("MBERESHI","Mbereshi"),
        ("MFUWE","Mfuwe"),
        ("MILENGE","Milenge"),
        ("MISISI","Misisi"),
        ("MKUSHI","Mkushi"),
        ("MONGU","Mongu"),
        ("MONZE","Monze"),
        ("MPIKA","Mpika"),
        ("MPOROKOSO","Mporokoso"),
        ("MPULUNGU","Mpulungu"),
        ("MUMBWA","Mumbwa"),
        ("MUYOMBE","Muyombe"),
        ("MWINILUNGA","Mwinilunga"),
        ("NCHELENGE","Nchelenge"),
        ("NGOMA","Ngoma"),
        ("NKANA","Nkana"),
        ("NSELUKA","Nseluka"),
        ("PEMBA","Pemba"),
        ("PETAUKE","Petauke"),
        ("SAMFYA","Samfya"),
        ("SENANGA","Senanga"),
        ("SERENJE","Serenje"),
        ("SESHEKE","Sesheke"),
        ("SHIWANG_ANGU","Shiwang'andu"),
        ("SIAVONGA","Siavonga"),
        ("SIKALONGO","Sikalongo"),
        ("SINAZONGWE","Sinazongwe"),
        ("SOLWEZI","Solwezi"),
        ("VENTURE","Venture"),
        ("ZAMBEZI","Zambezi"),
        ("ZIMBA","Zimba"),
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
    company = models.CharField(max_length=50)
    url = models.URLField(max_length=200, default="www.tumpetech.com")
    email = models.EmailField(default = 'info@tumpetech.com')
    job_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=False, unique_for_date='post_date', default="")
    post_date = models.DateField(auto_now=False, auto_now_add=True)
    closing_date = models.DateField()
    location = models.CharField(choices=towns_choices,
                                max_length=30,
                                default=LUSAKA,
                                )
    details = models.TextField()
    province = models.CharField(choices=province_choices,
                                max_length=30,
                                default=LUSAKA_P,
                                )
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