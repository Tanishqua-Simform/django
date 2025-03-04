function changePicture() {
  alert("You have changed the picture!");
}

let btn = document.getElementById("btn");
let pic = document.getElementById("pic");
btn.addEventListener("click", () => {
  curr = pic.getAttribute("src");
  if (curr === pic1) {
    pic.setAttribute("src", pic2);
    pic.setAttribute("class", "img-2");
  } else {
    pic.setAttribute("src", pic1);
    pic.setAttribute("class", "img-1");
  }
});
