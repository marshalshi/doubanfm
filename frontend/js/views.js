playListView = Backbone.View.extend({
        el: '#playarea',
        initialize: function(){
            this.model = new personalPlayList();
            this.model.fetch({
                    success: function(response){
                        for (var i in response.attributes ) {
                            play_list.push(response.attributes[i]);
                        }
                    },
                        error: function (){
                        alert("cannot fetch list");p
                    }
                });
        },
        events:{
            'click #next': 'nextSong'
        },
        nextSong: function(e){
            e.preventDefault();
            $('audio')[0].pause();
            $('source').attr('src', play_list[1].url);
            $('audio')[0].load();
        }
    });