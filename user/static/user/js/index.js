const hamburger=document.querySelector('#hamburger');
const overlay=document.querySelector('.overlay');

const close_button=document.querySelector('#close');


const displayNav=()=>{
    overlay.classList.add('mobile');
    hamburger.style.display='none';
    close_button.classList.add('close-btn');
    close_button.style.display="block";
 };


const removeNav=()=>{
    overlay.classList.remove('mobile');
    close_button.classList.remove('close-btn');
    close_button.style.display="none";
    hamburger.style.display="block";

    const media=matchMedia('min-width:600px');

    media.addEventListener('change',(e)=>{
        hamburger.style.display="none";
        
    })


} 

hamburger.addEventListener('click',displayNav);
close_button.addEventListener('click',removeNav);


// close_button.addEventListener('click',()=>{
//     overlay.style.display="none";
//     close_button.style.display
// });


