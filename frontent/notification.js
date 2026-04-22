function showNotification(message, type = "info") {
    const div = document.createElement("div");
    div.className = "notification " + type;
    div.innerText = message;

    document.body.appendChild(div);

    setTimeout(() => div.remove(), 3000);
}