//searchable dropdown
$('.select2').select2();

// Popover
$(document).ready(function() {
    $('[data-toggle="popover"]').popover();
});

// Grab inputted data
function get_inputs() {
    // Get entire form
    var rent_form = d3.select('#rent_form');
    // Grab all 'input' elements and all 'select' elements
    var input_fields = rent_form.selectall('input');
    var select_fields = rent_form.selectAll('select');

    // Define our return object
    var input_dict = {};

    // Iterate through our input/select elements and if filled, add to our return object
    input_fields.forEach(function(d){
        input_dict[d.attr('id')] = d.property('value');
    });
    select_fields.forEach(function(d){
        input_dict[d.attr('id')] = d.property('value');
    });

    return input_dict;
}

// Define submit/predict button
var predict_button = d3.select('#predict');

// Requires JSGlue

function submit_data(inputs){
    $.ajax({
        url: Flask.url_for('predict_rent_price'),
        type: 'POST',
        data: JSON.stringify(movies),   // converts js value to JSON string
        })
        .done(function(result){     // on success get the return object from server
            console.log(result);     // do whatever with it. In this case see it in console
        });
}

function predict(){
    submit_data(get_inputs());
}

predict_button.on('click', function(){
    predict();
});