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
.service('pDetailService' , ['$http' , function($http){
    let config = {
        url : '/portfolio/api/create',
        method : 'POST'
    }    
    return {
        create : function(data){
            return $http({
                method : config.method,
                url : config.url,
                data : data,
                headers : {
                    'Content-Type' : 'application/json'
                }
            });
        }
    }
}])
.controller('pDetailCtrl' , ['$scope' , 'pDetailService' , 'pService' , function($s , $conn , $serv){
    
    $s.md = {
        title : '',
        share_state : false,
        tags : {
            list : [],
            input : ""
        },
        drafts : {
            list : [],
            selected : {},
            search : ''
        },
        themes : {
            list : [],
            selected : {},
        }
    }
    $s.fn = {
        set : function(){
            $s.md.themes.list = window.__model.themes_serialized;
            $s.md.drafts.list = window.__model.drafts_serialized;
            $s.$apply();
        },
        drafts : {
            select : function(item){
                $s.md.drafts.selected = item;
                console.log($s.md.drafts.selected);
            }
        },
        themes : {
            select : function(item){
                $s.md.themes.selected = item;
                console.log($s.md.themes.selected);
            }
        },
        tags : {
            init : function(){},
            remove : function(idx){
                $s.md.tags.list.splice(idx , 1);
            },
            insert : function(e){
                if(e.keyCode === 13){
                    if($s.md.tags.input.trim() !== ""){
                        if($s.md.tags.list.length >= 5){
                            alert('태그는 5개 이상 등록할 수 없습니다.');
                            $s.md.tags.input = "";
                        }
                        else if($s.md.tags.input.indexOf(" ") >= 0){
                            alert("태그에는 공백이 입력될 수 없습니다.");
                        }
                        else if($s.md.tags.list.indexOf($s.md.tags.input) >= 0){
                            alert('이미 등록된 태그입니다.');
                        }
                        else{
                            $s.md.tags.list.push(
                                $s.md.tags.input.trim()
                            );
                            $s.md.tags.input = "";
                        }
                    }
                }
            },
        },
        common : {
            valid : function(){
                // title 
                if($s.md.title.trim().length <= 0){ 
                    alert('제목을 입력해주세요');
                    $('#portfolio_title').focus();
                    return false; 
                }
                else if(!$s.md.drafts.selected.pk){ 
                    alert('작성할 드래프트를 선택해주세요');
                    return false; 
                }
                else if(!$s.md.themes.selected.pk){ 
                    alert('작성할 테마를 선택해주세요')
                    return false; 
                }
                else { return true; }
            },
            submit : function(){
                if($s.fn.common.valid()){
                    let data = {};
                    data.title = $s.md.title.trim();
                    data.share_state = $s.md.share_state;
                    data.tags = $s.md.tags.list.join();
                    data.draft = $s.md.drafts.selected;
                    data.theme = $s.md.themes.selected;
                    $serv.detail.create(data)
                    .then(function(res){
                        if(res.data.result === 1){
                            alert('생성되었습니다.');
                            location.href= "/portfolio";
                        }
                    })
                }
                console.log($s.md);
            }
        },
        init : function(){
            console.log($s.md.tags);
        }
    }
    $s.fn.init();
}]);

window.__angular.ext = {
    set : function(){
        angular.element($('.portfolio-detail').eq(0)).scope().fn.set();
    }
}