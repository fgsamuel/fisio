$(function() {
	carregaDatepicker();
});

function carregaDatepicker(){
    //cria o datepicker com op��o de mes e ano
	$( ".datepicker" ).datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: "c-100:c"
      }, $.datepicker.regional[ "pt-BR" ]);

	//retira a edicao do campo
	$('.datepicker').attr('editable', false);
  }