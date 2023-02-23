function set_game_id(url){
    $.get(url, function(data){
        game_id = data["game_id"]
        $("p#game_id").text("Game ID: " + game_id);
        $("input#game_id").val(game_id);
    });
}


function show_game_form(){
    $(document).ready(function(){
        $("div#game_form").show();
    });
}


alert("Click button to start new game!")

set_game_id("http://127.0.0.1:8000/hide");
show_game_form();
