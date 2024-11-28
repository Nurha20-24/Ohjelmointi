'use strict'

const triggerElem = document.querySelector('#trigger')
const targetElement = document.querySelector('#target')

function changeImg() {
  targetElement.src="img/picB.jpg";
}

function revertImg()   {
  targetElement.src = "img/picA.jpg";
}

triggerElem.addEventListener('mouseover', changeImg)
triggerElem.addEventListener('mouseout', revertImg)
                                                       