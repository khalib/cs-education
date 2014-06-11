var app = angular.module('gearfoo', []);

//app.controller('AppController', function ModeNotificationController($scope, modeNotificationService) {
    app.controller('AppController', function ModeNotificationController($scope) {
    $scope.modeTitle = '';

    $scope.displayModeNotification = function(modeTitle, callback) {
        $scope.modeTitle = modeTitle;
        $scope.modeNotificationBarDisplayed = true;
        $scope.callback = callback;
    }

    $scope.hideModeNotification = function() {
        $scope.modeTitle = '';
        $scope.modeNotificationBarDisplayed = false;

        if ($scope.callback) {
            $scope.callback();
        }
    }
});

/*
app.service('modeNotificationService', function() {
    this.reverse = function(name) {
        return name.split('').reverse().join('');
    }
});
*/

function ImageController($scope) {
    $scope.imagePostMode = 'view';
    $scope.pins = [];

    $scope.enableImageTagMode = function() {
        $scope.imagePostMode = 'tag';
        $scope.displayModeNotification('Tag Mode', $scope.disableImageTagMode);
    }

    $scope.disableImageTagMode = function() {
        $scope.imagePostMode = 'view';
    }

    $scope.enableImageEditMode = function() {
        $scope.imagePostMode = 'edit';
        $scope.displayModeNotification('Edit Mode', $scope.disableImageTagMode);
    }

    $scope.enableImageCommentTagMode = function() {
        $scope.imagePostMode = 'comment-tag';
        $scope.displayModeNotification('Comment Tag Mode', $scope.disableImageTagMode);
    }

    $scope.imageTagAdd = function(event) {
        var pin = {};
        pin.offsetX = 25 / 2;
        pin.offsetY = 25 / 2;
        pin.floatX = (event.pageX - event.currentTarget.offsetLeft) / event.currentTarget.clientWidth;
        pin.floatY = (event.pageY - event.currentTarget.offsetTop) / event.currentTarget.clientHeight;

        var image = {};
        image.width = event.currentTarget.clientWidth;
        image.height = event.currentTarget.clientHeight;
        image.offsetX = event.currentTarget.offsetLeft;
        image.offsetY = event.currentTarget.offsetTop;
        image.locationX = image.width * pin.floatX;
        image.locationY = image.height * pin.floatY;

        pin.image = image;
        $scope.pins.push(pin);

        if ($scope.imagePostMode == 'tag') {
            console.log(pinX);
            console.log(pinY);
        }

        /*
        console.log(event.pageX - event.currentTarget.offsetLeft);
        console.log(event.pageY - event.currentTarget.offsetTop);
        console.log(event.currentTarget.clientHeight);
        console.log(event.currentTarget.clientWidth);
        */
    }
}