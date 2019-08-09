window.__angular.module
.directive('krInput', [ '$parse', function($parse) { return { priority : 2, restrict : 'A', compile : function(element) { element.on('compositionstart', function(e) { e.stopImmediatePropagation(); }); }, }; } ])
.directive('runPerRepeating' , function(){
    return {
        scope: { 
            runPerRepeating : '=' ,
            runPerRepeatingSource : '='
        },
        link : (scope , elem , attrs) =>{
            scope.runPerRepeating(scope.runPerRepeatingSource , elem);
        } 
    }
})