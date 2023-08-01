document.addEventListener('DOMContentLoaded', () => {
  const btn = document.querySelector('button');

  btn.addEventListener('click', async () => {

    const trackId = btn.getAttribute('data-track-id');

    const response = await fetch('/audio/?filename=' + trackId);

    const audioBlob  = await response.body;

    const audio = new Audio();
    audio.src = audioBlob;
    audio.play();
  });
});