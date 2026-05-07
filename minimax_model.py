from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


DEFAULT_MINIMAX_BASE_URL = "https://api.minimaxi.com/v1"
DEFAULT_MINIMAX_MODEL = "MiniMax-M2.7"


def get_model(**kwargs: Any):
    """Create a LangChain chat model that talks to MiniMax through the OpenAI-compatible API."""
    load_dotenv(Path(__file__).with_name(".env"), override=True)

    api_key = os.getenv("MINIMAX_API_KEY") or os.getenv("OPENAI_API_KEY")
    base_url = (
        os.getenv("MINIMAX_BASE_URL")
        or os.getenv("OPENAI_BASE_URL")
        or os.getenv("OPENAI_API_BASE")
        or DEFAULT_MINIMAX_BASE_URL
    )
    model = os.getenv("MINIMAX_MODEL") or DEFAULT_MINIMAX_MODEL

    if not api_key or "your_" in api_key:
        raise RuntimeError(
            "Please set MINIMAX_API_KEY or OPENAI_API_KEY in .env to your MiniMax API key."
        )

    return init_chat_model(
        model=model,
        model_provider="openai",
        api_key=api_key,
        base_url=base_url,
        **kwargs,
    )
