from __future__ import annotations

from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass(frozen=True)
class AppSettings:
    openrouter_api_key: str
    openrouter_model: str

    scaledown_api_key: str
    scaledown_api_url: str

    @staticmethod
    def load() -> "AppSettings":
        # Load local .env first; real deployments can use environment variables directly.
        load_dotenv()

        openrouter_api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
        openrouter_model = os.getenv("OPENROUTER_MODEL", "upstage/solar-pro-3:free").strip()

        scaledown_api_key = os.getenv("SCALEDOWN_API_KEY", "").strip()
        scaledown_api_url = os.getenv("SCALEDOWN_API_URL", "https://api.scaledown.ai/v1/compress").strip()

        return AppSettings(
            openrouter_api_key=openrouter_api_key,
            openrouter_model=openrouter_model,
            scaledown_api_key=scaledown_api_key,
            scaledown_api_url=scaledown_api_url,
        )
