document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.bubble').forEach(bubble => {
        bubble.style.left = `${Math.random() * 100}%`;
        bubble.style.width = `${Math.random() * 100}px`;
        bubble.style.height = bubble.style.width;
        bubble.style.animationDuration = `${Math.random() * 3 + 12}s`;
        bubble.style.animationDelay = `${Math.random() * 5}s`;
    });
});