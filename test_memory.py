
from memory import save_message, get_history

session = "demo-001"

save_message(session, "user", "My name is Ali.")
save_message(session, "assistant", "Nice to meet you, Ali!")

history = get_history(session)

for message in history:
    print(message)
