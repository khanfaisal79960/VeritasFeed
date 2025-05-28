// static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    // Example: Add a simple animation to cards on hover if not already handled by CSS
    // This is mostly for demonstration; CSS hover effects are generally preferred for performance.

    const newsCards = document.querySelectorAll('.card');

    newsCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            // Add a class that triggers a more pronounced animation
            // For this project, CSS handles the primary hover, but this shows JS interaction
            // card.classList.add('hover-effect');
        });

        card.addEventListener('mouseleave', () => {
            // Remove the class
            // card.classList.remove('hover-effect');
        });
    });

    // You could add more interactive elements here, like:
    // - A "Back to Top" button that appears on scroll
    // - Client-side filtering or sorting of news articles (if not handled by Flask)
    // - Dynamic loading of more articles (infinite scroll)
});
