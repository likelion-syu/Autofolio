window.__angular.module
// moment를 이용해 현재까지 일자를 출력함
.filter('momentFromNow', function () {
    return function (item) {
        let currentMoment = moment(item);
        return currentMoment.fromNow();
    };
});
