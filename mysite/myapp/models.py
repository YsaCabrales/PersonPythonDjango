from django.db import models
from django.utils.translation import gettext_lazy as _

class Person(models.Model):

    class GenderChoices(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")
        OTHERS = "O", _("Prefer Not To Say")

    class ZodiacSigns(models.TextChoices):
        CAPRICORN = "CORN", _("Capricorn")
        AQUARIUS = "AQUA", _("Aquarius")
        PISCES = "PISC", _("Pisces")
        ARIES = "ARIES", _("Aries")
        TAURUS = "TAU", _("Taurus")
        GEMINI = "GEM", _("Gemini")
        CANCER = "CANC", _("Cancer")
        LEO = "LEO", _("Leo")
        VIRGO = "VIRG", _("Virgo")
        LIBRA = "LIBR", _("Libra")
        SCORPIO = "SCOR", _("Scorpio")
        SAGITARRIUS = "SAG", _("Sagittarius")

    class BloodTypes(models.TextChoices):
        O = "O", _("O")
        A = "A", _("A")
        B = "B", _("B")
        AB = "AB", _("AB")

    # CharField - A string field, for small to large-sized strings.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, null=True, blank=True)

    # IntegerField - An integer. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.
    # SmallIntegerField - -32768 to 32767
    age = models.SmallIntegerField(null=True, blank=True)

    # TextChoices = Just like an Enum
    gender = models.CharField(choices=GenderChoices.choices,
                              default=GenderChoices.OTHERS, max_length=1)

    # A large text field. The default form widget for this field is a Textarea.
    address = models.TextField(default="")
    favorite_artist = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    zodiac_sign = models.CharField(choices=ZodiacSigns.choices, max_length=5, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="myapp/images", null=True, blank=True)
    mbti = models.CharField(max_length=4, null=True, blank=True)
    iq = models.SmallIntegerField(default=100)
    blood_type = models.CharField(choices=BloodTypes.choices, max_length=2, default="O")

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
