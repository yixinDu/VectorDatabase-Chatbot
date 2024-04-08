from ChatbotFunction import *
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Streamlit
# 初始化应用程序的会话状态并设置初始的回复和请求列表
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
         "content": "I'm your Vector Database Chatbot. To store content, use the command: 'Add:[content you want to store]'. For comparisons, use: 'Get:[content you want to compare]'"},
        {"role": "system",
         "content": "You're Vector Database Chatbot. Please analyze the user's command semantics and format their command to specific format. If the user's expression implies adding certain content, please format the command as 'Add: [added content]'; if the user's command implies searching for certain content, please format the command as 'Get: [searched content].'"}
    ]
if "messages" not in st.session_state:
    st.session_state["messages"] = []
print(st.session_state.messages)

# 如果会话状态中没有聊天内存，则创建一个新的内存实例

# 系统、用户和指令模版
# system_msg_template = SystemMessagePromptTemplate.from_template(template="利用提供的上下文信息，尽可能真实地回答问题、如果答案不在下面的文字中，请说'我不知道'")
# human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")
# prompt_msg_template = ChatPromptTemplate.from_template(
#     [system_msg_template, MessagesPlaceholder(Variable_name="history"), human_msg_template]
# )

# 创建对话链 将内存

for message in [m for m in st.session_state.messages if m["role"] != "system"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input
if prompt := st.chat_input("Please text here."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        # stream是调用openai处理后的内容
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=False
        )
        response = stream.choices[0].message.content
        print(response)

        if prompt ==None:
            response = prompt
        else:
            print('InputProcessing...')
            response = InputProcessing(response)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})