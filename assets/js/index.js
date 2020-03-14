// when page loads
$(document).ready(function() {
    // get current URL path and assign 'active' class
    var pathname = window.location.pathname;
    $('.navbar-nav > li > a[href="'+pathname+'"]').parent().addClass('active');
})

$(function() {
    $('#toggle-latest').change(function() {
        if ($(this).prop('checked') == true) {
            $('.old').hide();
        } else {
            $('.old').show();
        }
    })
})