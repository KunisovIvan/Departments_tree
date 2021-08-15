    $('.my-dropdown-submenu--after').on('click', function (event) {
    console.log('CLICK')
        $(this).parent().parent().toggleClass('my-dropdown-submenu--active')
    })