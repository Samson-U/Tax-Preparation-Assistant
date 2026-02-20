# Tax Preparation Assistant (Streamlit)

An Advanced AI-powered Tax Filing Chatbot that simplifies tax preparation using compressed tax codes and deduction guides.

This chatbot interacts conversationally with users, understands financial inputs, applies tax rules, calculates tax liability, and provides personalized tax-saving suggestions.

## Requirements

- Python 3.11+
- Windows/macOS/Linux

## Environment

Create a `.env` file (or copy from `.env.example`) and set:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL=upstage/solar-pro-3:free
SCALEDOWN_API_KEY=your_scaledown_api_key_here
SCALEDOWN_API_URL=https://api.scaledown.ai/v1/compress
```

Notes:

- ScaleDown is optional. If `SCALEDOWN_API_KEY` is empty, compression is skipped.
- Keep `.env` private. This repo ignores it via `.gitignore`.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

If the app can’t connect, verify your environment variables in `.env` and restart Streamlit.

## Structure

- UI: `src/tax_prep_assistant/ui/streamlit_app.py`
- Chat logic: `src/tax_prep_assistant/chat/service.py`
- API clients: `src/tax_prep_assistant/clients/`
- Settings/env: `src/tax_prep_assistant/settings.py`

## Behavior

- English only: enforced via the LLM system prompt.
- Secrets: API keys are never printed in the UI.

## Notes

- This project is a demo for learning and prototyping.
- Guidance is simplified and not legal or tax advice.

## Security

If you accidentally shared a key publicly, rotate/regenerate it with the provider and update `.env`.
