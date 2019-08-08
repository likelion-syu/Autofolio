window.__angular_app
.directive('krInput', [ '$parse', function($parse) { return { priority : 2, restrict : 'A', compile : function(element) { element.on('compositionstart', function(e) { e.stopImmediatePropagation(); }); }, }; } ])
.controller('pDetailCtrl' , ['$scope' , function($s){
    $s.md = {
        tags : {
            list : [
                'tag1',
                'tag2',
            ],
            input : ""
        }
    }
    $s.fn = {
        tags : {
            init : function(){},
            remove : function(idx){
                // console.log(idx);
                // console.log($s.md.tags.list);
                $s.md.tags.list.splice(idx , 1);
            },
            insert : function(e){
                // console.log(e);
                if(e.keyCode === 13){
                    if($s.md.tags.input.trim() !== ""){
                        if($s.md.tags.list.length >= 5){
                            alert('태그는 5개 이상 등록할 수 없습니다.');
                            $s.md.tags.input = "";
                        }
                        else if($s.md.tags.input.indexOf(" ") >= 0){
                            alert("태그에는 공백이 입력될 수 없습니다.");
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
        init : function(){
            console.log($s.md.tags);
        }
    }
    $s.fn.init();
}]);