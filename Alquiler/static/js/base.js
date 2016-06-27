function SumarColumna(grilla, columna){
    var resultVal = 0.0; 
    $("#" + grilla + " tbody tr").each(
        function(){
            var celdaValor = $(this).find('td:eq(' + columna + ')');
            if (celdaValor.val() != null)
                resultVal += parseFloat(celdaValor.html());     
            } //function    
        ) //each
    $("#" + grilla + " tfoot tr:last th:eq(" + columna + ")").html(resultVal.toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","));
}

function PonerComaColumna(grilla, columna){
    var resultVal = 0.0; 
    $("#" + grilla + " tbody tr").each(
        function(){
            var celdaValor = $(this).find('td:eq(' + columna + ')');
            if (celdaValor.val() != null)
                var valor = parseFloat(celdaValor.html());
                $(this).find('td:eq(' + columna + ')').html(valor.toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","));  
        } //function    
    ) //each
}

function EnviarMesAnio(){
    $("#submit").click(function(){
        var year = $("#year").val();
        var month = $("#month").val();
        location.pathname = "/pago/"+ month + "/" + year;
    });
}

function BotonAgregar(){
    $(".Canvas-main-button").click(function(){
        var jsurl = $(this).attr("name");
        location.pathname = jsurl;
    })
}

function MesPredeterminado(month){
    var selec = month - 01;
    $("#form_month_year select").find("option:eq(" + selec + ")").attr("selected", true);
}

function Calendario(){
    $("#datepicker").datepicker({dateFormat: 'dd/mm/yy', firstDay: 1});
}