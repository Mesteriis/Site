let  transparent = true;
let  transparentDemo = false;
let  fixedTop = false;

let  navbar_initialized = false;
let  backgroundOrange = true;
let  sidebar_mini_active = false;
let  toggle_initialized = false;

let  $html = $('html');
let  $body = $('body');
let  $navbar_minimize_fixed = $('.navbar-minimize-fixed');
let  $collapse = $('.collapse');
let  $navbar = $('.navbar');
let  $tagsinput = $('.tagsinput');
let  $selectpicker = $('.selectpicker');
let  $navbar_color = $('.navbar[color-on-scroll]');
let  $full_screen_map = $('.full-screen-map');
let  $datetimepicker = $('.datetimepicker');
let  $datepicker = $('.datepicker');
let  $timepicker = $('.timepicker');

let  seq = 0,
    delays = 80,
    durations = 500;
let  seq2 = 0,
    delays2 = 80,
    durations2 = 500;

(function () {
    let  isWindows = navigator.platform.indexOf('Win') > -1 ? true : false;

    if (isWindows) {
        // if we are on windows OS we activate the perfectScrollbar function
        if ($('.main-panel').length != 0) {
            let  ps = new PerfectScrollbar('.main-panel', {
                wheelSpeed: 2,
                wheelPropagation: true,
                minScrollbarLength: 20,
                suppressScrollX: true
            });
        }

        if ($('.sidebar .sidebar-wrapper').length != 0) {

            let  ps1 = new PerfectScrollbar('.sidebar .sidebar-wrapper');
            $('.table-responsive').each(function () {
                let  ps2 = new PerfectScrollbar($(this)[0]);
            });
        }


        $html.addClass('perfect-scrollbar-on');
    } else {
        $html.addClass('perfect-scrollbar-off');
    }
})();

$(document).ready(function () {

    let  scroll_start = 0;
    let  startchange = $('.row');
    let  offset = startchange.offset();
    let  scrollElement = navigator.platform.indexOf('Win') > -1 ? $(".ps") : $(window);
    scrollElement.scroll(function () {

        scroll_start = $(this).scrollTop();

        if (scroll_start > 50) {
            $(".navbar-minimize-fixed").css('opacity', '1');
        } else {
            $(".navbar-minimize-fixed").css('opacity', '0');
        }
    });


    $(document).scroll(function () {
        scroll_start = $(this).scrollTop();
        if (scroll_start > offset.top) {
            $(".navbar-minimize-fixed").css('opacity', '1');
        } else {
            $(".navbar-minimize-fixed").css('opacity', '0');
        }
    });

    if ($('.full-screen-map').length == 0 && $('.bd-docs').length == 0) {
        // On click navbar-collapse the menu will be white not transparent
        $('.collapse').on('show.bs.collapse', function () {
            $(this).closest('.navbar').removeClass('navbar-transparent').addClass('bg-white');
        }).on('hide.bs.collapse', function () {
            $(this).closest('.navbar').addClass('navbar-transparent').removeClass('bg-white');
        });
    }

    blackDashboard.initMinimizeSidebar();

    $navbar = $('.navbar[color-on-scroll]');
    scroll_distance = $navbar.attr('color-on-scroll') || 500;

    // Check if we have the class "navbar-color-on-scroll" then add the function to remove the class "navbar-transparent" so it will transform to a plain color.
    if ($('.navbar[color-on-scroll]').length != 0) {
        blackDashboard.checkScrollForTransparentNavbar();
        $(window).on('scroll', blackDashboard.checkScrollForTransparentNavbar)
    }

    $('.form-control').on("focus", function () {
        $(this).parent('.input-group').addClass("input-group-focus");
    }).on("blur", function () {
        $(this).parent(".input-group").removeClass("input-group-focus");
    });

    // Activate bootstrapSwitch
    $('.bootstrap-switch').each(function () {
        $this = $(this);
        data_on_label = $this.data('on-label') || '';
        data_off_label = $this.data('off-label') || '';

        $this.bootstrapSwitch({
            onText: data_on_label,
            offText: data_off_label
        });
    });
});

$(document).on('click', '.navbar-toggle', function () {
    let  $toggle = $(this);

    if (blackDashboard.misc.navbar_menu_visible == 1) {
        $html.removeClass('nav-open');
        blackDashboard.misc.navbar_menu_visible = 0;
        setTimeout(function () {
            $toggle.removeClass('toggled');
            $('.bodyClick').remove();
        }, 550);

    } else {
        setTimeout(function () {
            $toggle.addClass('toggled');
        }, 580);

        let  div = '<div class="bodyClick"></div>';
        $(div).appendTo('body').click(function () {
            $html.removeClass('nav-open');
            blackDashboard.misc.navbar_menu_visible = 0;
            setTimeout(function () {
                $toggle.removeClass('toggled');
                $('.bodyClick').remove();
            }, 550);
        });

        $html.addClass('nav-open');
        blackDashboard.misc.navbar_menu_visible = 1;
    }
});

$(window).resize(function () {
    // reset the seq for charts drawing animations
    seq = seq2 = 0;

    if ($full_screen_map.length == 0 && $('.bd-docs').length == 0) {
        let  isExpanded = $navbar.find('[data-toggle="collapse"]').attr("aria-expanded");
        if ($navbar.hasClass('bg-white') && $(window).width() > 991) {
            $navbar.removeClass('bg-white').addClass('navbar-transparent');
        } else if ($navbar.hasClass('navbar-transparent') && $(window).width() < 991 && isExpanded != "false") {
            $navbar.addClass('bg-white').removeClass('navbar-transparent');
        }
    }
});

blackDashboard = {
    misc: {
        navbar_menu_visible: 0
    },

    initMinimizeSidebar: function () {
        if ($('.sidebar-mini').length != 0) {
            sidebar_mini_active = true;
        }

        $('#minimizeSidebar').click(function () {
            let  $btn = $(this);

            if (sidebar_mini_active == true) {
                $('body').removeClass('sidebar-mini');
                sidebar_mini_active = false;
                blackDashboard.showSidebarMessage('Sidebar mini deactivated...');
            } else {
                $('body').addClass('sidebar-mini');
                sidebar_mini_active = true;
                blackDashboard.showSidebarMessage('Sidebar mini activated...');
            }

            // we simulate the window Resize so the charts will get updated in realtime.
            let  simulateWindowResize = setInterval(function () {
                window.dispatchEvent(new Event('resize'));
            }, 180);

            // we stop the simulation of Window Resize after the animations are completed
            setTimeout(function () {
                clearInterval(simulateWindowResize);
            }, 1000);
        });
    },

    showSidebarMessage: function (message) {
        try {
            $.notify({
                icon: "tim-icons ui-1_bell-53",
                message: message
            }, {
                type: 'info',
                timer: 4000,
                placement: {
                    from: 'top',
                    align: 'right'
                }
            });
        } catch (e) {
            console.log('Notify library is missing, please make sure you have the notifications library added.');
        }

    }

};

function hexToRGB(hex, alpha) {
    let  r = parseInt(hex.slice(1, 3), 16),
        g = parseInt(hex.slice(3, 5), 16),
        b = parseInt(hex.slice(5, 7), 16);

    if (alpha) {
        return "rgba(" + r + ", " + g + ", " + b + ", " + alpha + ")";
    } else {
        return "rgb(" + r + ", " + g + ", " + b + ")";
    }
}

$('#inChat').on('click', function () {
    $('#createdTicketDiv').hide()
    $('#ChatDiv').show()
    $('#attentions_label').hide()
})
$('#btnTicketCreated').on('click', function () {
    $('#createdTicketDiv').show()
    $('#ChatDiv').hide()
    $('#attentions_label').show()
})

function showNotification(from, align, text) {
    $.notify({
        icon: "tim-icons icon-bell-55",
        message: text

    }, {
        type: red,
        timer: 8000,
        placement: {
            from: from,
            align: align
        }
    });
}

$('.FirstCardBtn').on('click', function () {
    switch (this.id) {
        case '0': {
            $('#pls_0').show()
            $('#pls_1').hide()
            $('#pls_2').hide()
            break;
        }
        case '1': {
            $('#pls_0').hide()
            $('#pls_1').show()
            $('#pls_2').hide()
            break;
        }
        case '2': {
            $('#pls_0').hide()
            $('#pls_1').hide()
            $('#pls_2').show()
            break;
        }
    }
})
for (let notification of document.getElementsByClassName('itemNotifi')) {
    console.log(notification.textContent);
    showNotification('bottom', 'right', notification.textContent)
}

function addNewTab(name, siteAddress, width = '100%', height = '1000px', token = NaN, setStateAction = true) {
    let tabsPanel = document.getElementById('nav-tab');
    let newTab = document.createElement('a');
    let newContainer = document.createElement('div')
    let newEntered = document.createElement('div')
    newContainer.className = "tab-pane fade"
    newContainer.id = name + '-ContainerID'
    newTab.className = 'nav-item nav-link ml-2';
    let tmpSTR = '<span class="badge badge-light ml-1" id="' + name + '-CloseBtnTab">&times;</span>'
    newTab.innerHTML = name + " " + tmpSTR;
    newTab.id = name + '-TabID';
    newTab.setAttribute('data-toggle', "tab");
    newTab.href = '#' + newContainer.id;
    newTab.role = "tab";
    newTab.setAttribute('aria-controls', newContainer.id);
    newTab.setAttribute('aria-selected', "false");
    newContainer.setAttribute('aria-labelledby', newTab.id)
    newContainer.setAttribute('role', 'tabpanel')
    document.getElementById('nav-dash-tab').after(newTab);
    newEntered.className = "container-fluid";
    // newEntered.id =
    // содержание контейнера дописать

    let Iframe = document.createElement('iframe');
    // Iframe.src = 'http://online.wialon.center';
    Iframe.src = siteAddress;
    Iframe.setAttribute('frameBorder', 'no');
    Iframe.seamless = true;
    Iframe.innerText = 'Ваш браузер не поддерживает плавающие фреймы!';
    Iframe.style.width = width;
    Iframe.style.height = height;
    // туда
    // Iframe.contentWindow.postMessage('message', '*');
    // Iframe.allow = token; // token для сайт
    Iframe.loading = 'lazy'
    // там его обработать
    window.onmessage = function (event) {
        if (event.data == 'message') {
            console.log('Message received!');
        }
    };
    // от туда
    // window.top.postMessage('reply', '*')
    window.onmessage = function (event) {
        if (event.data == 'reply') {
            console.log('Reply received!');
        }
    };
    newEntered.append(Iframe);
    newContainer.prepend(newEntered);
    console.log(newContainer);
    document.getElementById('nav-tabContent').append(newContainer)
    if (setStateAction) {
        newTab.click();
    }
    let cb = document.getElementById(name + '-CloseBtnTab');
    cb.style.opacity = '.0';
    cb.addEventListener('click', function () {
        console.log(this);
        let base = this.id.substr(0, this.id.indexOf('-'));
        for (let tab of document.getElementById('nav-tab').children) {
            if (!tab.classList.contains('active')) {
                tab.click();
                break;
            }
        }
        document.getElementById(base + '-ContainerID').remove();
        document.getElementById(base + '-TabID').remove();
    })
    cb.addEventListener('mouseenter', function () {
        cb.style.opacity = '1';

    })
    cb.addEventListener('mouseleave', function () {
        cb.style.opacity = '0.1';

    })
    cb.style.borderRadius = '2px'
}


$(document).ready(function () {
    $().ready(function () {
        let $sidebar = $('.sidebar');
        let $navbar = $('.navbar');
        let $main_panel = $('.main-panel');

        let $full_page = $('.full-page');

        let $sidebar_responsive = $('body > .navbar-collapse');
        let sidebar_mini_active = true;
        let white_color = false;

        let window_width = $(window).width();

        let fixed_plugin_open = $('.sidebar .sidebar-wrapper .nav li.active a p').html();


        $('.fixed-plugin a').click(function (event) {
            if ($(this).hasClass('switch-trigger')) {
                if (event.stopPropagation) {
                    event.stopPropagation();
                } else if (window.event) {
                    window.event.cancelBubble = true;
                }
            }
        });

        $('.fixed-plugin .background-color span').click(function () {
            $(this).siblings().removeClass('active');
            $(this).addClass('active');

            let  new_color = $(this).data('color');

            if ($sidebar.length != 0) {
                $sidebar.attr('data', new_color);
            }

            if ($main_panel.length != 0) {
                $main_panel.attr('data', new_color);
            }

            if ($full_page.length != 0) {
                $full_page.attr('filter-color', new_color);
            }

            if ($sidebar_responsive.length != 0) {
                $sidebar_responsive.attr('data', new_color);
            }
        });

        $('.switch-sidebar-mini input').on("switchChange.bootstrapSwitch", function () {
            let  $btn = $(this);

            if (sidebar_mini_active == true) {
                $('body').removeClass('sidebar-mini');
                sidebar_mini_active = false;
                blackDashboard.showSidebarMessage('Sidebar mini deactivated...');
            } else {
                $('body').addClass('sidebar-mini');
                sidebar_mini_active = true;
                blackDashboard.showSidebarMessage('Sidebar mini activated...');
            }

            // we simulate the window Resize so the charts will get updated in realtime.
            let  simulateWindowResize = setInterval(function () {
                window.dispatchEvent(new Event('resize'));
            }, 180);

            // we stop the simulation of Window Resize after the animations are completed
            setTimeout(function () {
                clearInterval(simulateWindowResize);
            }, 1000);
        });

        $('.switch-change-color input').on("switchChange.bootstrapSwitch", function () {
            let  $btn = $(this);

            if (white_color == true) {

                $('body').addClass('change-background');
                setTimeout(function () {
                    $('body').removeClass('change-background');
                    $('body').removeClass('white-content');
                }, 900);
                white_color = false;
            } else {

                $('body').addClass('change-background');
                setTimeout(function () {
                    $('body').removeClass('change-background');
                    $('body').addClass('white-content');
                }, 900);

                white_color = true;
            }


        });

        $('.light-badge').click(function () {
            $('body').addClass('white-content');
        });

        $('.dark-badge').click(function () {
            $('body').removeClass('white-content');
        });
    });
});