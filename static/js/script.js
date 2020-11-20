$(document).ready(function () {
    $('.modal').modal();
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip({
        'inDuration': 500,
        'transitionMovement': 0,

    });



    $(document).scroll(function (e) {
        var scrollAmount = $(window).scrollTop();
        var documentHeight = $(document).height();
        var windowHeight = $(window).height();
        var scrollPercent = (scrollAmount / (documentHeight - windowHeight)) * 100;

        // For scrollbar 1
        $(".scrollBar1").css("width", scrollPercent + "%");

        // For scrollbar 2
        $(".scrollBar2").css("width", scrollPercent + "%");
    });







});