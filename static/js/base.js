$(document).ready(function() {

    var data = JSON.parse(document.getElementById('json_data').textContent);;
    console.log(data)

    if (data != '') {
    for (var key in data) {
        column_data =  $( ".table_row" ).clone().attr('class', 'table_row_' + key)
        if (data.hasOwnProperty(key)) {
            list_of_key = data[key]
            
            column_data.find("td").find("input").attr('value', key)
            column_data.find("td").find("select").val( list_of_key[0])
            if (list_of_key[0] == 'age') {
                range = column_data.find(".range_td").find(".range_hidden")
                range.attr('hidden', false)
                range.find("#ran_from").attr('value', list_of_key[1])
                range.find("#ran_from_to").attr('value', list_of_key[2])
            }
            column_data.find(".hidden_td").attr('hidden', false)
        
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
    row.find("td").find(".Column").find("input").attr('required', true)
    
})

});
$(document).on('click', 'div.hidden_btn', function () {
    $(this).closest('tr').remove();
});

$(document).on('change', '#id_types', function () {
    if ($(this).val() == 'age') {
   $(this).parent().parent().find(".range_td").find(".range_hidden").attr('hidden', false)
    }
    else {
        $(this).parent().parent().find(".range_td").find(".range_hidden").attr('hidden', true)
    }
}).change();