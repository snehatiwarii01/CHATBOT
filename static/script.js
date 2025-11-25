function addMessage(text, sender) {
    let box = document.getElementById("chatbox");
    let msg = document.createElement("div");
    
    // Add base classes for styling + the sender class (user/bot)
    // We add 'p-2', 'rounded', 'border' (for bot) manually here to match HTML structure
    msg.className = "msg p-2 rounded " + sender;
    
    if (sender === 'bot') {
        msg.classList.add('border'); // Add border to bot messages for visibility
    }
    
    msg.innerText = text;
    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;
}

function handleEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

async function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value.trim();

    if (!message) return; 

    addMessage(message, "user");
    input.value = "";
    input.disabled = true;

    try {
        let response = await fetch("/chat", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({message: message})
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        let data = await response.json();
        addMessage(data.reply, "bot");

    } catch (error) {
        console.error("Error:", error);
        addMessage("Error: Could not connect to the bot.", "bot");
    } finally {
        input.disabled = false;
        input.focus();
    }
}