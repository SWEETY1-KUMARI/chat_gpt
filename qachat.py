from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

if submit_button and input_text:
    response = get_gemini_response(input_text)
    
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The Chat History is")
for role, text in st.session_state.get('chat_history', []):
    st.write(f"{role}: {text}")






# import React, { useState } from 'react';
# import { GenerativeModel } from 'google.generativeai'; // Assuming GenerativeModel is provided by the google.generativeai package
# import { setConfig, header, textInput, button, subheader, write } from 'streamlit'; // Assuming these Streamlit functions are provided by a custom package or library

# // Configure the API key
# const apiKey = process.env.REACT_APP_GOOGLE_API_KEY;
# GenerativeModel.configure({ api_key: apiKey });

# // Function to load Gemini Pro model and get responses
# const model = new GenerativeModel("gemini-pro"); 
# const chat = model.startChat({ history: [] });

# function getGeminiResponse(question) {
#     const response = chat.sendMessage(question, { stream: true });
#     return response;
# }

# // Component
# function GeminiApp() {
#     const [inputText, setInputText] = useState('');
#     const [chatHistory, setChatHistory] = useState([]);

#     // Function to handle question submission
#     const handleSubmit = () => {
#         if (inputText) {
#             const response = getGeminiResponse(inputText);
#             setChatHistory(prevHistory => [
#                 ...prevHistory,
#                 ["You", inputText],
#                 ...response.map(chunk => ["Bot", chunk.text])
#             ]);
#             setInputText('');
#         }
#     };

#     return (
#         <div>
#             {header("Gemini LLM Application")}
#             {textInput("Input: ", { value: inputText, onChange: e => setInputText(e.target.value), key: "input" })}
#             {button("Ask the question", { onClick: handleSubmit })}
#             {chatHistory.length > 0 && subheader("The Response is")}
#             {chatHistory.map(([role, text], index) => (
#                 <div key={index}>
#                     {role === "You" ? <b>{role}: </b> : <i>{role}: </i>}
#                     {write(text)}
#                 </div>
#             ))}
#         </div>
#     );
# }

# // Set Streamlit page config
# setConfig({ page_title: "Q&A Demo" });

# // Render the GeminiApp component
# export default GeminiApp;
