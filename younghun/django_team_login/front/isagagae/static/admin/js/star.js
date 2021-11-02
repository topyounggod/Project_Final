$(".star").on('click',function(){
    var idx = $(this).index();
    $(".star").removeClass("on");
    for(var i=0; i<=idx; i++){
    $(".star").eq(i).addClass("on");
    }
});