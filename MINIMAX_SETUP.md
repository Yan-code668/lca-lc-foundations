# MiniMax setup for this LangChain course

This course originally used OpenAI models such as `gpt-5-nano`. The notebooks and course scripts in this local copy have been updated to create chat models through `minimax_model.get_model()`.

## 1. Configure `.env`

Set your MiniMax key in `.env`:

```env
OPENAI_API_KEY='your_real_minimax_api_key'
OPENAI_BASE_URL='https://api.minimax.io/v1'
OPENAI_API_BASE='https://api.minimax.io/v1'
MINIMAX_MODEL='MiniMax-M2.7'
```

`TAVILY_API_KEY` is separate. MiniMax replaces the chat model API, not the Tavily web-search API.

## 2. Model initialization pattern

The original course pattern was:

```python
from langchain.chat_models import init_chat_model

model = init_chat_model(model="gpt-5-nano")
```

This local copy now uses:

```python
from minimax_model import get_model

model = get_model()
```

The original agent pattern was:

```python
agent = create_agent(model="gpt-5-nano", tools=tools)
```

This local copy now uses:

```python
from minimax_model import get_model

agent = create_agent(model=get_model(), tools=tools)
```

## 3. Provider-specific notes

The Anthropic and Google cells in Module 1 Lesson 1 were only there to demonstrate provider switching. In this local copy, the live model calls have been redirected to MiniMax so you do not need Anthropic or Google keys for the main lessons.

The audio and multimodal examples may still depend on model capabilities. If MiniMax's selected model does not support audio input, skip that audio-specific cell and continue with the text and tools lessons.

## 4. Quick smoke test

After installing the course dependencies, run this in a notebook cell:

```python
from minimax_model import get_model

model = get_model()
response = model.invoke("用一句话解释 LangChain 是什么。")
print(response.content)
```

If this works, your MiniMax configuration is ready for the normal LangChain lessons.
