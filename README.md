# VectorDatabase-Chatbot

Implementation of a Chat System based on Streamlit, OpenAI, and Pinecone

#### Domain Selection:

The application aims to facilitate chat interactions, with a focus on handling textual data. Its scope includes storing and retrieving text-based information through natural language commands.

#### Vector Database Implementation:
Pinecone is chosen as the vector database for its suitability in handling textual data and efficient retrieval based on semantic similarity. The preprocessed dataset is stored in Pinecone, with data indexing supporting fast and accurate information retrieval.

#### Application Development:
The application is developed using Streamlit, featuring a user-friendly interface. Users can input natural language queries or preferences through the interface. Backend logic integrates the OpenAI Language Model (LLM) for query processing and utilizes Pinecone for data retrieval. This ensures the system returns relevant and accurate responses to user queries.

#### Evaluation and Testing:
Testing includes scenarios where the input content is empty, in which case the system outputs a default prompt. Users can input and retrieve text content based on the provided prompts.

![image-20240409192610152](/Users/yfkj/Library/Application Support/typora-user-images/image-20240409192610152.png)

#### Conclusion

Through these steps, our chat system successfully integrates Streamlit, OpenAI, and Pinecone, providing users with a seamless and efficient experience for storing and retrieving text-based information through natural language commands.

#### Outlook

In the future, we can further enhance the output format, such as improving the readability of the query results. Additionally, optimizing the UI interface to allow users to upload files and perform queries based on file content can be considered. These functionalities will be implemented and submitted in the "Last Assignment with Options".