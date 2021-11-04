//document.getElementById('H_rating1').onclick = function(){
//    alert('별,,별,,별,,별하나에 추억과 별 하나에 시와 별 하나에 어머니,,')
//};

/*
document.getElementsByClassName('rate_radio').onclick = function(){
    var items = document.getElementsByClassName('rate_radio');
    items.forEach(function(item,index){
        console.log(item, index)
        if(index < items){
            item.checked = true;
        }else{
            item.checked = false
        }
    })
};
*/
//$(".rate_radio").on('click', function(){
//    alert("?")
//})

$(".rate_radio").each(function(i, items){
    //console.log(items)
    $(this).on('click',function(){
        //console.log($(this))
            $(this).each(function(){
                console.log($(this))
                //$(this)의 상위 요소 중 가장 근접한 하나를 반환
                //console.log($(this).closest('div'))
                //console.log($(this).closest('div').children('input').checked = true)
                //$(this).closest('div').children('input').checked = true
                //
                console.log($(this).closest('div').children('input'))
                console.log($('input:checkbox[name=rating]:checked').closest('div').children('input').index('input'))
                console.log($('input:checkbox[name=rating]:checked').closest('div').children('input').index('input:checkbox[name=rating]'))
//                console.log($(this).closest('div').children('input').index('input:checkbox[name=rating]:checked'))
//                console.log(($(this).closest('div').children('input').checked == true).index('input'))
                for (var i = 0; i < $(this).closest('div').children('input').index('input'); i++){
                    $(this).closest('div').children('input').eq(i).checked = true
                }
                /*
                if($(this).closest('div').children('input').checked = true) {
                    $(this).parents('class').children('input').checked = true;
                }else{
                    $(this).parents('class').children('class').checked = false;
                } */

            }) // children : 바로 아래 요소, 자식 요소만 찾을 때
    });
})

// 클릭한 애의 부모 클래스 찾아가기 -> 그 부모클래스의 자식클래스 중에 클릭 이벤트 들어간 거까지 체크 되게