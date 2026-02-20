from __future__ import annotations

import streamlit as st

from tax_prep_assistant.chat.service import ChatService
from tax_prep_assistant.clients.openrouter_client import OpenRouterClient
from tax_prep_assistant.clients.scaledown_client import ScaleDownClient
from tax_prep_assistant.settings import AppSettings


def run() -> None:
    settings = AppSettings.load()

    st.set_page_config(
        page_title="Tax Preparation Assistant",
        page_icon="🧾",
        layout="centered",
    )

    st.title("Tax Preparation Assistant")

    if "chat_log" not in st.session_state:
        st.session_state.chat_log = [
            {
                "role": "assistant",
                "content": "Hi — ask me any tax filing question.",
            }
        ]

    for message in st.session_state.chat_log:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_prompt = st.chat_input("Type your tax question...")

    if user_prompt:
        st.session_state.chat_log.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.write(user_prompt)

        llm = OpenRouterClient(api_key=settings.openrouter_api_key, model=settings.openrouter_model)
        compressor = (
            ScaleDownClient(api_key=settings.scaledown_api_key, api_url=settings.scaledown_api_url)
            if settings.scaledown_api_key
            else None
        )
        chat_engine = ChatService(llm=llm, compressor=compressor)

        assistant_reply = chat_engine.reply(st.session_state.chat_log)

        with st.chat_message("assistant"):
            st.write(assistant_reply)

        st.session_state.chat_log.append({"role": "assistant", "content": assistant_reply})

    st.caption("Demo helper only. Not legal or tax advice.")
