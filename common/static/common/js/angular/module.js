window.__angular = {};
window.__angular.module = angular.module('afapp' , [])
.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});