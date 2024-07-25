function addItem() {
    const list = document.querySelector('.my_list');
  
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
  
    list.appendChild(newItem);
  }
  
  const addItemButton = document.getElementById('add_item');

  addItemButton.addEventListener('click', addItem);
  