$(document).ready(function() {
let form_count = Number($("[name=extra_field_count]").val());
// get extra form count so we know what index to use for the next item.


element = $( ".table_row" )

$("#add-another").click(function() {
    form_count ++;
    element.attr('class', 'type_name_' + form_count);
    element.appendTo( "#forms")
    console.log(element)
    // build element and append it to our forms container

    $("[name=extra_field_count]").val(form_count);
    // increment form count so our view knows to populate 
    // that many fields for validation
})
});