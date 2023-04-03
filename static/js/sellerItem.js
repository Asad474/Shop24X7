let ham = document.querySelector(".ham");
let close = document.querySelector(".close");
let left = document.querySelector(".left");
let pContainer = document.querySelector(".product-container")
let right = document.querySelector(".right");




ham.addEventListener( "click", ()=>{
  left.style.left = 0;
})

close.addEventListener( "click", ()=>{
  left.style.left ="-100%";
})

pContainer.addEventListener("click" , ()=>{
  left.style.left ="-100%";
})