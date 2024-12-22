async function getPrediction() {
  const imageInput = document.getElementById("imageInput").files[0];
  if (!imageInput) {
    alert("Please upload an image!");
    return;
  }

  const formData = new FormData();
  formData.append("image", imageInput);

  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    const resultText = document.getElementById("resultText");

    // Display prediction result
    resultText.textContent = `Class: ${result.class}, Confidence: ${(result.confidence * 100).toFixed(2)}%`;
  } catch (error) {
    alert("Error: " + error.message);
    console.error("Detailed error:", error); // Log the error in the console
  }
}