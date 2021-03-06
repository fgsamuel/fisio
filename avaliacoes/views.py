# -*- coding: utf-8 -*-

import datetime

from django.forms.formsets import formset_factory

from avaliacoes.forms import AvaliacaoForm, HistoricoForm, FormularioPARQForm, DadosVitaisForm, \
	CircunferenciasForm, PesoAlturaForm, PlicometriaForm, ObjetivosForm, \
	ImagemPosturalForm
from avaliacoes.models import ImagemPostural, Avaliacao
from views_simpleClass import *


def avaliacoes_listar(request):
	
	context = {}
	
	if request.method == 'POST':
		txtCliente = request.POST.get('txtCliente')
		txtAvaliador = request.POST.get('txtAvaliador')
		txtData = request.POST.get('txtData')
		
		filtro = {}
		
		if txtCliente:
			filtro['cliente__nome__icontains'] = txtCliente
			context['txtCliente'] = txtCliente
		if txtAvaliador:
			filtro['avaliador__nome__icontains'] = txtAvaliador
			context['txtAvaliador'] = txtAvaliador
		if txtData:
			filtro['data__exact'] = datetime.datetime.strptime(txtData, '%d/%m/%Y').strftime('%Y-%m-%d')
			context['txtData'] = txtData
		
		if filtro:
			lista = Avaliacao.objects.filter(**filtro)
		else:
			lista = Avaliacao.objects.all()

	else:		
		lista = Avaliacao.objects.all()
		
	context['lista'] = lista
	return render(request, 'avaliacoes/index.html', context)

def avaliacoes_inserir(request):
	avaliacaoForm = AvaliacaoForm(prefix="avaliacao")
	historicoForm = HistoricoForm(prefix="historico")
	parqForm = FormularioPARQForm(prefix="parq")
	dadosVitaisForm = DadosVitaisForm(prefix="dadosvitais")
	circunferenciasForm = CircunferenciasForm(prefix="circunferencias")
	pesoAlturaForm = PesoAlturaForm(prefix="pesoAltura")
	plicometriaForm = PlicometriaForm(prefix="plicometria")
	objetivosForm = ObjetivosForm(prefix="objetivos")
	ImagemPosturalFormSet = formset_factory(ImagemPosturalForm, extra=1)
	imagemPosturalFormSet = ImagemPosturalFormSet(prefix='imagem')
		
	if request.method == 'POST': # If the form has been submitted...
		imagemPosturalFormSet = ImagemPosturalFormSet(request.POST, request.FILES, prefix='imagem')
		avaliacaoForm = AvaliacaoForm(request.POST, prefix="avaliacao")
		historicoForm = HistoricoForm(request.POST, prefix="historico")
		parqForm = FormularioPARQForm(request.POST, prefix="parq")
		dadosVitaisForm = DadosVitaisForm(request.POST, prefix="dadosvitais")
		circunferenciasForm = CircunferenciasForm(request.POST, prefix="circunferencias")
		pesoAlturaForm = PesoAlturaForm(request.POST, prefix="pesoAltura")
		plicometriaForm = PlicometriaForm(request.POST, prefix="plicometria")
		objetivosForm = ObjetivosForm(request.POST, prefix="objetivos")

		
		if avaliacaoForm.is_valid() \
		and historicoForm.is_valid() \
		and parqForm.is_valid() \
		and dadosVitaisForm.is_valid() \
		and circunferenciasForm.is_valid() \
		and pesoAlturaForm.is_valid() \
		and plicometriaForm.is_valid() \
		and objetivosForm.is_valid() \
		and imagemPosturalFormSet.is_valid() :
			#salva a avaliação no banco primeiro para poder salvar os filhos
			avaliacao = avaliacaoForm.save()

			
			if historicoForm.has_changed():
				historico = historicoForm.save(commit=False)
				historico.avaliacao = avaliacao
				historico.save()
				historicoForm.save_m2m()
			
			if objetivosForm.has_changed():
				objetivos = objetivosForm.save(commit=False)
				objetivos.avaliacao = avaliacao
				objetivos.save()

			if parqForm.has_changed():
				parq = parqForm.save(commit=False)
				parq.avaliacao = avaliacao
				parq.save()

			if dadosVitaisForm.has_changed():
				dadosVitais = dadosVitaisForm.save(commit=False)
				dadosVitais.avaliacao = avaliacao
				dadosVitais.save()

			if circunferenciasForm.has_changed():
				circunferencias = circunferenciasForm.save(commit=False)
				circunferencias.avaliacao = avaliacao
				circunferencias.save()

			if pesoAlturaForm.has_changed():
				pesoAltura = pesoAlturaForm.save(commit=False)
				pesoAltura.avaliacao = avaliacao
				pesoAltura.save()
				
			if plicometriaForm.has_changed():
				plicometria = plicometriaForm.save(commit=False)
				plicometria.avaliacao = avaliacao
				plicometria.save()
			
			for imagem in imagemPosturalFormSet:
				print(imagem)
				if imagem.has_changed():
					i = imagem.save(commit=False)
					i.avaliacao = avaliacao
					i.save()
			
			return redirect("avaliacoes_listar")
			
	context = {
		'avaliacaoForm' : avaliacaoForm,
		'historicoForm' : historicoForm,
		'parqForm' : parqForm,
		'dadosVitaisForm' : dadosVitaisForm,
		'circunferenciasForm' : circunferenciasForm,
		'pesoAlturaForm' : pesoAlturaForm,
		'plicometriaForm' : plicometriaForm,
		'objetivosForm' : objetivosForm,
		'imagemPosturalFormSet':imagemPosturalFormSet,
		}
	return render(request, 'avaliacoes/inserir.html', {'forms':context})


def avaliacoes_visualizar(request, pk):
	a = Avaliacao.objects.get(pk=pk)
	context = {'obj':a}
	return render(request, 'avaliacoes/visualizar.html', context)

def avaliacoes_editar(request, pk):
	
	a = Avaliacao.objects.get(pk=pk)
	
	if request.method == 'POST': # If the form has been submitted...
		avaliacaoForm = AvaliacaoForm(request.POST, instance=a, prefix="avaliacao")
		historicoForm = HistoricoForm(request.POST, instance=a.historico, prefix="historico")
		parqForm = FormularioPARQForm(request.POST, instance=a.formularioparq, prefix="parq")
		dadosVitaisForm = DadosVitaisForm(request.POST, instance=a.dadosvitais, prefix="dadosvitais")
		circunferenciasForm = CircunferenciasForm(request.POST, instance=a.circunferencias, prefix="circunferencias")
		pesoAlturaForm = PesoAlturaForm(request.POST, instance=a.pesoaltura, prefix="pesoAltura")
		plicometriaForm = PlicometriaForm(request.POST, instance=a.plicometria, prefix="plicometria")
		objetivosForm = ObjetivosForm(request.POST, instance=a.objetivos, prefix="objetivos")

		
		if avaliacaoForm.is_valid() \
		and historicoForm.is_valid() \
		and parqForm.is_valid() \
		and dadosVitaisForm.is_valid() \
		and circunferenciasForm.is_valid() \
		and pesoAlturaForm.is_valid() \
		and plicometriaForm.is_valid() \
		and objetivosForm.is_valid() :
			#salva a avaliação no banco primeiro para poder salvar os filhos
			avaliacao = avaliacaoForm.save()

			
			if historicoForm.has_changed():
				historico = historicoForm.save(commit=False)
				historico.avaliacao = avaliacao
				historico.save()
				historicoForm.save_m2m()
			
			if objetivosForm.has_changed():
				objetivos = objetivosForm.save(commit=False)
				objetivos.avaliacao = avaliacao
				objetivos.save()

			if parqForm.has_changed():
				parq = parqForm.save(commit=False)
				parq.avaliacao = avaliacao
				parq.save()

			if dadosVitaisForm.has_changed():
				dadosVitais = dadosVitaisForm.save(commit=False)
				dadosVitais.avaliacao = avaliacao
				dadosVitais.save()

			if circunferenciasForm.has_changed():
				circunferencias = circunferenciasForm.save(commit=False)
				circunferencias.avaliacao = avaliacao
				circunferencias.save()

			if pesoAlturaForm.has_changed():
				pesoAltura = pesoAlturaForm.save(commit=False)
				pesoAltura.avaliacao = avaliacao
				pesoAltura.save()
				
			if plicometriaForm.has_changed():
				plicometria = plicometriaForm.save(commit=False)
				plicometria.avaliacao = avaliacao
				plicometria.save()
			
			return redirect("avaliacoes_listar")
	else:
		avaliacaoForm = AvaliacaoForm(instance=a, prefix="avaliacao")
		historicoForm = HistoricoForm(instance=a.historico, prefix="historico")
		parqForm = FormularioPARQForm(instance=a.formularioparq, prefix="parq")
		dadosVitaisForm = DadosVitaisForm(instance=a.dadosvitais, prefix="dadosvitais")
		circunferenciasForm = CircunferenciasForm(instance=a.circunferencias, prefix="circunferencias")
		pesoAlturaForm = PesoAlturaForm(instance=a.pesoaltura, prefix="pesoAltura")
		plicometriaForm = PlicometriaForm(instance=a.plicometria, prefix="plicometria")
		objetivosForm = ObjetivosForm(instance=a.objetivos, prefix="objetivos")
		context = {
			'avaliacaoForm' : avaliacaoForm,
			'historicoForm' : historicoForm,
			'parqForm' : parqForm,
			'dadosVitaisForm' : dadosVitaisForm,
			'circunferenciasForm' : circunferenciasForm,
			'pesoAlturaForm' : pesoAlturaForm,
			'plicometriaForm' : plicometriaForm,
			'objetivosForm' : objetivosForm,
			}
		return render(request, 'avaliacoes/editar.html', {'forms':context})
	

def imagens(request):
	ImagemPosturalFormSet = formset_factory(ImagemPosturalForm, extra=1)
	forms = ImagemPosturalFormSet()
	# Handle file upload
	if request.method == 'POST':
		todel = request.POST.getlist('todelete')
		print(todel)

	
	# Load documents for the list page
	lista = ImagemPostural.objects.all()

	# Render list page with the documents and the form
	return render(request, 'imagens.html', {'lista':lista, 'forms':forms})
