let arrScreenShot = [];
$('select').on('change', function () {
    switch (this.value) {
        case 'S_techSupportDiv': {
            $('.depsForm').hide()
            $('#S_techSupportDiv').show()
            $('#openChatBtnFormSupport').show()
            break;
        }
        case 'S_AccDiv': {
            $('.depsForm').hide()
            $('#openChatBtnFormSupport').hide()
            $('#S_AccDiv').show()
            break;
        }
        case 'd3': {
            $('#openChatBtnFormSupport').hide()
            break;
        }
        case 'S_Devs': {
            $('.depsForm').hide()
            $('#openChatBtnFormSupport').hide()
            $('#S_Devs').show()
            break;
        }
    }

});
$(document).ready(function () {
    if (arrScreenShot.length > 4) {

    }
    $('#getScreeShot').click(function (e) {
        e.preventDefault();
        // в html2canvas передаем id контента
        html2canvas($('#screenShotAria')[0], {
            scale: 1 // Дополнительные опции
        }).then(function (canvas) {
            arrScreenShot.push(canvas.toDataURL());
            let imgBase64 = canvas.toDataURL().toString();
            let img = $("<img class='screenShot'/>");
            img.attr('src', imgBase64);
            img.id = 'scr' + (arrScreenShot.length - 1)
            img.css('display', 'inline-block');
            img.css('margin', '1px');
            let divImg = $("<div class='placeHolderScreenshot'></div>")

            $(divImg).append(img)
            let tmpSTR = $('<span class="badge badge-light ml-1" id="Scr-' + (arrScreenShot.length - 1) + '-CloseBtn">&times;</span>')
            $(divImg).append(tmpSTR)
            $('#ScreenShotPrevPlace').append(divImg)
            if (arrScreenShot.length > 4) {
                $('#getScreeShot').hide()
            }
            $(tmpSTR).on('click', function () {
                let i = 'Scr-0-CloseBtn'
                delete arrScreenShot[i]
                $(this).parent().remove()
                if (arrScreenShot.length >= 5) {
                    $('#getScreeShot').show()
                }
            })
            //canvas.toBlob(function(blob) {
            //saveAs(blob, "screenshoot.png");
            //});
        });
    });
});
$('#closeBtnFormSupport').on('click', function () {

})
$('#submitBtnFormSupport').on('click', function () {
    switch ($('#depsSelect').val()) {

        case 'S_techSupportDiv': {
            let person = {
                'fio': $('#s_contactName').val(),
                'tel': $('#s_contactTel').val(),
                'user': '',
                'firm': '',
                'userTel': ''
            };
            let pack = {
                'dep': 'Support',
                'type': $('#s_typeTicket option:selected').text(),
                'title': $('#s_TitleTicket').val(),
                'note': $('#s_noteTicket').val(),
                'person': JSON.stringify(person),
                'src': JSON.stringify(arrScreenShot),
                'time': new Date().toLocaleString(),
                'isObserv': $('#isObserv').val(),
            }
            $.post('{% url "sendMail" %}', JSON.stringify(pack)).then(res => console.log(res))
            // $.ajax({
            //   type: "POST",
            // url: '{% url 'sendMail' %}',
            //data: JSON.stringify(pack),
            //success: function (data, textStatus, jqXHR) {
            //  alert('DONE')
            //},
            //dataType: 'text',
            //async: true,
            //error: function (num) {
            //  alert("эБеда");
            //},
            //timeout:5000
            //{);
            //
            break;
        }
        case 'S_AccDiv': {
            break;
        }
        case'S_SaleDiv': {
            break;
        }
        case 'S_Devs' : {
            break;
        }
        default: {
            alert("Перед отправкой необходимо заполнить все поля формы")

            break;
        }
    }

})