
$(window).on('load', function(){
    // 별점 색칠하기 (true)
    $('.rating').children('.rate_radio').on('click', function(){
        for(var k=0; k<$('.rating').length; k++){
            var $rate_radio = $(".rating").eq(k).children('.rate_radio')
            $rate_radio.each(function(i){
               if(this.checked){
                   for (var j = 0; j < i; j++) {
                       $rate_radio.eq(j).prop('checked', true)
                   }
                   //console.log($('input:checkbox[name=rating]:checked').length)
                   //var $rates = $('input:checkbox[name=rating]:checked').length
               }

            });
        }
    })
    // 별점 갯수 구하기
    $("#countstar").click(function(){
        var $par = $(".rating");
        var results = [];
        let count = 0
        for (var i = 0; i < $par.length; i++) {
            $chd = $par.eq(i).children('.rate_radio');
            for (var j = 0; j < $chd.length; j++) {
//                console.log(this.('input[type="checkbox"]:checked').length)
                console.log($chd.eq(j).prop('checked')==true);

//                console.log($(chd.eq(j).prop('checked')==true).length)
//                console.log($chd.eq(j).attr('checked'));
//                var countCheckedCheckboxes = this.filter(':checked').length;
//                console.log(countCheckedCheckboxes);

//                console.log(($chd.eq(j).prop('checked')==true).size());
//                  console.log((this.prop('checked')==true).length)
//                  console.log($(''))
            }
            // true인 갯수를 세서, 배열에 저장
        }
        // 보내기
    });

});








// 최신 코드
//$(function(){
//    $('.rating').children('.rate_radio').on('click', function(){
//
//        for(var k=0; k<$('.rating').length; k++){
//            var $rate_radio = $(".rating").eq(k).children('.rate_radio')
//            $rate_radio.each(function(i){
//               if(this.checked){
//                   for (var j = 0; j < i; j++) {
//                       $rate_radio.eq(j).prop('checked', true)
//                   }
////                   console.log($('input:checkbox[name=rating]:checked').length)
//               }
//
//            });
//    }
//        })
//        var $rates = $('input:checkbox[name=rating]:checked').length
//        console.log($rates)
//        location.href="user/savestar/?checked="+$rates;
////
//}
//);


// 원래 코드

//$(function(){
//    $('.rating').children('.rate_radio').on('click', function(){
//
//        var $rate_radio = $(".rating").eq(0).children('.rate_radio')
//        $rate_radio.each(function(i){
//           if(this.checked){
//               for (var j = 0; j < i; j++) {
//                   $rate_radio.eq(j).prop('checked', true)
//               }
//           }
//        });
//
//    })
//
//});