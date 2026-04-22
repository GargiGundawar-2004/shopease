function showNotification(message) {
    if (!message) {
        console.error("No message provided");
        return;
    }

    alert(message); // simple UI
}