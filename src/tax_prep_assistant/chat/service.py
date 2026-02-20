from __future__ import annotations

from dataclasses import dataclass

from tax_prep_assistant.clients.openrouter_client import OpenRouterClient
from tax_prep_assistant.clients.scaledown_client import ScaleDownClient


@dataclass(frozen=True)
class ChatService:
    llm: OpenRouterClient
    compressor: ScaleDownClient | None = None

    def reply(self, chat_log: list[dict[str, str]]) -> str:
        if not chat_log:
            return "Hi, ask me any tax filing question."

        latest = chat_log[-1]
        latest_text = latest.get("content", "")

        compressed_text = (
            self.compressor.compress(latest_text) if (self.compressor is not None) else latest_text
        )

        request_messages: list[dict[str, str]] = [
            {
                "role": "system",
                "content": (
                    "You are a concise tax preparation helper. "
                    "Respond in English only. "
                    "Give practical guidance and mention this is not legal or tax advice."
                ),
            },
            *chat_log[:-1],
            {"role": "user", "content": compressed_text},
        ]

        return self.llm.chat(request_messages)
