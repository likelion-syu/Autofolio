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
.directive('runPerRepeating' , function(){
    return {
        scope: { 
            runPerRepeating : '=' ,
            runPerRepeatingSource : '='
        },
        link : (scope , elem , attrs) =>{
            scope.runPerRepeating(scope.runPerRepeatingSource);
            
        } 
    }
})
.controller("pListCtrl" , ['$scope' , ($s) =>{
    $s.md = {
        portfolios : {
            items : []
        },
        drafts : {
            count : 0
        }
    }

    $s.fn = {
        init : function(){
            if($s.md.drafts.count === 0){
                $('#btn-modal-toggle').click();
            }
        },
        list : {
            close : function(){

            },
            repeat : function(item){
                if(item.fields && item.fields.tags){
                    let splitted = item.fields.tags.split(',');
                    item.tags_splitted = splitted;
                }
                else{
                    item.tags_splitted = [];
                }
            }
        }
    }

    $s.ext = {
        init : function(){
            $s.md.portfolios.items = window.__model.portfolios_serialized;
            $s.md.drafts.count = window.__model.drafts_count;
            $s.$apply();    

            $s.fn.init();
        }
    }
}])
.filter('momentFromNow', function () {
    return function (item) {
        let currentMoment = moment(item);
        // console.log(item , currentMoment);
        return currentMoment.fromNow();
    };
});

window.__angular ={
    init : function(){
        angular.element($('.portfolio-list').eq(0)).scope().ext.init();
    }
}