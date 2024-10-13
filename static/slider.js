const fromSlider = document.getElementById('fromSlider');
const toSlider = document.getElementById('toSlider');
const fromInput = document.getElementById('fromInput');
const toInput = document.getElementById('toInput');
const minCost = document.getElementById('minCost');
const maxCost = document.getElementById('maxCost');

// Function to update input values when sliders are adjusted
function updateInputValues() {
    fromInput.value = fromSlider.value;
    toInput.value = toSlider.value;
    updateHiddenFields();
}

// Function to update slider values when inputs are adjusted
function updateSliderValues() {
    fromSlider.value = fromInput.value;
    toSlider.value = toInput.value;
    updateHiddenFields();
}

// Function to sync the hidden fields with the slider values
function updateHiddenFields() {
    minCost.value = fromSlider.value;
    maxCost.value = toSlider.value;
}

// Initialize the hidden fields on page load
document.addEventListener('DOMContentLoaded', () => {
    updateHiddenFields();
});
