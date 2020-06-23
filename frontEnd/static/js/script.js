//searchable dropdown
$('.select2').select2();

// Popover
$(document).ready(function() {
    $('[data-toggle="popover"]').popover();
});

d3.select("#submitButton").on("click", function() {
    d3.select.("#finalAmount").style("display", "block");
});