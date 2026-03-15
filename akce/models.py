from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

class Akce(models.Model):
    nazev = models.CharField(max_length=200, verbose_name="Název akce")
    datum = models.DateField(blank=True, null=True, help_text="Zadejte datum ve formátu: <em>YYYY-MM-DD</em>.",
                             verbose_name="Datum konání akce")
    popis = models.TextField(blank=True, null=True, verbose_name="Podrobnější popis akce")
    KATEGORIE = (
        ('divadlo', 'Divadlo'),
        ('hudba', 'Hudba'),
        ('kino', 'Kino'),
        ('výstava', 'Výstava'),
    )
    kategorie = models.CharField(max_length=10, choices=KATEGORIE, blank=True, default='hudba', help_text='Vyberte kategorii akce',
                                verbose_name="Kategorie akce")
    hodnoceni = models.FloatField(default=5.0,
                             validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
                             null=True,
                             help_text="Zadejte hodnocení v rozsahu (range 1.0 - 5.0)",
                             verbose_name="Hodnocení")
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Autor akce")
    upraveno = models.DateTimeField(auto_now=True, verbose_name="Datum a čas poslední úpravy")

    class Meta:
        ordering = ["-datum", "nazev"]


    def __str__(self):
        return f"{self.nazev}, datum: {str(self.datum)}"
