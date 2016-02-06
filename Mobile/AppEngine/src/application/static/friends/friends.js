'use strict';

angular.module('myApp.friends', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/friends', {
    templateUrl: 'static/friends/friends.html',
    controller: 'friendsController'
  });
}])

.controller('friendsController', ['$scope', '$http', function($scope, $http) {
  $scope.friends = [];

    $http.get('/api/friends').then(function(response){
        $scope.friends = response.data.friends;
        console.log(response.data);
    }, function() {
        console.log('An error occured while requesting friend list');
    })

}]);
