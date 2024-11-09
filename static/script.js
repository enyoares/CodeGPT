async function sendMessage() {
    const userInput = document.getElementById("user-input");
    const message = userInput.value.trim();
    
    if (!message) return;

    // 사용자 메시지 표시
    addMessage(message, "user-message");
    userInput.value = "";

    // 서버에 요청 보내기
    const response = await fetch("/query", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: message }),
    });

    if (response.ok) {
        const data = await response.json();
        addMessage(data.answer, "bot-message");
    } else {
        addMessage("오류가 발생했습니다. 다시 시도해 주세요.", "bot-message");
    }
}

// 메시지를 대화창에 추가
function addMessage(text, className) {
    const chatHistory = document.getElementById("chat-history");
    const messageElement = document.createElement("div");
    messageElement.classList.add("chat-message", className);
    messageElement.textContent = text;
    chatHistory.appendChild(messageElement);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}
