(function ($) {
	
	// Меняем тип поля с text на date
	/*
		$("#id_birth_date").focus(function() {
			$(this).attr("type", "date")
		});
	*/
	
	// Инициализируем datepicker
	if ($("#id_birth_date").length > 0) {
		$( "#id_birth_date" ).datepicker({ dateFormat: 'dd.mm.yy' }).attr("autocomplete", "off") ;
	}
	
	// Инициализируем PhoneMask
	if ($("#id_phone").length > 0){
	      $('#id_phone').usPhoneFormat({
          format: '(xxx) xxx-xxxx',
      });   
	}
	
	// Скрываем сообщения
	if ($('#msg').length > 0){ 
		setTimeout(function(){
			$('#msg').slideUp("normal", function() { $('#msg').remove(); } )
		}, 2000);
	}
	
	//
	 $('#dataTable').DataTable();
	
})(window.jQuery);