from django.db import models
from django.urls import reverse
import datetime
from django.conf import settings
from PIL import Image
from ckeditor.fields import RichTextField


class job(models.Model):
    #Job categories
    OTHER = "OTH"
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
    NA = "N/A"
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

    #Copperbelt locations
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

    #Eastern locations 
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
    VUBWI_D = "VBD"

    #Luapula locations
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

    #Lusaka locations
    CHILANGA_D = "CHLD"
    CHONGWE_D = "CHND"
    KAFUE_D = "KAFD"
    LUANGWA_D = "LUGD"
    LUSAKA_D = "LSKD"
    RUFUNSA_D = "RFD"

    #Muchinga locations
    CHINSALI_D = "CSLD"
    ISOKA_D = "ISD"
    KANCHIBIYA_D = "KD"
    LAVUSHIMANDA_D = "LVD"
    MAFINGA_D = "MFD"
    MPIKA_D = "MPKD"
    NAKONDE_D = "NKD"
    SHIWANG_ANDU_D = "SHGD"

    #Northern locations
    CHILUBI_D = "CHLBD"
    KAPUTA_D = "KPTD"
    KASAMA_D = "KSMD"
    LUNTE_D = "LNTD"
    LUPOSOSHI_D = "LPD"
    LUWINGU_D = "LWD"
    MBALA_D = "MBLD"
    MPOROKOSO_D = "MPOD"
    MPULUNGU_D = "MPUD"
    MUNGWI_D = "MGWD"
    NSAMA = "NSMD"
    SENGA_D = "SND"

    #North-western locations
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

    #Southern province locationspip install crispy-bootstrap5
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

    #Western province locations
    KALABO_D = "KLBOD"
    KAOMA_D = "KOMAD"
    LIMULUNGA_D = "LMGAD"
    LUAMPA_D = "LMPD"
    LUKULU_D = "LUKUD"
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
 
    country_choices = [
    ('US', 'United States'),
    ('AF', 'Afghanistan'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AS', 'American Samoa'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AI', 'Anguilla'),
    ('AQ', 'Antarctica'),
    ('AG', 'Antigua And Barbuda'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AW', 'Aruba'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'),
    ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Belarus'),
    ('BE', 'Belgium'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivia'),
    ('BA', 'Bosnia And Herzegowina'),
    ('BW', 'Botswana'),
    ('BV', 'Bouvet Island'),
    ('BR', 'Brazil'),
    ('BN', 'Brunei Darussalam'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('KH', 'Cambodia'),
    ('CM', 'Cameroon'),
    ('CA', 'Canada'),
    ('CV', 'Cape Verde'),
    ('KY', 'Cayman Islands'),
    ('CF', 'Central African Rep'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CX', 'Christmas Island'),
    ('CC', 'Cocos Islands'),
    ('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CG', 'Congo'),
    ('CK', 'Cook Islands'),
    ('CR', 'Costa Rica'),
    ('CI', 'Cote D`ivoire'),
    ('HR', 'Croatia'),
    ('CU', 'Cuba'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DK', 'Denmark'),
    ('DJ', 'Djibouti'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('TP', 'East Timor'),
    ('EC', 'Ecuador'),
    ('EG', 'Egypt'),
    ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'),
    ('ER', 'Eritrea'),
    ('EE', 'Estonia'),
    ('ET', 'Ethiopia'),
    ('FK', 'Falkland Islands (Malvinas)'),
    ('FO', 'Faroe Islands'),
    ('FJ', 'Fiji'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('GF', 'French Guiana'),
    ('PF', 'French Polynesia'),
    ('TF', 'French S. Territories'),
    ('GA', 'Gabon'),
    ('GM', 'Gambia'),
    ('GE', 'Georgia'),
    ('DE', 'Germany'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GR', 'Greece'),
    ('GL', 'Greenland'),
    ('GD', 'Grenada'),
    ('GP', 'Guadeloupe'),
    ('GU', 'Guam'),
    ('GT', 'Guatemala'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-bissau'),
    ('GY', 'Guyana'),
    ('HT', 'Haiti'),
    ('HN', 'Honduras'),
    ('HK', 'Hong Kong'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JP', 'Japan'),
    ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'),
    ('KI', 'Kiribati'),
    ('KP', 'Korea (North)'),
    ('KR', 'Korea (South)'),
    ('KW', 'Kuwait'),
    ('KG', 'Kyrgyzstan'),
    ('LA', 'Laos'),
    ('LV', 'Latvia'),
    ('LB', 'Lebanon'),
    ('LS', 'Lesotho'),
    ('LR', 'Liberia'),
    ('LY', 'Libya'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('MO', 'Macau'),
    ('MK', 'Macedonia'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),
    ('MY', 'Malaysia'),
    ('MV', 'Maldives'),
    ('ML', 'Mali'),
    ('MT', 'Malta'),
    ('MH', 'Marshall Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),
    ('MU', 'Mauritius'),
    ('YT', 'Mayotte'),
    ('MX', 'Mexico'),
    ('FM', 'Micronesia'),
    ('MD', 'Moldova'),
    ('MC', 'Monaco'),
    ('MN', 'Mongolia'),
    ('MS', 'Montserrat'),
    ('MA', 'Morocco'),
    ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),
    ('NP', 'Nepal'),
    ('NL', 'Netherlands'),
    ('AN', 'Netherlands Antilles'),
    ('NC', 'New Caledonia'),
    ('NZ', 'New Zealand'),
    ('NI', 'Nicaragua'),
    ('NE', 'Niger'),
    ('NG', 'Nigeria'),
    ('NU', 'Niue'),
    ('NF', 'Norfolk Island'),
    ('MP', 'Northern Mariana Islands'),
    ('NO', 'Norway'),
    ('OM', 'Oman'),
    ('PK', 'Pakistan'),
    ('PW', 'Palau'),
    ('PA', 'Panama'),
    ('PG', 'Papua New Guinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Peru'),
    ('PH', 'Philippines'),
    ('PN', 'Pitcairn'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('PR', 'Puerto Rico'),
    ('QA', 'Qatar'),
    ('RE', 'Reunion'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('RW', 'Rwanda'),
    ('KN', 'Saint Kitts And Nevis'),
    ('LC', 'Saint Lucia'),
    ('VC', 'St Vincent/Grenadines'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'Sao Tome'),
    ('SA', 'Saudi Arabia'),
    ('SN', 'Senegal'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leone'),
    ('SG', 'Singapore'),
    ('SK', 'Slovakia'),
    ('SI', 'Slovenia'),
    ('SB', 'Solomon Islands'),
    ('SO', 'Somalia'),
    ('ZA', 'South Africa'),
    ('ES', 'Spain'),
    ('LK', 'Sri Lanka'),
    ('SH', 'St. Helena'),
    ('PM', 'St.Pierre'),
    ('SD', 'Sudan'),
    ('SR', 'Suriname'),
    ('SZ', 'Swaziland'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('SY', 'Syrian Arab Republic'),
    ('TW', 'Taiwan'),
    ('TJ', 'Tajikistan'),
    ('TZ', 'Tanzania'),
    ('TH', 'Thailand'),
    ('TG', 'Togo'),
    ('TK', 'Tokelau'),
    ('TO', 'Tonga'),
    ('TT', 'Trinidad And Tobago'),
    ('TN', 'Tunisia'),
    ('TR', 'Turkey'),
    ('TM', 'Turkmenistan'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),
    ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'),
    ('UK', 'United Kingdom'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VU', 'Vanuatu'),
    ('VA', 'Vatican City State'),
    ('VE', 'Venezuela'),
    ('VN', 'Viet Nam'),
    ('VG', 'Virgin Islands (British)'),
    ('VI', 'Virgin Islands (U.S.)'),
    ('EH', 'Western Sahara'),
    ('YE', 'Yemen'),
    ('YU', 'Yugoslavia'),
    ('ZR', 'Zaire'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabwe'),
    ]
    
    industry_choices = [
        ("OTHER","Other"),
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
        ("PUBLIC_SECTOR","Public Sector"),
        ("RETAIL_AND_SALES","Retail and Sales"),
        ("TRANSPORT_AND_LOGISTICS","Transport and Logistics"),
    ]
    approval_choices = [
        (True,"Approved"),
        (False,"Pending"),
    ]
    employment_choices = [
        ("N/A","n/a"),
        ("FULL_TIME","Full-time"),
        ("PART_TIME","Part-time"),
        ("CONTRACT","Contract"),
        ("TEMPORARY","Temporary"),
        ("INTERSHIP","Internship"),
    ]


    location_choices = [
        ("N/A","n/a"),
        ("CHADIZA", "Chadiza"),
        ("CHAMA", "Chama"),
        ("CHANDESI", "Chandesi"),
        ("CHAVUMA", "Chavuma"),
        ("CHEMBE", "Chembe"),
        ("CHIBOMBO", "Chibombo"),
        ("CHIENGI", "Chiengi"),
        ("CHILANGA","Chilanga"),
        ("CHILUBI", "Chilubi"),
        ("CHILILABOMBWE", "Chililabombwe"),
        ("CHINGOLA", "Chingola"),
        ("CHIPATA", "Chipata"),
        ("CHINSALI", "Chinsali"),
        ("CHINYINGI", "Chinyingi"),
        ("CHIRUNDU", "Chirundu"),
        ("CHISAMBA", "Chisamba"),
        ("CHOMA", "Choma"),
        ("CHONGWE","Chongwe"),
        ("GWEMBE", "Gwembe"),
        ("IKELENGE","Ikelenge"),
        ("ISOKA", "Isoka"),
        ("ITEZHI","Itezhi Tezhi"),
        ("KABOMPO", "Kabompo"),
        ("KABWE", "Kabwe"),
        ("KAFUE", "Kafue"),
        ("KAFULWE", "Kafulwe"),
        ("KALABO", "Kalabo"),
        ("KALOMO", "Kalomo"),
        ("KALULUSHI", "Kalulushi"),
        ("KANYEMBO", "Kanyembo"),
        ("KAOMA", "Kaoma"),
        ("KAPIRI", "Kapiri Mposhi"),
        ("KAPUTA","Kaputa"),
        ("KASAMA", "Kasama"),
        ("KASEMPA", "Kasempa"),
        ("KASHIKISHI", "Kashikishi"),
        ("KATABA", "Kataba"),
        ("KATETE", "Katete"),
        ("KAWAMBWA", "Kawambwa"),
        ("KAZEMBE", "Kazembe"),
        ("KAZUNGULA", "Kazungula"),
        ("KIBOMBOBENE", "Kibombomene"),
        ("KITWE", "Kitwe"),
        ("LIVINGSTONE", "Livingstone"),
        ("LUANSHYA", "Luanshya"),
        ("LUANGWA", "Luangwa"),
        ("LUFWANYAMA", "Lufwanyama"),
        ("LUKULU", "Lukulu"),
        ("LUNDAZI", "Lundazi"),
        ("LUSAKA", "Lusaka"),
        ("LUWINGU","Luwingu"),
        ("MACHA", "Macha"),
        ("MAFINGA","Mafinga"),
        ("MAKENI", "Makeni"),
        ("MAMBWE","Mambwe"),
        ("MANSA", "Mansa"),
        ("MASAITI","Masaiti"),
        ("MAZABUKA", "Mazabuka"),
        ("MBALA", "Mbala"),
        ("MBERESHI", "Mbereshi"),
        ("MFUWE", "Mfuwe"),
        ("MILENGE", "Milenge"),
        ("MISISI", "Misisi"),
        ("MKUSHI", "Mkushi"),
        ("MONGU", "Mongu"),
        ("MONZE", "Monze"),
        ("MPIKA", "Mpika"),
        ("MPONGWE","Mpongwe"),
        ("MPOROKOSO", "Mporokoso"),
        ("MPULUNGU", "Mpulungu"),
        ("MUFULIRA", "Mufulira"),
        ("MUFUMBWE","Mufumbwe"),
        ("MUMBWA", "Mumbwa"),
        ("MUNGWI","Mungwi"),
        ("MWENSE","Mwense"),
        ("MUYOMBE", "Muyombe"),
        ("MWINILUNGA", "Mwinilunga"),
        ("NAKONDE","Nakonde"),
        ("NAMWALA","Namwala"),
        ("NCHELENGE","Nchelenge"),
        ("NDOLA", "Ndola"),
        ("NGOMA", "Ngoma"),
        ("NKANA", "Nkana"),
        ("NSELUKA", "Nseluka"),
        ("NYIMBA","Nyimba"),
        ("PEMBA", "Pemba"),
        ("PETAUKE", "Petauke"),
        ("RUFUNSA","Rufunsa"),
        ("SAMFYA", "Samfya"),
        ("SENANGA", "Senanga"),
        ("SERENJE", "Serenje"),
        ("SESHEKE", "Sesheke"),
        ("SHANGONMBO","Shangombo"),
        ("SHIWANG_ANGU", "Shiwang'andu"),
        ("SIAVONGA", "Siavonga"),
        ("SIKALONGO", "Sikalongo"),
        ("SINAZONGWE", "Sinazongwe"),
        ("SOLWEZI", "Solwezi"),
        ("ZAMBEZI", "Zambezi"),
        ("ZIMBA", "Zimba"),
        ("CENTRAL","Central"),
        ("COPPERBELT","Copperbelt"),
        ("EASTERN","Eastern"),
        ("LUAPULA","Luapula"),
        ("LUSAKA_P","Lusaka Province"),
        ("NORTHERN","Northern"),
        ("NORTH_WESTERN","North Western"),
        ("MUCHINGA","Muchinga"),
        ("WESTERN","Western"),
        ("SOUTHERN","Southern"),
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
    logo = models.ImageField(default='default_logo.png', upload_to='media/logos')
    job_title = models.CharField(max_length=60,null=False, default="")
    post_date = models.DateField(auto_now=False, auto_now_add=True)
    closing_date = models.DateField()
    organisation = models.CharField(max_length=50,null=False, default="")
    location = models.CharField(choices=location_choices,
                                max_length=30,
                                default=NA,
                                )
    country = models.CharField(choices=country_choices, default="", max_length=30)
    industry = models.CharField(choices=industry_choices,
                                max_length=30,
                                default=ACADEMIA,
                                )
    details = RichTextField(blank=True, 
                            null=True,
                            )
    
    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.logo.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.logo.path)

    def __str__(self):
        return self.job_title+" - "+self.closing_date.strftime("%d-%m-%Y")
        
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