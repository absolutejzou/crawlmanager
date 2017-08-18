$(function() {
    $.ajaxSetup({
        complete: function (xhr, status, e) {
            if ( xhr.status == 278 ) {
                window.location.href = xhr.getResponseHeader("Location");
            }
        },
        traditional: true
    });

    $('.dropdown-button').dropdown({
        inDuration: 300,
        outDuration: 225,
        constrainWidth: false,
        hover: false,
        gutter: 0,
        belowOrigin: true,
        alignment: 'left',
        stopPropagation: true
    });

    $('#side-button').sideNav();
});
