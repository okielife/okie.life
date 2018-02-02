// create an angular module to hold everything for this page
// note to self, if we split things across JS files, calling angular.module with just a name won't create a new app
var app = angular.module('pictionaryApp', []);

// configure the module to use a different template interpolation sequence to avoid conflicting with Django
app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

// configure the module to perform C.S.R.F. operations nicely with Django
app.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

// create a controller containing functions and variables made available in the controller's scope
app.controller('pictionaryController', ['$scope', '$http', function ($scope, $http) {
    "use strict";

    $scope.current_word = {word: 'Initialized'};
    $scope.enable_voting = false;

    // Variables and functions for the E+ task section
    $scope.up_vote = function (word_id) {
        $http.post('/pictionary/up_vote/', {pk: word_id});
    };

    // Variables and functions for the E+ task section
    $scope.down_vote = function (word_id) {
        $http.post('/pictionary/down_vote/', {pk: word_id});
    };

    // Variables and functions for the E+ task section
    $scope.get_word = function () {
        $http.get('/pictionary/get_word/')
            .then(function (response) {
                $scope.current_word = response.data.word;
                $scope.enable_voting = true;
            });
    };
    $scope.get_word();

    $scope.current_time = "Click to start";
    $scope.timer = null;

    $scope.reset_timer = function () {

        if ($scope.timer) {
            clearInterval($scope.timer);
            $scope.timer = null;
        }

        $scope.current_time = "Starting Timer...";

        // Set the date we're counting down to, including a padding time
        var timer_length = 60000; // 1 minute
        var time_padding = 1500; // 1.5 seconds
        var countDownDate = Date.now() + timer_length + time_padding;

        // Update the count down every 1 second
        $scope.timer = setInterval(function () {

            // Get today's date and time
            var now = new Date().getTime();

            // Find the distance between now an the count down date
            var distance = countDownDate - now;

            // Time calculations for days, hours, minutes and seconds
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the element with id="demo"
            if (seconds === 0) {
                seconds = '00';
            } else if (seconds < 10) {
                seconds = '0' + seconds;
            }
            $scope.current_time = minutes + ":" + seconds;

            // If the count down is finished, write some text
            if (distance < 0) {
                clearInterval($scope.timer);
                $scope.timer = null;
                $scope.current_time = "OUT OF TIME";
                document.getElementById("demo").style.color = "red";
            }
            $scope.$apply();
        }, 1000);
    }

}]);
