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
.controller('pUpdateCtrl' , ['$scope' , 'pService' , ($s , $serv) =>{
    
    $s.md = {
        title : '',
        pk : -1,
        share_state : false,
        portfolio : {},
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
            // $s.md.portfolio = window.__model.portfolio_serialized;
            let portfolio = window.__model.portfolio_serialized[0].fields;
            
            $s.md.title = portfolio.title;
            $s.md.pk = window.__model.portfolio_serialized[0].pk;
            if(portfolio.tags !== ''){
                let splitted = portfolio.tags.split(',');
                splitted.map(item =>{
                    $s.md.tags.list.push(item);
                });
            }

            $s.md.themes.list = window.__model.themes_serialized;
            $s.md.drafts.list = window.__model.drafts_serialized;

            $s.md.drafts.list.map(item=>{
                // console.log(item.pk === portfolio.draft);
                if(item.pk === portfolio.draft){
                    $s.md.drafts.selected = item;
                }
            });

            $s.md.themes.list.map(item=>{
                if(item.pk === portfolio.theme){
                    $s.md.themes.selected = item;
                }
            });

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
                    data.draft = $s.md.drafts.selected.pk;
                    data.theme = $s.md.themes.selected.pk;                    
                    data.pk = $s.md.pk;

                    $serv.detail.update(data)
                    .then(function(res){
                        console.log(res);
                        if(res.data.result > 0){
                            alert('수정되었습니다.');
                            location.href= "/portfolio"; 
                        }
                    });
                }
                // console.log($s.md);
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