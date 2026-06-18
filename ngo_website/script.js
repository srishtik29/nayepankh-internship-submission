// ===== Scroll Reveal Animation =====

const reveals = document.querySelectorAll(".reveal");

function revealElements() {

    reveals.forEach((element) => {

        const windowHeight = window.innerHeight;
        const elementTop = element.getBoundingClientRect().top;

        if (elementTop < windowHeight - 100) {
            element.classList.add("active");
        }

    });

}

window.addEventListener("scroll", revealElements);
revealElements();


// ===== Dark Mode =====

const darkBtn = document.getElementById("darkBtn");

if(localStorage.getItem("theme") === "dark"){
    document.body.classList.add("dark-mode");
    darkBtn.textContent = "☀️";
}

darkBtn.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");

    if(document.body.classList.contains("dark-mode")){

        darkBtn.textContent = "☀️";
        localStorage.setItem("theme","dark");

    }else{

        darkBtn.textContent = "🌙";
        localStorage.setItem("theme","light");

    }

});