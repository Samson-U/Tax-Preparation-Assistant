from __future__ import annotations

from dataclasses import dataclass

import requests


@dataclass(frozen=True)
class ScaleDownClient:
    api_key: str
    api_url: str

    def compress(self, text: str) -> str:
        if not self.api_key or not text.strip():
            return text

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "text": text,
            "mode": "balanced",
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=25)
            response.raise_for_status()
            data = response.json()

            compressed = (
                data.get("compressed_text")
                or data.get("text")
                or data.get("result")
                or data.get("output")
            )
            if isinstance(compressed, str) and compressed.strip():
                return compressed.strip()

            return text
        except requests.RequestException:
            return text
