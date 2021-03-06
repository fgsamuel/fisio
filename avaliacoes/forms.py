# -*- coding: utf-8 -*-

from django.forms import ModelForm, DateTimeInput
from django.forms.widgets import SelectMultiple

from avaliacoes.models import Avaliacao, Historico, FormularioPARQ, DadosVitais, Circunferencias, PesoAltura, \
	Plicometria, Objetivos, Doenca, AtividadeFisica, Cirurgia, Medicacao, \
	ImagemPostural
from file_resubmit.admin import AdminResubmitFileWidget,\
	AdminResubmitImageWidget


class AvaliacaoForm(ModelForm):
	class Meta:
		model = Avaliacao
		fields = '__all__'
		widgets = {
		            'data': DateTimeInput(format='%d/%m/%Y', attrs={
										'class':'datepicker',
										'size':'10',
										'editable' : 'false'
									}),
	        		}

class ObjetivosForm(ModelForm):
	class Meta:
		model = Objetivos
		exclude = ('avaliacao',)
		
class HistoricoForm(ModelForm):
	class Meta:
		model = Historico
		exclude = ('avaliacao',)
		widgets = {
		            'atividades_fisicas': SelectMultiple(attrs={
										'class':'select2',
										'style':'width:500px',
										'data-placeholder': 'Selecione as atividades físicas'
									}),
		            'doencas': SelectMultiple(attrs={
										'class':'select2',
										'style':'width:350px',
										'data-placeholder': 'Selecione as doenças'
									}),
		            'historico_familiar_doencas': SelectMultiple(attrs={
										'class':'select2',
										'style':'width:500px',
										'data-placeholder': 'Selecione as doenças'
									}),
		            'medicacoes': SelectMultiple(attrs={
										'class':'select2',
										'style':'width:500px',
										'data-placeholder': 'Selecione as medicações'
									}),
		            'cirurgias': SelectMultiple(attrs={
										'class':'select2',
										'style':'width:500px',
										'data-placeholder': 'Selecione as cirurgias'
									}),
	        		}

class FormularioPARQForm(ModelForm):
	class Meta:
		model = FormularioPARQ
		exclude = ('avaliacao',)


class DadosVitaisForm(ModelForm):
	class Meta:
		model = DadosVitais
		exclude = ('avaliacao',)

class CircunferenciasForm(ModelForm):
	class Meta:
		model = Circunferencias
		exclude = ('avaliacao',)

class PesoAlturaForm(ModelForm):
	class Meta:
		model = PesoAltura
		exclude = ('avaliacao',)

class PlicometriaForm(ModelForm):
	class Meta:
		model = Plicometria
		exclude = ('avaliacao',)
		
'''
Este método recebe um form e o valida
após isso, ele pega o conteúdo deste form,
percorre tupla por tupla.
Se todoas estiverem vazias, retorna true
se pelo moenos uma estiver preenchida, retorna false
Se o form não passar na validação, retorna none.
'''
		
class DoencaForm(ModelForm):
	class Meta:
		model = Doenca
		fields = '__all__'

class AtividadeFisicaForm(ModelForm):
	class Meta:
		model = AtividadeFisica
		fields = '__all__'
		
class CirurgiaForm(ModelForm):
	class Meta:
		model = Cirurgia
		fields = '__all__'

class MedicacaoForm(ModelForm):
	class Meta:
		model = Medicacao
		fields = '__all__'
		
class ImagemPosturalForm(ModelForm):
	class Meta:
		model = ImagemPostural
		exclude = ('avaliacao',)
		widgets = {
            'foto': AdminResubmitImageWidget
        }
	
	
	
	
	