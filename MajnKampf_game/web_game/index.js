let player_pos = [0,0]
const player_speed = 10;

let props = []

let player_inventory = []
let inv_open = false

generate_trees(25)
generate_stones(25)



function remove_items(){
  const items_all = document.getElementsByClassName("inv_item");

  while (items_all.length > 0) {
    items_all[0].remove();
  }
}
function load_items(){
 
  remove_items()
  for(const item of player_inventory){
  
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

  
  if (event.key == 'r') {
    // reagovat na stisknutí klávesy Enter


    remove_items()
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



  function prop_interact(){
    prop_class = document.getElementsByClassName("prop")

    for(const prop of props){
      radius_x = prevedZaporneNaKladne(prop[0] - player_pos[0])
      radius_y = prevedZaporneNaKladne(prop[1] - player_pos[1])

      if (radius_x < 20 && radius_y < 20){
        console.log("AHOJ")
      }
    }

  }
  

  function prevedZaporneNaKladne(cislo) {
    if (cislo < 0) {
      return -cislo;
    } else {
      return cislo;
    }
  }



 
  
  
function generate_trees(number){
    for (let i =0; i <= number; i++) {
      let  left = randomIntFromInterval(0,1980)
      let  top_y =  randomIntFromInterval(0,1980)
      props.push([left, top_y, 'tree'])
       $('.stones').append(
      `
      <div id="prop" class="prop tree" style="left: ${left}px; top: ${top_y}px;"><img src="assets/tree.png" width="120"></div>
      `
    )
    }
  
  }
  
  
  function generate_stones(number){
    for (let i =0; i <= number; i++) {
      let left = randomIntFromInterval(0,1980);
      let top_y =  randomIntFromInterval(0,1980)
      props.push([left, top_y, 'stone'])
       $('.stones').append(
      `
      <div id="prop" class="stone" style="left: ${left}px; top: ${top_y}px;"><img src="assets/stone.png" width="50"></div>
      `
    )
    }
  }
  
  
  function randomIntFromInterval(min, max) { // min and max included 
  return Math.floor(Math.random() * (max - min + 1) + min)
  }
 
  

/*
  $('.stones').append(
    `
    <div id="stone" style="left: ${l}px; top: ${t}px;"><img src="stone.png" width="50"></div>
    `
  )*/