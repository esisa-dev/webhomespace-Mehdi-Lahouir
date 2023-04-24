function createSpan(wichDiv, input){
    const languesDiv = document.querySelector(wichDiv);
    const newSpan = document.createElement('span');

    let txt = document.getElementById(input);
    if(txt.value != '')
        newSpan.textContent = '\u2022 ' + txt.value ;
    newSpan.style.display = 'block';

    languesDiv.appendChild(newSpan);

    txt.value = '';
}function getFiles() {
    fetch('/files')
      .then(response => response.json())
      .then(data => {
        let fileList = document.getElementById('file-list');
        for (let file of data) {
          let row = fileList.insertRow(-1);
          let nameCell = row.insertCell(0);
          nameCell.innerHTML = `<a href="/${file.name}">${file.name}</a>`; // make the name a link
          let typeCell = row.insertCell(1);
          typeCell.innerHTML = file.type;
          let sizeCell = row.insertCell(2);
          sizeCell.innerHTML = `<button onclick="showSize(${file.size})">Size</button>`; // add a button to show the size
          let modifiedCell = row.insertCell(3);
          modifiedCell.innerHTML = file.modified;
        }
      });
  }
  
  function showSize(size) {
    let centerDiv = document.createElement('div');
    centerDiv.innerHTML = `Size: ${size}`;
    centerDiv.style.textAlign = 'center';
    document.body.appendChild(centerDiv);
  }
  