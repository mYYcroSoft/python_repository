if (event.key == 'e') {
    stones = this.getElementsByClassName('stone')
    // reagovat na stisknutí klávesy Enter
    for(const pos of stone_pos){
      console.log(player_pos)
      postion_between = [pos[0] - player_pos[0], pos[1] - player_pos[1]]
      console.log(postion_between)
      if (postion_between[0] < 2 && postion_between[1] < 2){
        for (const stone of stones){
          console.log(`Stone left: ${stone.style.left}  Stone top: ${stone.style.top} `)
          console.log(`Between left: ${postion_between[0]} Between top:   ${postion_between[1]}`
          )

       
          if(Math.abs(`${postion_between[0]}px` == stone.style.left) <= 1 && Math.abs(`${postion_between[1]}px` == stone.style.top) <= 1)  {
            stone.remove()
          }

        }
      }
    }
 
  }