let player_pos = [0,0]
const player_speed = 10;
let stone_pos = [100, 100]


document.addEventListener('keydown', function(event) {
    if (event.key == 'd') {
      // reagovat na stisknutí klávesy Enter
      player_pos[0] += player_speed
      


      document.getElementById('player').style.left =  `${player_pos[0]}px`
    } 
    if (event.key == 'a') {
      // reagovat na stisknutí klávesy Enter
      player_pos[0] -= player_speed
      
      document.getElementById('player').style.left =  `${player_pos[0]}px`
    } 
    if (event.key == 's') {
      // reagovat na stisknutí klávesy Enter
      player_pos[1] += player_speed
     
      document.getElementById('player').style.top =  `${player_pos[1]}px`
    } 
    if (event.key == 'w') {
      // reagovat na stisknutí klávesy Enter
      player_pos[1] -= player_speed
 
      document.getElementById('player').style.top =  `${player_pos[1]}px`
    } 
    if (event.key == 'e') {
      // reagovat na stisknutí klávesy Enter
      if (player_pos[0] - stone_pos[0] < 10 && player_pos[1] - stone_pos[1] < 5){
        console.log("STone")
      }
   
    } 
  });




  $(".terrain").append
(`
<div id="stone" style="left: ${stone_pos[0]}px; right: ${stone_pos[1]}px"> STONE</div>
`);

