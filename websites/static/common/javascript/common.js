$.ajaxSetup({
    complete: function (xhr, status, e) {
        if ( xhr.status == 278 ) {
            window.location.href = xhr.getResponseHeader("Location");
        }
    },
    traditional: true
});