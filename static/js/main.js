// Main JS for Glory to God Vehicles
// Placeholder for interactivity

document.addEventListener('DOMContentLoaded', function() {
    // Example: highlight active nav
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        if (link.href === window.location.href) {
            link.classList.add('active');
        }
    });
});
