'use strict';

angular.module('myApp')
    .service('facebookService', ['$http', '$q', function($http, $q) {
    var self = this;

    self.getFriends = function() {
      return $q(function(resolve, reject) {
        $http.get('/api/friends').then(function(response){
          resolve(response.data.friends);
        }, function(err) {
          reject(err);
        });
      });
    };

    return self;
}]);
