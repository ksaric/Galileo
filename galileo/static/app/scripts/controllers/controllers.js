'use strict';

angular.module('galileo.controllers', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider

            .when('/home', {
                templateUrl: '/static/js/app/views/home.html',
                controller: 'HomeCtrl'})

            .when('/computers', {
                templateUrl: '/static/js/app/views/computers.html',
                controller: 'ComputersCtrl'})

            .when('/databases', {
                templateUrl: '/static/js/app/views/databases.html',
                controller: 'DatabasesCtrl'})

            .when('databases/users/', {
                templateUrl: '/static/js/app/views/users.html',
                controller: 'PortsCtrl'})

            .when('/databases/tablespaces/', {
                templateUrl: '/static/js/app/views/tablespaces.html',
                controller: 'PortsCtrl'})

            .when('/ports/:computerId', {
                templateUrl: '/static/js/app/views/ports.html',
                controller: 'PortsCtrl'})
        ;
    }])

    .controller('HomeCtrl', function ($scope, Restangular) {
    })

    .controller('ComputersCtrl', function ($scope, Restangular) {
        var computers = Restangular.all('computer');

        computers.customGET().then(function (computers) {
            $scope.computers = computers['objects'];
        });
    })

    .controller('DatabasesCtrl', function ($scope, Restangular) {
        var databases = Restangular.all('database');

        databases.customGET().then(function (databases) {
            $scope.databases = databases['objects'];
        });
    })

    .controller('PortsCtrl', function ($scope, $routeParams, Restangular) {
        //  api/computer/2/ports
        var computerId = $routeParams.computerId;

        var testing = Restangular.all('computer/' + computerId + '/ports');

        testing.customGET().then(function (ports) {
            $scope.ports = ports['objects'];
        });
    })


;