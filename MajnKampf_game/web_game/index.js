let player_pos = [0,0]
const player_speed = 10;
let stone_pos = []


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
  function randomIntFromInterval(min, max) { // min and max included 
    return Math.floor(Math.random() * (max - min + 1) + min)
  }
  

  for (let i =0; i <= 5; i++) {
    left = randomIntFromInterval(0,500)
    top = randomIntFromInterval(0,500)
    stone_pos.push([left, top])
  }



/*
  $('.stones').append(
    `
    <div id="stone" style="left: ${l}px; top: ${t}px;"><img src="stone.png" width="50"></div>
    `
  )*/