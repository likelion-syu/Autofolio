window.__angular.module
// portfolio detail 관련 서비스 
.service('pService' , ['$http' , function($http){
    let config = {
        method : 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        detail : {
            'create' : {
                url : '/portfolio/api/create',
            },
        },
        list : {
            'delete' : {
                url : '/portfolio/api/delete',
            },
            'get' : {
                url : '/portfolio/api/get',
            }
        }
    }

    return {
        detail : {
            create : function(data){
                return $http({
                    method : config.method,
                    url : config.detail.create.url,
                    headers : config.headers,
                    data : data
                });
            },
        },
        list : {
            get : function(){
                return $http({
                    method : config.method,
                    url : config.list.get,
                    headers : config.headers
                });
            },
            del : function(pk){
                return $http({
                    method : config.method,
                    url : config.list.delete.url,
                    headers : config.headers,
                    data : {
                        "pk" : pk
                    }
                });
            },
        }
    }
}])
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
