// frontend/js/dashboard.js
function loadDashboard() {
    fetch("/api/data")
        .then(res => res.json())
        .then(data => {
            const div = document.getElementById("dashboard");
            div.innerHTML = "<h3>Data Loaded</h3>";
        });
}