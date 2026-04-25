// frontend/js/dashboard.js
function loadDashboard() {
    fetch("/api/data")
        .then(res => res.json())
        .then(data => {
            document.getElementById("dashboard").innerText = JSON.stringify(data);
        });
}