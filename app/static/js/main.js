let menu = document.querySelector('#menu-bar');
let nav = document.querySelector('.nav');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    nav.classList.toggle('active');
}

let section = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header .nav a');

window.onscroll = () =>{

    menu.classList.remove('fa-times');
    nav.classList.remove('active');

    section.forEach(sec =>{

        let top = window.scrollY;
        let height = sec.offsetHeight;
        let offset = sec.offsetTop - 150;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height){
            navLinks.forEach(links =>{
                links.classList.remove('active');
                document.querySelector('header .nav a[href*='+id+']').classList.add('active');
            });
        };
    });

}

const realFileBtn = document.getElementById("real-file");
const customBtn = document.getElementById("custom-button");
const customTxt = document.getElementById("custom-text");
const imagePreview = document.getElementById("image-preview");

customBtn.addEventListener("click", function() {
  realFileBtn.click();
});

realFileBtn.addEventListener("change", function() {
  const file = this.files[0];

  if (file) {
    const reader = new FileReader();

    reader.addEventListener("load", function() {
      const image = new Image();
      image.src = this.result;
      image.classList.add("w-100"); // Adjust image width as needed
      imagePreview.innerHTML = ""; // Clear previous image if any
      imagePreview.appendChild(image);
    });

    reader.readAsDataURL(file);
    customTxt.innerHTML = file.name; // Display file name
  } else {
    customTxt.innerHTML = "No file chosen, yet.";
    imagePreview.innerHTML = ""; // Clear image preview
  }
});
