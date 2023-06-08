let player_pos = [0,0]
const player_speed = 10;
let stone_pos = []

let player_inventory = []
let inv_open = false


async function remove_items(){
  console.log("REMOVED")
  const items = document.getElementsByClassName('inv_item')
  
  for(const x of items){
    x.remove()
  }

}
function load_items(){
 
  remove_items()
  for(const item of player_inventory){
    console.log("TEST")
    $('.item-list').append(
      `
      <div class="inv_item" id="itm">
    <span class="item_name">${item}</span>
  </div>
      `
    )
 
  }

}


document.addEventListener('keydown', function(event) {
  if (event.key == 'i') {
    if(inv_open == false){
      document.getElementById("inv").style.display = 'block';
      inv_open = true
      load_items()
     
    
    } else {
      console.log("NE")
     
      document.getElementById("inv").style.display = 'none';
      inv_open = false
    }
    console.log(inv_open)
  }

  if (event.key == 'g') {
    // reagovat na stisknutí klávesy Enter


    player_inventory.push('Test')
    load_items()
    console.log(player_inventory)
  } 
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
      stones = this.getElementsByClassName('stone')
      for(const stone_position of stone_pos){
        radius_x = stone_position[0] - player_pos[0]
        radius_y = stone_position[1] - player_pos[1]
        console.log(`X: ${radius_x}  y: ${radius_y}` )
        if (radius_x < 10 && radius_y < 10 ){
          console.log("RADIUS TRUE")
          for(const stone of stones){
            console.log(`left: ${stone.style.left}   ${stone_position[0]}px` )
            console.log(`top: ${stone.style.top}   ${stone_position[1]}px` )
            if(`${stone.style.left}` == `${stone_position[0]}px` && `${stone.style.top}` == `${stone_position[1]}px`){
              console.log("STONE TRUE")
              stone.remove()
              player_inventory.push(['Stone'])
            }
          }
        }
      }
    } 
  });
  function randomIntFromInterval(min, max) { // min and max included 
    return Math.floor(Math.random() * (max - min + 1) + min)
  }
  

  for (let i =0; i <= 100; i++) {
    left = randomIntFromInterval(0,1980);

    kokot_top =  randomIntFromInterval(0,1980)
    console.log(kokot_top)
    stone_pos.push([left, kokot_top])
     $('.stones').append(
    `
    <div id="stone" class="stone" style="left: ${left}px; top: ${kokot_top}px;"><img src="stone.png" width="50"></div>
    `
  )
  }



/*
  $('.stones').append(
    `
    <div id="stone" style="left: ${l}px; top: ${t}px;"><img src="stone.png" width="50"></div>
    `
  )*/