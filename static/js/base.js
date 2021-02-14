$(document).ready(function() {
let form_count = Number($("[name=extra_field_count]").val());

table_row =  $( ".table_row" ).clone().attr('class', 'table_row_0')
table_row.find("td").find("input").attr('required', false)

$("#add-another").click(function() {
    form_count ++;
    row = table_row.clone()
    row.attr('class', 'table_row_' + form_count).appendTo( "#forms" );
    
    $("[name=extra_field_count]").val(form_count);
})
});

// function AddRenamedTag(type, obj) {
//     element = $( "" + obj ).clone()
//     element.attr('name', ('obj_' + obj,'obj_' + form_count));
//     element.appendTo( "#forms" );
//   }