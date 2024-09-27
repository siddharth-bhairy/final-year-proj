function toggleMenu() {
    const sideMenu = document.getElementById('sideMenu');
    const backgroundOverlay = document.getElementById('backgroundOverlay');
    const menuBtn = document.getElementById('menuBtn');

    sideMenu.classList.toggle('show'); // Toggle the class to slide the menu in and out
    backgroundOverlay.classList.toggle('blur'); // Toggle the blur effect on the background overlay
    menuBtn.style.display = sideMenu.classList.contains('show') ? 'none' : 'block'; // Hide hamburger button when menu is shown
}
