from __future__ import annotations

from dataclasses import dataclass

import requests


@dataclass(frozen=True)
class OpenRouterClient:
    api_key: str
    model: str
    base_url: str = "https://openrouter.ai/api/v1"
    app_title: str = "Tax Preparation Assistant"
    referer: str = "http://localhost:8501"

    def chat(self, messages: list[dict[str, str]], temperature: float = 0.5) -> str:
        if not self.api_key:
            return "I can’t connect yet. The server is missing required configuration."

        endpoint = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": self.referer,
            "X-Title": self.app_title,
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload, timeout=45)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        except requests.RequestException as exc:
            return f"OpenRouter request failed: {exc}"
        except (KeyError, IndexError, TypeError):
            return "OpenRouter returned an unexpected response format."
