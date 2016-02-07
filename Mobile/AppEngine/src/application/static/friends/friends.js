'use strict';

angular.module('myApp.friends', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/friends', {
    templateUrl: 'static/friends/friends.html',
    controller: 'friendsController'
  });
}])

.controller('friendsController', ['$scope', 'facebookService', function($scope, facebookService) {
    $scope.friends = [];

    facebookService.getFriends().then(function(friends){
        $scope.friends = friends;
    }, function(err) {
        console.log('An error occured while requesting friend list: ' + err);
    });

}]);
