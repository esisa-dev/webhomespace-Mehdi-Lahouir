function createSpan(wichDiv, input){
    const languesDiv = document.querySelector(wichDiv);
    const newSpan = document.createElement('span');

    let txt = document.getElementById(input);
    if(txt.value != '')
        newSpan.textContent = '\u2022 ' + txt.value ;
    newSpan.style.display = 'block';

    languesDiv.appendChild(newSpan);

    txt.value = '';
}