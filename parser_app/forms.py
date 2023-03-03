from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOISES = (
        ("CARS", "CARS"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISES)

    class Meta:
        fields = [
            'media_type'
        ]

    def parser_data(self):
        if self.data['media_type'] == "CARS_KG":
            car_parser = parser.parser()
            for i in car_parser:
                models.CarParser.objects.create(**i)