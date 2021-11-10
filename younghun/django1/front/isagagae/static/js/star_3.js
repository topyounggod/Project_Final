
//$(window).on('load', function(){
//    // 별점 색칠하기 (true)
//    $('.rating').children('.rate_radio').on('click', function(){
//        for(var k=0; k<$('.rating').length; k++){
//            var $rate_radio = $(".rating").eq(k).children('.rate_radio')
//            $rate_radio.each(function(i){
//               this.checked = false;
//               console.log(this.checked)
//                   })
//               }
//            })
//        });

$(window).on('load', function(){

//    $('rating').children('.rate_radio').on('click', function(){
//        this.checked = false;
//    });

    $('.rating').children('.rate_radio').on('click', function(e){
        // 클릭한 별
        var $this = $(this)
        // 클릭한 별을 가진 부모의 자식요소 체크박스들 (별 한줄)
        var $parent = $this.parent().children('input')
        // 한줄 모두 체크해제
        $parent.each(function(idx, ele){
            ele.checked = '';
        })
        // 클릭한 별 전까지 체크
        $parent.each(function(idx, ele){
            if (ele.title == $this.prop('title')){
                ele.checked = 'true';
                return false;
            } else {
                ele.checked = 'true';
            }
        })
        /*for(var k=0; k<$('.rating').length; k++){
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
            //



        }*/
    })
    });


// 최신 코드
//$(window).on('load', function(){
//    // 별점 색칠하기 (true)
//    $('.rating').children('.rate_radio').on('click', function(){
//    //
//        for(var k=0; k<$('.rating').length; k++){
//            var $rate_radio = $(".rating").eq(k).children('.rate_radio')
//            $rate_radio.each(function(i){
//               if(this.checked){
//                   for (var j = 0; j < i; j++) {
//                       $rate_radio.eq(j).prop('checked', true)
//                   }
//                   //console.log($('input:checkbox[name=rating]:checked').length)
//                   //var $rates = $('input:checkbox[name=rating]:checked').length
//               }
//
//            });
//        }
//    })
//    // 별점 갯수 구하기
//    $("#countstar").click(function(){
//        var $par = $(".rating");
//        var results = [];
//        let count = 0
//        for (var i = 0; i < $par.length; i++) {
//            $chd = $par.eq(i).children('.rate_radio');
//            for (var j = 0; j < $chd.length; j++) {
////                console.log(this.('input[type="checkbox"]:checked').length)
//                console.log($chd.eq(j).prop('checked')==true);
//
////                console.log($(chd.eq(j).prop('checked')==true).length)
////                console.log($chd.eq(j).attr('checked'));
////                var countCheckedCheckboxes = this.filter(':checked').length;
////                console.log(countCheckedCheckboxes);
//
////                console.log(($chd.eq(j).prop('checked')==true).size());
////                  console.log((this.prop('checked')==true).length)
////                  console.log($(''))
//            }
//            // true인 갯수를 세서, 배열에 저장
//        }
//        // 보내기
//    });
//
//});
