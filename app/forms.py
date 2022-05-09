from django import forms
from django.forms import ModelForm, inlineformset_factory

from app.utils import generate_bootstrap_widgets_for_all_fields
from . import (
    models
)


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone phone'
            if field_name == 'cep' or field_name == 'postalcode':
                field.widget.attrs['class'] = 'form-control cep'


class MatchForm(BaseForm, ModelForm):
    class Meta:
        model = models.Match
        fields = (
            "id", "id_match", "competicao", "id_competicao", "time1", "time2", "data", "horario", "local", "estadio",
            "rodada", "posicao", "placar1", "placar2", "penalti1", "penalti2", "eliminou_jogo_volta",
            "classificou_gols_fora", "datahora", "desempate_time1", "desempate_time2")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Match)

    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
