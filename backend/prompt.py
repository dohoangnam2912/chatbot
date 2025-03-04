contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

qa_system_prompt = (
    "You are an assistant for question-answering tasks." 
    "Use the following pieces of retrieved context to answer the question." 
    "If there's no related context, just answer with your base knowledge." 
    "Use three sentences maximum and keep the answer concise."
)

print(contextualize_q_system_prompt)
print(qa_system_prompt)