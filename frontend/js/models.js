
personalPlayList = Backbone.Model.extend({
        initialize: function(){
            this.url = "json/";
        },
        parse: function(response, options){
            return response.song;
        }
    });
