
function updateHeader() {
    const header = document.querySelector('header');

    header.textContent = 'New Header!!!';
  }
  
  const updateButton = document.getElementById('update_header');
  
  updateButton.addEventListener('click', updateHeader);
