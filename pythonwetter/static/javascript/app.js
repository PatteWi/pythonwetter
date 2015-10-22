Ember.Handlebars.registerHelper('linkTo', Ember.Handlebars.helpers['link-to']);
App = Ember.Application.create({
    //LOG_TRANSITIONS: true,

    // Extremely detailed logging, highlighting every internal
    // step made while transitioning into a route, including
    // `beforeModel`, `model`, and `afterModel` hooks, and
    // information about redirects and aborted transitions
    //LOG_TRANSITIONS_INTERNAL: true,
    LOG_VIEW_LOOKUPS: true
});

App.Router.map(function() {
    // put your routes here

    //this.route("index", {path: /index/});
    //this.route("weather", {path: /weather/});

    this.route("comment", {path: /comment/});
    this.resource("weathers", { path: "/weathersearch"}, function(){
        this.resource("weather", { path: "/weather"});
    });
});

App.Router.reopen({
    location: 'history'
});

App.WeathersRoute = Ember.Route.extend({

    model: function (param) {
        return $.getJSON('http://pythonwetter-zwergchief.rhcloud.com/weathers/?search=' + param.datum + "," + param.stadt)
        //return $.getJSON('http://127.0.0.1:8000/weathers/?search=' + param.datum + "," + param.stadt)

    }
});

App.WeathersController = Ember.ArrayController.extend({
    queryParams: ["datum", "stadt"],
    options: [1, 2, 3, 4, 5, 6],
    isComment: false,
    text:null,
    user: null,
    bewertung:null,
    commentdatum:null,

    actions: {
        clickComment: function () {
            this.set('isComment', true);
        },

        createTodo: function(){
            var wetterid = 'http://pythonwetter-zwergchief.rhcloud.com/weathers/'+ this.get('wid') + '/';
            var text = this.get('kommentar');
            var user = this.get('user');
            var bewertung = this.get('bewertung');
            var commentdatum = this.get('commentdatum');
            var controller = this.controller;
            //var csrf = $.cookie('csrftoken')
            $.ajax({
                //xhrFields: {withCredentials: true},
                //url: 'http://127.0.0.1:8000/comments/',
                url: 'http://pythonwetter-zwergchief.rhcloud.com/comments/',
                type: 'POST',
                contentType: "application/json;",
                data: JSON.stringify({bewertung: bewertung, commentdatum: commentdatum, wetter: wetterid, kommentar: text, user: user}),
                success: function() {
                    window.location.reload(true);
                }
            });
        }
    }
});

Ember.Handlebar.helper('format-date', function(date){
    return moment.unix(date).fromNow();
});