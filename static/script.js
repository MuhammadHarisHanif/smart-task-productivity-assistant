
const chatBox = document.getElementById("chat-box");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const loading = document.getElementById("loading");
const resetBtn = document.getElementById("reset-btn");

// Create and save a session ID in the browser
let sessionId = localStorage.getItem("smart_task_session");

if (!sessionId) {
    sessionId = crypto.randomUUID();
    localStorage.setItem("smart_task_session", sessionId);
}

// Display a message in the chat
function addMessage(text, sender) {
    const message = document.createElement("div");
    message.className = `message ${sender}`;
    message.textContent = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Load previous conversation
async function loadHistory() {
    try {
        const response = await fetch(
            `/history?session_id=${encodeURIComponent(sessionId)}`
        );

        if (!response.ok) throw new Error("Could not load history");

        const data = await response.json();

        if (data.messages && data.messages.length > 0) {
            chatBox.innerHTML = "";

            data.messages.forEach(msg => {
                const sender = msg.role === "user" ? "user" : "bot";
                addMessage(msg.content, sender);
            });
        }
    } catch (error) {
        console.error(error);
    }
}

// Send a message to Flask
chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, "user");
    userInput.value = "";

    sendBtn.disabled = true;
    loading.style.display = "block";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                session_id: sessionId,
                message: message
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Request failed");
        }

        addMessage(data.reply, "bot");

    } catch (error) {
        addMessage(error.message, "bot");
    } finally {
        sendBtn.disabled = false;
        loading.style.display = "none";
        userInput.focus();
    }
});

// Reset conversation history
resetBtn.addEventListener("click", async () => {
    try {
        const response = await fetch("/reset", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ session_id: sessionId })
        });

        if (!response.ok) throw new Error("Could not reset conversation");

        chatBox.innerHTML = "";
        addMessage("Conversation reset! How can I help?", "bot");

    } catch (error) {
        addMessage(error.message, "bot");
    }
});

// Load saved messages when page opens
loadHistory();
