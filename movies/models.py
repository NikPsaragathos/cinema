from django.db import models
from datetime import date



MOVIE_CATEGORIES = [(0,"ALL"), (1,"Δράσης"),(2,"Επιστημονικής Φαντασίας"), (3,"Δραματική"),(4,"Ρομαντική"), (5,"Ιστορική"),(6,"Βιογραφική")]
TIME_CHOICES =[(0,"(Όλα)"), (1,"18:00 μμ"),(2,"19:00 μμ"), (3,"20:00 μμ"),(4,"21:00 μμ"), (5,"22:00 μμ"),(6,"23:00 μμ"),(7,"24:00 μμ")]
PRICE_CHOICES = [(0, "Όλα"), (1, "Φοιτητικό/Στρατιωτικό: 5,5€"), (2, "Παιδικό:7,5€"), (3, "Αίθουσα 2D:10€"), (4, "Αίθουσα 3D:11€"),(5, "Αίθουσα DOLBY:11€"), (6, "Αίθουσα DOLBY-3D:12€"), (7, "Αίθουσα GOLD:20€")]

# --------------------------------------------------------------------
# Model movie
# --------------------------------------------------------------------

class movie(models.Model):
    title = models.CharField(max_length=100, blank=True, default='', verbose_name="ΤΙΤΛΟΣ")
    director = models.CharField(max_length=100, blank=True, default='', verbose_name="ΣΚΗΝΟΘΕΤΗΣ")
    actor = models.CharField(max_length=100, blank=True, default='', verbose_name="ΗΘΟΠΟΙΟΣ")
    categoryId = models.IntegerField(choices=MOVIE_CATEGORIES,null=True, verbose_name="ΚΑΤΗΓΟΡΙΑ")
    imbdUrl = models.CharField(max_length=400, blank=True, default='')
    coverUrl = models.CharField(max_length=400, blank=True, default='', verbose_name="ΕΞΩΦΥΛΟ")
    viewDate= models.DateField(verbose_name="ΗΜΕΡΟΜΗΝΙΑ ΠΡΟΒΟΛΗΣ", default=date.today)
    timeId = models.IntegerField(choices=TIME_CHOICES, default='', verbose_name="ΩΡΑ ΠΡΟΒΟΛΗΣ")
    priceId =  models.IntegerField(choices=PRICE_CHOICES, default='', verbose_name="ΤΙΜΗ ΕΙΣΗΤΗΡΙΟΥ")
    description = models.CharField(max_length=1000, blank=True, default='', verbose_name="ΠΕΡΙΓΡΑΦΗ ΤΑΙΝΙΑΣ")
    trailer=models.CharField(max_length=1000, blank=True, default='', verbose_name="TRAILER ΤΑΙΝΙΑΣ")
    owner = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return "{0} ({1} {2})".format(self.title, self.director, self.categoryId)

    class Meta:
        db_table = "movie"
        verbose_name = "Ταινία"
        verbose_name_plural = "Ταινίες"
        ordering = ["title"]
