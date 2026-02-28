/**
 * Step Wizard Design Template
 * Reusable JS for step-by-step navigation.
 * Usage: Add data-step to each step, call initStepWizard(container, options).
 */

function initStepWizard(container, options) {
  options = options || {};
  var steps = container.querySelectorAll('[data-step]');
  var total = steps.length;
  var current = parseInt(options.startAt || 0, 10);
  var progressFill = container.querySelector('.wizard-progress-fill');
  var progressText = container.querySelector('.wizard-progress-text');
  var onStepChange = options.onStepChange || function() {};

  function showStep(index) {
    index = Math.max(0, Math.min(index, total - 1));
    current = index;
    
    steps.forEach(function(step, i) {
      step.classList.toggle('active', i === index);
    });

    if (progressFill) {
      progressFill.style.width = ((index + 1) / total * 100) + '%';
    }
    if (progressText) {
      progressText.textContent = 'Schritt ' + (index + 1) + ' von ' + total;
    }

    onStepChange(index, total);
  }

  container.addEventListener('click', function(e) {
    var btn = e.target.closest('[data-wizard-next]');
    if (btn) {
      e.preventDefault();
      showStep(current + 1);
    }
    btn = e.target.closest('[data-wizard-prev]');
    if (btn) {
      e.preventDefault();
      showStep(current - 1);
    }
  });

  showStep(current);
  return { showStep: showStep, getCurrent: function() { return current; } };
}
