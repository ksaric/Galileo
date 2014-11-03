'use strict';

/**
 * @ngdoc overview
 * @name galileoApp
 * @description
 * # galileoApp
 *
 * Main module of the application.
 */
angular
    .module('galileoApp', [
        'ngAnimate',
        'ngCookies',
        'ngResource',
        'ngRoute',
        'ngSanitize',
        'ngTouch',
        'restangular',
        'galileo.controllers'
    ])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/home'});
    }])

    .config(function (RestangularProvider) {
        RestangularProvider.setBaseUrl('/api');
    });






