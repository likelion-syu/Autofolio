angular.module('afapp' , [])
.controller("pListCtrl" , ['$scope' , ($s) =>{
    console.log('Hello');

    $s.md = {

    }

    $s.fn = {
        init : function(){
            console.log('initialized');
        }
    }


    $s.fn.init();
}]);