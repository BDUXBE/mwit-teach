document.querySelectorAll('.quiz').forEach(quiz => {
  const opts = quiz.querySelectorAll('.opt');
  const feedback = quiz.querySelector('.feedback');

  opts.forEach(btn => {
    btn.addEventListener('click', () => {
      if (quiz.dataset.answered) return;
      quiz.dataset.answered = '1';

      const correct = btn.dataset.correct === 'true';
      btn.classList.add(correct ? 'correct' : 'wrong');

      if (!correct) {
        opts.forEach(b => {
          if (b.dataset.correct === 'true') b.classList.add('correct');
        });
      }

      opts.forEach(b => b.disabled = true);

      if (feedback) {
        const th = document.documentElement.lang === 'th';
        if (correct) {
          feedback.textContent = (th && quiz.dataset.feedbackCorrectTh)
            ? quiz.dataset.feedbackCorrectTh
            : (quiz.dataset.feedbackCorrect || '✓ Correct!');
        } else {
          feedback.textContent = (th && quiz.dataset.feedbackWrongTh)
            ? quiz.dataset.feedbackWrongTh
            : (quiz.dataset.feedbackWrong || '✗ Not quite — review the concept above and try again.');
        }
      }
    });
  });
});
