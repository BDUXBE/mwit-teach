/* Shared quiz widget — reused across all lessons */
(function () {
  function initQuiz(quizEl) {
    const opts = quizEl.querySelectorAll('.opt');
    const feedback = quizEl.querySelector('.feedback');
    let answered = false;

    opts.forEach(btn => {
      btn.addEventListener('click', () => {
        if (answered) return;
        answered = true;
        const isCorrect = btn.dataset.correct === 'true';
        btn.classList.add(isCorrect ? 'correct' : 'wrong');
        opts.forEach(b => {
          b.disabled = true;
          if (b.dataset.correct === 'true') b.classList.add('correct');
        });
        feedback.textContent = isCorrect
          ? (quizEl.dataset.feedbackCorrect || 'Correct!')
          : (quizEl.dataset.feedbackWrong  || 'Not quite — see the highlighted answer.');
        feedback.style.color = isCorrect ? 'var(--ok)' : 'var(--warn)';
      });
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.quiz').forEach(initQuiz);
  });
})();
