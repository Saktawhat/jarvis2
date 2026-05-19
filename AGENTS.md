# Repository Guidelines

## Project Structure & Module Organization

This is a small Python voice assistant with modules kept at the repository root.

- `main.py` transcribes audio with Whisper, routes search-like prompts, and streams Ollama responses.
- `record.py` records microphone input and writes `temp_audio.wav`.
- `search.py` detects search intents and calls `websearch`, `webfetch`, or a DuckDuckGo fallback.
- `wakeword.py` is a placeholder for wake-word logic.
- `test_vad.py` is an ad hoc CUDA availability check, not a full test suite.
- `pyproject.toml` and `uv.lock` define the Python 3.13 environment.

Avoid committing generated runtime audio such as `temp_audio.wav`.

## Build, Test, and Development Commands

Use `uv` for dependency management.

- `uv sync` installs the locked dependencies from `uv.lock`.
- `uv run python main.py` runs the assistant. Requires microphone access, Whisper model cache, and an Ollama model such as `tinyllama:latest`.
- `uv run python test_vad.py` checks whether PyTorch can see CUDA.
- `uv add <package>` adds a dependency and updates project metadata.

There is no separate build step.

## Coding Style & Naming Conventions

Follow standard Python style with 4-space indentation and snake_case names for functions, variables, and modules. Keep module-level constants uppercase, such as `ENABLE_WEB_SEARCH`.

Prefer small functions with explicit inputs and return values. Keep comments concise; English comments are preferred for shared maintenance.

## Testing Guidelines

No formal testing framework is configured yet. For new behavior, prefer `pytest` tests under a future `tests/` directory with names like `test_search.py` and functions named `test_<behavior>()`.

Mock microphone input, network calls, subprocess calls, Whisper, and Ollama. Normal tests should not require live audio devices, GPU access, or external services.

## Commit & Pull Request Guidelines

This repository has no commit history yet, so use a simple Conventional Commits style: `feat: add wake word detector`, `fix: handle missing websearch command`, or `docs: add contributor guide`.

Pull requests should include a short description, reason for the change, verification commands, and runtime notes such as required local models, microphone permissions, or GPU assumptions.

## Security & Configuration Tips

Treat microphone recordings and transcripts as sensitive. Do not commit captured audio, API keys, local model caches, or machine-specific configuration. When adding integrations, read secrets from environment variables and document the required variable names in `README.md`.
