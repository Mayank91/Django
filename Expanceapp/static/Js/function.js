$(document).ready(function(){
    $('#pr').hide();
    $('#pr1').hide();
    $('#pr2').hide();
    $('#div1').hide();
    $('#div2').hide();
    $('#div3').hide();

    $('#btn1').click(function(){
        $('#pr').toggle();
    });
    $('#btn2').click(function(){
        $('#pr1').toggle();
    });
    $('#btn3').click(function(){
        $('#pr2').toggle();
    });
    $('#btn1').click(function(){
        $('#pm').toggle();
    });
    $('#btndata1').click(function(){
        $('#div2').toggle(1000);
    });
    $('#btndata').click(function(){
        $('#div1').toggle(1000);
    });
    $('#btndata2').click(function(){
        $('#div3').toggle(1000);
    });



});