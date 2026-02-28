# Step Wizard Design Template

Reusable template for step-by-step interactive processes. One step at a time, responsive, Lucide icons.

## Usage

1. Include CSS: `step-wizard.css`
2. Include Lucide: `<script src="https://unpkg.com/lucide@latest"></script>`
3. Include JS: `step-wizard.js`
4. Structure your HTML:

```html
<div class="wizard-app" id="wizard">
  <div class="wizard-container">
    <div class="wizard-progress">
      <div class="wizard-progress-bar">
        <div class="wizard-progress-fill"></div>
      </div>
      <span class="wizard-progress-text">Schritt 1 von 7</span>
    </div>

    <div class="wizard-step active" data-step="0">
      <!-- Step content -->
      <div class="wizard-nav">
        <button type="button" class="wizard-btn wizard-btn-primary" data-wizard-next>
          <i data-lucide="chevron-right"></i> Weiter
        </button>
      </div>
    </div>

    <div class="wizard-step" data-step="1">
      <!-- Step content -->
      <div class="wizard-nav">
        <button type="button" class="wizard-btn wizard-btn-secondary" data-wizard-prev>
          <i data-lucide="chevron-left"></i> Zurück
        </button>
        <button type="button" class="wizard-btn wizard-btn-primary" data-wizard-next>
          <i data-lucide="chevron-right"></i> Weiter
        </button>
      </div>
    </div>
  </div>
</div>

<script>
  lucide.createIcons();
  initStepWizard(document.getElementById('wizard'), { startAt: 0 });
</script>
```

## CSS Variables

- `--wizard-bg`: Background (#f8f8f8)
- `--wizard-accent`: Buttons, progress (#333)
- `--wizard-dark-block`: Dark content blocks (#4a4a4a)

## No arrows in buttons

Use text-only ("Weiter", "Zurück") or non-arrow Lucide icons (e.g. check, rotate-ccw). Do not use arrow or chevron icons in primary buttons.
