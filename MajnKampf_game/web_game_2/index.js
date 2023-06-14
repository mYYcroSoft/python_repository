const player_default_speed = [
    /*[walk_speed, run_speed]*/
    10, 20
]


let player_pos = [
    /*x , y*/    
    0,0]
let player_inventory = [
    /*['item_name', 'item_count', 'item_type']*/
]


let generated_prop_list = [
/*{name: 'stone', image: 'object.png', prop_id: 1, x: stone_x, y: stone_y, object: obj_id}*/

]


/* ON PAGE LOAD EVENTS */
window.addEventListener("load", (event) => {
    generate_stones()
  });


 /* Player movement */ 
 document.addEventListener('keydown', function(event) {
if(event.key == 'd'){
    player_pos[0] += 10
    update_player_pos()
}
if(event.key == 'a'){
    player_pos[0] -= 10
    update_player_pos()
}
if(event.key == 'w'){
    player_pos[1] -= 10
    update_player_pos()
}
if(event.key == 's'){
    player_pos[1] += 10
    update_player_pos()
}

if(event.key == 'e'){
    checkPlayerBetweenRadius()
}
 })

function update_player_pos(){
    p(player_pos)
    document.getElementById("player").style.left = `${player_pos[0]}px`
    document.getElementById("player").style.top = `${player_pos[1]}px`
}


/* Counting radius between props and player postition */ 
let props_radius = []

function getRadiusBetweenEveryProps(){
    props_radius = []
    
    generated_prop_list.forEach(object =>{
       /* console.log(object)*/
        let id = object.object
        let rad_x = object.x - player_pos[0]
        let rad_y = object.y - player_pos[1]
       /* p(`radius_x: ${rad_x}    rad_y: ${rad_y}`)*/
        let radius = {x: rad_x, y: rad_y, id: id}
        props_radius.push(radius)
    })
}

function checkPlayerBetweenRadius(){
getRadiusBetweenEveryProps()
props_radius.forEach(radius =>{
if(radius.x < 50 && radius.y < 50){
    p("NEAR")
    const thisObject = generated_prop_list.find(({object }) => object === radius.id)
    for(const objectClass of document.getElementsByClassName("prop")){
        console.log(thisObject.x +`px`)
        console.log(objectClass.style.left)
        if(thisObject.x +`px` === objectClass.style.left && thisObject.y + `px` === objectClass.style.top){
            objectClass.remove()
        }
    }

   
}
})
}
/*--------------------------------------------------------------*/ 
/*  Prop generator */
const stone_count = 15
function generate_stones(){
    for(let i=0; i<=stone_count; i++){
        let stone_x = randomIntFromInterval(0,1980)
        let stone_y = randomIntFromInterval(0,800)
        let obj_id = randomIntFromInterval(1000,9999)
        let prop_data = {name: 'stone', image: 'stone.png', prop_id: 1, x: stone_x, y: stone_y, object: obj_id}
        generated_prop_list.push(prop_data)
        draw_props_html(stone_x, stone_y, 'stone')
      
    }
}
function draw_props_html(x,y,type){
    generated_prop_list.forEach(object=>{
        $('.map_props').append(` 
            <div class="prop" name="${object.name}" style="top: ${object.y}px; left: ${object.x}px">
            <div class="props_pos">x: ${object.x}px   y: ${object.y}px</div>
            <img src="assets/${object.image}" width="50"></div>
        `)
    });
}
  
function randomIntFromInterval(min, max) { // min and max included 
    return Math.floor(Math.random() * (max - min + 1) + min)
    }
   

function p(t){
    console.log(`💻 [Console]     ${t}`)
}