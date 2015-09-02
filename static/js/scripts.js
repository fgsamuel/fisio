$(function() {
	carregaDatepicker();
  carregaSelect2();
});

function carregaDatepicker(){
	$( ".datepicker" ).datepicker({
        format: 'dd/mm/yyyy',
      });
  }

//Configura o componente chosen
function carregaSelect2(){
  $(".select2").select2();
}