var questions = angular.module('questions', ['ngRoute']);
questions.config(function($interpolateProvider){
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
});
questions.config(['$routeProvider',
	function($routeProvider) {
		$routeProvider.
			when('/', {
				templateUrl: '/static/partials/questions-list.html',
				controller: 'ListCtrl'
			}).
			when('/:questionId', {
				templateUrl: '/static/partials/question-detail.html',
				controller: 'DetailCtrl'
			});
  }]);
questions.controller('ListCtrl', function ($scope, $http, $location){

	$scope.loadQuestions = function() {
		$scope.questions = []
		$http.get('api').then(function(response){
			$scope.questions = response.data;
		});
	};
	
	$scope.sorter = 'id';
	$scope.field = 'title';
	$scope.queryFunc = function(field) {
		return field
	}
	$scope.loadQuestions();
	
	$scope.goat = function(question){
		$location.path(String(question.id));
	};
});

questions.controller('DetailCtrl', function ($scope, $http, $routeParams){

	$scope.loadQuestionDetail = function() {
		$scope.question = []
		$scope.question_id = $routeParams.questionId
			$http.get('api/'.concat($scope.question_id)).then(function(response){
				$scope.question = response.data;
			});
		};
	$scope.cur = Number($routeParams.questionId);
	$scope.loadQuestionDetail();
	$scope.assaf = $routeParams.questionId
});