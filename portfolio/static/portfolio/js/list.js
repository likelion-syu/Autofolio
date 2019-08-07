window.__angular_app
.directive('myRepeatDirective', function() {
    return function(scope, element, attrs) {
        if (scope.$last){
            window._swiper = new Swiper('.swiper-container', {
                slidesPerView: 3,
                spaceBetween: 30,
                pagination: {
                  el: '.swiper-pagination',
                  clickable: true,
                },
              });
        }
    };
})
.controller("pListCtrl" , ['$scope' , ($s) =>{
    console.log('Hello');

    $s.md = {
        items : [
            { thumbnail : 'thumbnail' , title : 'title' , created_dt : (new Date()) },
            { thumbnail : 'thumbnail' , title : 'title' , created_dt : (new Date()) },
            { thumbnail : 'thumbnail' , title : 'title' , created_dt : (new Date()) },
            { thumbnail : 'thumbnail' , title : 'title' , created_dt : (new Date()) }
        ],
        swiper : {}
    }

    $s.fn = {
        init : function(){
            console.log('initialized');

        }
    }


    $s.fn.init();
}]);