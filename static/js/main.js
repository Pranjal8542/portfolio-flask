window.addEventListener("load", () => {
    const loader = document.getElementById("loader");
    loader.style.display = "none";
});
const form = document.getElementById("contactForm");

if (form) {
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        alert("Message sent! (Backend will be added later)");
        form.reset();
    });
}
/* ===============================
   SCROLL REVEAL
================================ */

const revealElements = document.querySelectorAll(".section-header, .about-card, .skills-card, .project-card, .contact-card");

const revealOnScroll = () => {
    const triggerBottom = window.innerHeight * 0.85;

    revealElements.forEach(el => {
        const boxTop = el.getBoundingClientRect().top;
        if (boxTop < triggerBottom) {
            el.classList.add("active");
        }
    });
};

window.addEventListener("scroll", revealOnScroll);
revealOnScroll();

/* ===============================
   NAVBAR ACTIVE LINK
================================ */

const navLinks = document.querySelectorAll(".nav-link");
const currentPath = window.location.pathname;

navLinks.forEach(link => {
    if (link.getAttribute("href") === currentPath) {
        link.classList.add("active");
    }
});
const lamp = document.getElementById("lamp");
const formBox = document.getElementById("contactFormBox");

if (lamp && formBox) {
    lamp.addEventListener("click", () => {
        lamp.classList.toggle("on");
        formBox.classList.toggle("show");
        formBox.classList.toggle("hidden");
    });
}
