var staat = {};
var grid = false;
//const url = "http://users.ugent.be/~sevbesau/cgi-bin/script.cgi?";
var url = "http://0.0.0.0:8080/cgi-bin/Sudokucgi.cgi?";



update = function(state) {

    // spelbord updaten
    for (let i = 0; i < 81; i++) {
        $('#' + i).text(state.spelbord[i])
    }

    // als er een bericht is, geef het dan weer
    if (state.message) {
        alert(state.message);
    }
    
    // state opslagen als stringweergave
    staat = JSON.stringify(state)
}


Startnew = function() {
    // start een nieuw spel
    fetch(url + "func=new_game")
    .then(function(response) {
        return response.json(); 
    })
    .then(function(myJson) {
        update(myJson);
    });
    
}

maakZet = function(staat, coord, waarde) {
    // maakt een zet op basis van de opgeslagen staat en de geselecteerde kleur
    fetch(url + 'func=do_move&' + 'state=' + staat + '&coord=' + coord + '&waarde=' + waarde)
    .then(function(response) {
        return response.json();
    })
    .then(function(myJson) {
        update(myJson);
    });
};


Startnew();


$(document).ready(function(){
    // word uitgevoerd wanneer alle html geladen is

    $(".tegel").click(function(e) {
        let coord = [Math.floor(e.target.id / 9), e.target.id%9]
        let waarde = $("#nummer").val()
        maakZet(staat, coord, waarde)    
    });
    

    $('#new').click(function(){
        Startnew();
    });

});
