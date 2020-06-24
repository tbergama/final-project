//searchable dropdown
$('.select2').select2();

// Popover
$(document).ready(function() {
    $('[data-toggle="popover"]').popover();
});

// Submit button
d3.select("#submitButton").on("click", function() {
    d3.select.("#finalAmount").style("display", "block");
});

// Grab inputted data
function get_inputs() {
    var input_dict = $('#rent_form').serializeArray();

    return input_dict;
}

// Define submit/predict button
var predict_button = d3.select('#predict');

// Requires JSGlue

function submit_data(inputs) {
    $.ajax({
            url: Flask.url_for('predict_rent_price'),
            type: 'POST',
            data: JSON.stringify(movies), // converts js value to JSON string
        })
        .done(function(result) { // on success get the return object from server
            console.log(result); // do whatever with it. In this case see it in console
        });
}

function predict() {
    submit_data(get_inputs());
}

predict_button.on('click', function() {
    predict();
});