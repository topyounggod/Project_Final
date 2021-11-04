//별점 마킹 모듈 프로토타입으로 생성
//function Rating(){};
//Rating.prototype.rate = 0;
//Rating.prototype.setRate = function(newrate){
//    //별점 마킹 - 클릭한 별 이하 모든 별 체크 처리
//    this.rate = newrate;
//    let items = document.querySelectorAll('.rate_radio');
//    items.forEach(function(item, idx){
//        if(idx < newrate){
//            item.checked = true;
//        }else{
//            item.checked = false
//        }
//    });
//}
//
//let rating = new Rating();//별점 인스턴스 생성

var items = document.querySelectorAll('.rate_radio');
var ratings = document.querySelectorAll('.rating');
var tmp = document.querySelector('.rating');
console.log(items);
console.log(ratings);
console.log(tmp);
console.log(tmp.querySelectorAll('.rate_radio'));


document.addEventListener('DOMContentLoaded', function(){
    //별점선택 이벤트 리스너
//    document.querySelector('.rating').addEventListener('click',function(e){
//        let elem = e.target;
//        console.log(elem)
//        if(elem.classList.contains('rate_radio')){
//            rating.setRate(parseInt(elem.value));
//        }
//    });

    for(var i=0; i<ratings.length; i++) {
        ratings[i].addEventListener('click',function(e){
            var elem = e.target;
//            console.log(elem.value);
            var parent = elem.parentElement;
//            console.log(parent);
            if(elem.classList.contains('.rate_radio')){
                setRate(parent, parseInt(elem.value));
            }
        });
    }

});


function setRate(parent, newrate) {
    //별점 마킹 - 클릭한 별 이하 모든 별 체크 처리
//    this.rate = newrate;
    console.log(parent);
    var items = parent.querySelectorAll('.rate_radio');
    console.log(items);
    items.forEach(function(item, idx){
        if(idx < newrate){
            item.checked = true;
        }else{
            item.checked = false;
        }
    });
}

function counting() {
    let count = 0;
    var counting_obj = document.querySelectorAll('.rate_radio');
//    var counting_obj = document.getElementsByName("rating");
    var counting_leng = counting_obj.length;
    var checked = 0;
    for (i=0; i < counting_leng; i++) {
        if (counting_obj[i].checked == true) {
            checked += 1;
//            count++;
        }
    }
    console.log("checked " ,checked);
//    console.log(count);
    if (checked < 0 ) {
        alert("항목을 선택해주세요");
        return;
    }
    //post
//    var form = document.createElement('form');
//    form.setAttribute('method' , 'post');
//    form.setAttribute('action' , 'user/savestar')
//    document.charset = "utf-8"
//
//    //
//    console.log("test2233")
//    for (var key in params){
//        var hiddenField = document.create('input')
//        console.log(key)

    //}

//      location.href="user/savestar/"
    location.href="user/savestar/?checked="+checked;
}

//location.href="search.jsp?type="+type+"&type2=type"+type2;
//document.getElementById("checked").innerHTML = "출력";


//function Rating(newrate){
//    let items = document.querySelectorAll('.rate_radio');
//    items.forEach(function (item, idx){
//        if(idx < newrate){
//            item.checked = true;
//        }else{
//            item.checked = false
//        }
//    });
//}

//let rating = new Rating
//
//document.addEventListener('DOMContentLoaded', function(){
//    // 별점선택 이벤트 리스터
//    document.querySelector('.rating').addEventListener('click', function(e){
//        let elem = e.target;
//        console.log(elem)
//        if(elem.classList.contains('.rate_radio')){
//            rating.setRate(parseInt(elem.value));
//        }
//    })
//});

//$('document').ready(function (){
//    $('button').click(function(){
//        function Rating(){newrate};
//        Rating.prototype.rate = 0;
//        Rating.prototype.setRate = function(newrate){
//    //별점 마킹 - 클릭한 별 이하 모든 별 체크 처리
//        this.rate = newrate;
//        let items = document.querySelectorAll('.rate_radio');
//        items.forEach(function(item, idx){
//            if(idx < newrate){
//                item.checked = true;
//            }else{
//                item.checked = false
//            }
//        });
//}
//
//        let rating = new Rating();//별점 인스턴스 생성
//
//
//        document.addEventListener('DOMContentLoaded', function(){
//   //별점선택 이벤트 리스너
//        let ratings = document.querySelector('.rating')
//        ratings.addEventListener('click',function(e){
//        let elem = e.target;
//        console.log(elem)
//        if(elem.classList.contains('rate_radio')){
//            rating.setRate(parseInt(elem.value));
//        }
//    });
//});
//
//
//        function counting() {
//        let count = 0;
//        var counting_obj = document.querySelectorAll('.rate_radio');
////    var counting_obj = document.getElementsByName("rating");
//        var counting_leng = counting_obj.length;
//        var checked = 0;
//        for (i=0; i < counting_leng; i++) {
//            if (counting_obj[i].checked == true) {
//                checked += 1;
////            count++;
//        }
//    }
//    console.log("checked " ,checked);
////    console.log(count);
//    if (checked < 0 ) {
//        alert("항목을 선택해주세요");
//        return;
//    }
//
//
//    location.href="user/savestar/?checked="+checked;
//}
//    })
//})




///////
//2번시도

//    function Rating2(){};
//    Rating2.prototype.rate = 0;
//    Rating2.prototype.setRate = function(newrate2){
//    //별점 마킹 - 클릭한 별 이하 모든 별 체크 처리
//    this.rate = newrate2;
//    let items2 = document.querySelectorAll('.rate_radio2');
//    items2.forEach(function(item, idx){
//        if(idx < newrate2){
//            item.checked = true;
//        }else{
//            item.checked = false
//        }
//    });
//}
//
////let rating2 = new Rating2();//별점 인스턴스 생성
//
//
//    document.addEventListener('DOMContentLoaded', function(){
//   //별점선택 이벤트 리스너
//        let ratings2 = document.querySelector('.rate_radio2')
//        ratings2.addEventListener('click',function(e){
//        let elem2 = e.target;
//        console.log(elem2)
//        if(elem2.classList.contains('rate_radio2')){
//            rating.setRate(parseInt(elem2.value));
//        }
//    });
//});
//
//
//    function counting2() {
//    let count = 0;
//    var counting_obj = document.querySelectorAll('.rate_radio2');
////    var counting_obj = document.getElementsByName("rating");
//    var counting_leng = counting_obj.length;
//    var checked = 0;
//    for (i=0; i < counting_leng; i++) {
//        if (counting_obj[i].checked == true) {
//            checked += counting_obj[i].value
//        }
//    }
//    console.log("checked " ,checked);
////    console.log(count);
//    if (checked < 0 ) {
//        alert("항목을 선택해주세요");
//        return;
//    }
//
//
//    location.href="user/savestar/?checked="+checked;


