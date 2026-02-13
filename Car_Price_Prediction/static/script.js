document.addEventListener("DOMContentLoaded", () => {
  // Event listener for brand dropdown change
  const brandDropdown = document.getElementById("brand");
  if (brandDropdown) {
    brandDropdown.addEventListener("change", loadModel);
  }

  // Add form submission handler
  const form = document.getElementById("car-form");
  if (form) {
    form.addEventListener("submit", submitForm);
  }
});

// Function to load car models dynamically based on the selected brand
function loadModel() {
  const brand = document.getElementById("brand").value; // Get selected brand
  const modelDropdown = document.getElementById("model"); // Get model dropdown

  // Clear current options in model dropdown and show loading message
  modelDropdown.innerHTML = "<option>Loading...</option>";

  // Fetch models for the selected brand from Flask backend
  fetch(`/get_models?brand=${encodeURIComponent(brand)}`)
    .then(response => {
      if (!response.ok) {
        throw new Error("Failed to fetch models");
      }
      return response.json();
    })
    .then(data => {
      // Clear current options
      modelDropdown.innerHTML = "";

      // Populate models if available
      if (data.models && data.models.length > 0) {
        data.models.forEach(m => {
          const option = document.createElement("option");
          option.value = m;
          option.textContent = m;
          modelDropdown.appendChild(option);
        });
      } else {
        // Display message if no models are available
        modelDropdown.innerHTML = "<option>No models available</option>";
      }
    })
    .catch(error => {
      console.error("Error fetching models:", error);
      modelDropdown.innerHTML = "<option>Error loading models</option>";
    });
}

// Function to validate numeric inputs before form submission
function validateNumericInput(event, fieldName) {
  const value = event.target.value;
  const errorField = document.getElementById(`${fieldName}-error`);

  // Check if value is a number
  if (isNaN(value) || value === "") {
    errorField.textContent = "Please enter a valid number.";
    errorField.style.display = "block";
  } else {
    errorField.textContent = "";
    errorField.style.display = "none";
  }
}

// Function to handle form submission
function submitForm(event) {
  event.preventDefault(); // Prevent default form submission

  // Get form data
  const formData = new FormData(event.target);

  // Create an object from the form data
  const data = {};
  formData.forEach((value, key) => {
    data[key] = value;
  });

  // Post data to Flask backend for prediction
  fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams(data),
  })
    .then(response => {
      if (!response.ok) {
        throw new Error("Failed to fetch prediction");
      }
      return response.text();
    })
    .then(result => {
      // Display the prediction result
      document.getElementById("prediction-result").textContent = `Predicted Price: ${result}`;
    })
    .catch(error => {
      console.error("Error during prediction:", error);
      document.getElementById("prediction-result").textContent = "An error occurred. Please try again.";
    });
}

 
  document.getElementById("car-form").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(this);

    fetch("/predict", {
        method: "POST",
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            const errorMessage = document.getElementById("error-message");
            const predictionResult = document.getElementById("prediction-result");

            if (data.success) {
                // Show the prediction result
                errorMessage.style.display = "none";
                predictionResult.style.display = "block";
                predictionResult.innerText = `Predicted Price: ₹${data.price}`;
            } else {
                // Show the error message
                predictionResult.style.display = "none";
                errorMessage.style.display = "block";
                errorMessage.innerText = data.error;
            }
        })
        .catch(err => {
            const errorMessage = document.getElementById("error-message");
            errorMessage.style.display = "block";
            errorMessage.innerText = "An unexpected error occurred. Please try again.";
        });
});

  
