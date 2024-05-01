document.addEventListener('DOMContentLoaded', function() {
  const backToTopButton = document.querySelector('.footer__back-to-top');

  backToTopButton.addEventListener('click', function(e) {
    e.preventDefault();
    window.scrollTo({top: 0, behavior: 'smooth'});
  });

  console.log("Back to Top button is now active."); // Log message for debugging
});