document.addEventListener("DOMContentLoaded", function () {
    const slider = document.getElementById("cost-slider");
    const minCostLabel = document.getElementById("minCostLabel");
    const maxCostLabel = document.getElementById("maxCostLabel");
    const minCostInput = document.getElementById("minCost");
    const maxCostInput = document.getElementById("maxCost");

    // Create two range inputs for the double slider
    const minSlider = document.createElement("input");
    const maxSlider = document.createElement("input");

    minSlider.type = "range";
    minSlider.min = "1000";
    minSlider.max = "100000";
    minSlider.value = "1000";
    minSlider.step = "500";
    
    maxSlider.type = "range";
    maxSlider.min = "1000";
    maxSlider.max = "100000";
    maxSlider.value = "100000";
    maxSlider.step = "500";

    // Append sliders to the slider container
    slider.appendChild(minSlider);
    slider.appendChild(maxSlider);

    // Update labels and hidden inputs
    function updateLabels() {
        minCostLabel.innerText = minSlider.value;
        maxCostLabel.innerText = maxSlider.value;

        // Ensure the min slider can't go above the max slider
        if (parseInt(minSlider.value) > parseInt(maxSlider.value)) {
            minSlider.value = maxSlider.value;
        }
        
        // Update hidden inputs
        minCostInput.value = minSlider.value;
        maxCostInput.value = maxSlider.value;
    }

    // Add event listeners
    minSlider.addEventListener("input", updateLabels);
    maxSlider.addEventListener("input", updateLabels);

    // Initial labels update
    updateLabels();
});

