window.__angular.module
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