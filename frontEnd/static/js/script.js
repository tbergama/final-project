//searchable dropdown
$('.select2').select2();

// Popover
$(document).ready(function() {
    $('[data-toggle="popover"]').popover();
});



// Grab inputted data
function get_inputs() {
    var input_dict = $('#rent_form').serializeArray();

    return input_dict;
}

// Define submit/predict button
var predict_button = d3.select('#predict');


function submit_data(data) {
    fetch('/test', {

            // Specify the method
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            // A JSON payload
            body: JSON.stringify(data)
        }).then(response => response.json())
        .then(function(data) {
            console.log(data);
        });
}

function predict() {
    submit_data(get_inputs());
}

predict_button.on('click', function() {
    predict();
});
// Submit button
d3.select("#submitButton").on("click", function() {
    d3.select.("#finalAmount").style("display", "block");
});