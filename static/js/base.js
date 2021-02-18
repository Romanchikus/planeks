$(document).ready(function() {

    var data = JSON.parse(document.getElementById('json_data').textContent);;
    console.log(data)


    if (data != '') {
    for (var key in data) {
        column_data =  $( ".table_row" ).clone().attr('class', 'table_row_' + key)
        if (data.hasOwnProperty(key)) { // this will check if key is owned by data object and not by any of it's ancestors
        column_data.find("td").find("input").attr('value', key)
        column_data.find("td").find("select").val( data[key])
        column_data.find(".hidden_td").attr('hidden', false)
        // column_data.find(".hidden_btn").attr('id', '@' + key)
        
            $( "#forms" ).append( column_data);
        }
    }
}


$("#add-another").click(function() {
    row =  $( ".table_row" ).clone()
    row.find('select').val($( ".table_row" ).find('select').val())
    row.attr('class', 'table_row_').appendTo( "#forms" );
    $( ".table_row" ).find("td").find("input").val('');
    $( ".table_row" ).find("td").find("select").val('');
    row.find(".hidden_td").attr('hidden', false)
    row.find("td").find("input").attr('required', true)
    
})

});
$(document).on('click', 'div.hidden_btn', function () {
    $(this).closest('tr').remove();
});