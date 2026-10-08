const form = document.getElementById("prediction-form");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const data = {
        sepal_length: Number(document.getElementById("sepal_length").value),
        sepal_width: Number(document.getElementById("sepal_width").value),
        petal_length: Number(document.getElementById("petal_length").value),
        petal_width: Number(document.getElementById("petal_width").value)
    };

    try {
        const response = await fetch("http://localhost:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error("Prediction request failed");
        }

        const result = await response.json();

        document.getElementById("prediction").textContent = result.prediction;
        document.getElementById("probability").textContent =
            result.probability.toFixed(4);

    } catch (error) {
        document.getElementById("prediction").textContent = "Error";
        document.getElementById("probability").textContent = "-";
        console.error(error);
    }
});