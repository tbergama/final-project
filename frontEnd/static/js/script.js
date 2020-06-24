//searchable dropdown
$('.select2').select2();

// // Popover
// $(document).ready(function() {
//     $('[data-toggle="popover"]').popover();
// });



// Grab inputted data
function get_inputs() {
    return $('#rent_form').serializeArray();
}

function submit_data(data) {
    fetch('/model-predict', {

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
            d3.select("#finalAmount").text("$" + data);
            d3.select("#finalAmountdiv").style("display", "block");
        });

}

function predict() {
    submit_data(get_inputs());
}


// Submit button
d3.select("#submitButton").on("click", predict);