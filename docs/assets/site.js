(() => {
  const root = document.documentElement;
  const theme = document.getElementById('theme');
  let saved;
  try { saved = localStorage.getItem('engineering-theme'); } catch (_) {}
  function apply(value) {
    root.dataset.theme = value;
    theme.textContent = value === 'dark' ? 'Light theme' : 'Dark theme';
    theme.setAttribute('aria-label', `Switch to ${value === 'dark' ? 'light' : 'dark'} theme`);
  }
  apply(saved === 'light' ? 'light' : 'dark');
  theme.addEventListener('click', () => {
    const value = root.dataset.theme === 'dark' ? 'light' : 'dark';
    apply(value);
    try { localStorage.setItem('engineering-theme', value); } catch (_) {}
  });
  const search = document.getElementById('search');
  if (!search) return;
  const exercise = document.getElementById('exercise');
  const questions = [...document.querySelectorAll('.question')];
  const expand = document.getElementById('expand');
  function filter() {
    const term = search.value.toLocaleLowerCase().trim();
    let count = 0;
    document.querySelectorAll('.chapter').forEach(chapter => {
      let shown = 0;
      chapter.querySelectorAll('.question').forEach(q => {
        q.hidden = !(exercise.value === 'all' || exercise.value === chapter.dataset.chapter) || !q.textContent.toLocaleLowerCase().includes(term);
        if (!q.hidden) { shown++; count++; }
      });
      chapter.hidden = shown === 0;
    });
    document.getElementById('results').textContent = `${count} of 66 questions`;
    document.getElementById('empty').hidden = count !== 0;
    expand.textContent = 'Expand visible answers';
  }
  search.addEventListener('input', filter);
  exercise.addEventListener('change', filter);
  expand.addEventListener('click', () => {
    const visible = questions.filter(q => !q.hidden);
    const open = visible.some(q => !q.open);
    visible.forEach(q => { q.open = open; });
    expand.textContent = open ? 'Collapse visible answers' : 'Expand visible answers';
  });
})();
