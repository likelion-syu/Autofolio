window.__angular.module
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
.controller("pListCtrl" , ['$scope' , 'pService' , ($s , $serv) =>{
    $s.md = {
        portfolios : {
            items : []
        },
        drafts : {
            count : 0
        },
        theme :{
            list : []
        }
    }

    $s.fn = {
        init : function(){
            if($s.md.drafts.count === 0){
                $('#btn-modal-toggle').click();
            }
        },
        list : {
            get : function(){
                
            },
            del : function(item){
                if(confirm('삭제하시겠습니까?')){
                    $serv.list.del(item.pk)
                    .then(res=>{
                        console.log(res);
                    });
                }
            },
            repeat : function(item , elem){
                if(item.fields && item.fields.tags){
                    let splitted = item.fields.tags.split(',');
                    item.tags_splitted = splitted;
                }
                else{
                    item.tags_splitted = [];
                }
                let anchorTag = elem.find('.item-header-edit a');
                anchorTag.prop("href" , '/portfolio/update/' + item.pk);
            }
        }
    }

    $s.ext = {
        init : function(){
            $s.md.portfolios.items = window.__model.portfolios_serialized;
            $s.md.drafts.count = window.__model.drafts_count;
            $s.md.theme.list = window.__model.portfolios_related_serialized;
            console.log($s.md.theme.list)
            $s.$apply();    

            $s.fn.init();
        }
    }
}])

window.__angular.ext ={
    init : function(){
        angular.element($('.portfolio-list').eq(0)).scope().ext.init();
    }
}