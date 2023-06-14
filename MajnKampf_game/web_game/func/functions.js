export async function remove_items(){
    const items_all = document.getElementsByClassName("inv_item");
  
    while (items_all.length > 0) {
      items_all[0].remove();
    }
  }