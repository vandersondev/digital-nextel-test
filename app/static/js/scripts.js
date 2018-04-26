(function($) {
    $(function() {
        $('.vacation-form').on('submit', function() {
            if (!$('.weather-group input[type=checkbox]:checked').length) {
                alert('Selecione ao menos um clima');
                return false;
            }
        });
    });
})(jQuery);