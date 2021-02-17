$(document).ready(function() {

    var data = JSON.parse(document.getElementById('json_data').textContent);;
    console.log(data)


    
    for (var key in data) {
        column_data =  $( ".table_row" ).clone().attr('class', 'table_row_' + key)
        if (data.hasOwnProperty(key)) { // this will check if key is owned by data object and not by any of it's ancestors
        column_data.find("td").find("input").attr('value', key)
        column_data.find("td").find("select").val( data[key])
            $( "#forms" ).append( column_data);
        }
    }


$("#add-another").click(function() {
    row =  $( ".table_row" ).clone()
    row.find('select').val($( ".table_row" ).find('select').val())
    row.attr('class', 'table_row_').appendTo( "#forms" );
    $( ".table_row" ).find("td").find("input").val('');
    $( ".table_row" ).find("td").find("select").val('');
    
})


});