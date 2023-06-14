
let stone_pos = []
let tree_pos = []


 


export async function randomIntFromInterval(min, max) { // min and max included 
return Math.floor(Math.random() * (max - min + 1) + min)
}

export async function generate_trees(number){
    for (let i =0; i <= number; i++) {
        let left = randomIntFromInterval(0,1980)
        let kokot_top =  randomIntFromInterval(0,1980)
      console.log(kokot_top)
      tree_pos.push([left, kokot_top])
       $('.stones').append(
      `
      <div id="tree" class="tree" style="left: ${left}px; top: ${kokot_top}px;"><img src="assets/tree.png" width="120"></div>
      `
    )
    }
  
  }
  
  
  export async function generate_stones(number){
    for (let i =0; i <= number; i++) {
        let left = randomIntFromInterval(0,1980);
        let top_y =  randomIntFromInterval(0,1980)
      stone_pos.push([left, top_y])
       $('.stones').append(
      `
      <div id="stone" class="stone" style="left: ${left}px; top: ${top_y}px;"><img src="assets/stone.png" width="50"></div>
      `
    )
    }
  }
  
 
  