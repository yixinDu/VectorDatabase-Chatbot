from openai import OpenAI
import streamlit as st
from pinecone import Pinecone

# Pinecone Init
pc = Pinecone(api_key=st.secrets["PINECONE_API_KEY"])
index = pc.Index("7375hw")

# openai Init
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Stream title
st.title("VectorDatabase Chatbot")


# Embedding
def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


# 保存Upsert
def UpsertDatabse(text):
    try:
        embedding = get_embedding(text)
        index.upsert([{"id": text, "values": embedding}])
        print("Upsert success!")
        return f"' {text} ' Upsert success!"
    except Exception as e:
        print("Upsert failed!")
        return f"Upsert failed: {str(e)}"


# 查询Query
def QueryDatabase(text):
    try:
        embedding = get_embedding(text)
        result = index.query(vector=embedding, top_k=1)
        return result
    except Exception as e:
        return f"Query failed: {str(e)}"


def generate_format(result):
    try:
        # 获取'matches'列表
        matches = result['matches']
        # 用于存储输出的列表
        output_list = []

        # 遍历'matches'列表
        for match in matches:
            # 将'id'和'score'的内容组合成一个字符串
            output = f"' {match['id']}' matches most, which score is {match['score']}"
            # 将输出字符串添加到输出列表中
            output_list.append(output)

        # 使用换行符连接所有输出字符串，并返回结果
        return '\n'.join(output_list)
    except Exception as e:
        return f"{result} ,foramt failed: {str(e)}"

# 分析openai处理后的文本
def InputProcessing(text):
    print('before: ' + text)

    # 拆分response
    seperate_responce = text.split(": ")
    print(seperate_responce)

    # 如果是Add 调用upsert；如果是Get 调用Query
    if seperate_responce[0] == 'Add':
        return UpsertDatabse(seperate_responce[1])
        # return '" ' + seperate_responce[1] + ' " add successfully'
    else:
        result = QueryDatabase(seperate_responce[1])
        # format_result = format_result_function(result)
        format_result = generate_format(result)
        return format_result
