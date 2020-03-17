// when page loads
$(document).ready(function() {
    // get current URL path and assign 'active' class
    var pathname = window.location.pathname;
    $('.navbar-nav > li > a[href="'+pathname+'"]').parent().addClass('active');
})

$(function() {
    $('#toggle-latest').change(function() {
        if ($(this).prop('checked') == true) {
            // reset topics checkbox effect
            $('td li').show();
            $('tbody tr').show();
            $('#theme-checkbox input[type=checkbox]').each(function() {
                $(this).prop('checked', false);
                $(this).parent().removeClass("active");
            });
            $('.old').hide();
        } else {
            $('.old').show();
        }
    })
})

$(function() {
    $('#theme-checkbox input[type=checkbox]').click(function(){
        $('.test-txt').html("val: " + $(this).val() + ", checked: " + $(this).prop('checked'));
        $('#theme-checkbox input[type=checkbox]').not(this).each(function() {
            $(this).prop('checked', false);
            $(this).parent().removeClass("active");
        });
        if ($(this).prop('checked')) {
            $('td li').hide();
            $('td li.' + $(this).val()).show();
            $('tbody tr').hide();
            $('tbody tr.' + $(this).val()).show();
        } else {
            $('td li').show();
            $('tbody tr').show();
        }
    });
})
