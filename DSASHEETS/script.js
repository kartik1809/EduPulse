// Particle Animation
document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector("header");
    const particleCount = 50;
    const particleSize = 4;

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement("span");
        particle.classList.add("particle");
        particle.style.width = particleSize + "px";
        particle.style.height = particleSize + "px";
        particle.style.left = Math.random() * window.innerWidth + "px";
        particle.style.top = Math.random() * header.clientHeight + "px";
        header.appendChild(particle);
    }
});
