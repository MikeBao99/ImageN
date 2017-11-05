$(document).ready(function() {
    $('.quiz-button').click(function() {
        $('#sidebar .sidebar-group a').each(function() {
            if (window.location.href.includes($(this).attr('href'))) {
                if ($(this).attr('href') != '/') {
                    localStorage.setItem($(this).text(), true);
                }
            }
        });
    });

    $('#sidebar .sidebar-group a').each(function() {
        if (window.location.href.includes($(this).attr('href'))) {
            if ($(this).attr('href') != '/') {
                $(this).parent().addClass('active');
            }
        }
        if (localStorage.getItem($(this).text()) != undefined) {
            var icon = $(document.createElement('span'));
            icon.addClass('glyphicon glyphicon-ok');
            icon.css('float', 'right');
            $(this).append(icon);
        }
    });
});
