## Problem: Excessive Token Consumption Before Prompt

Developers building with large language models (LLMs), particularly those focused on code generation like Claude Code, are experiencing significant frustration due to LLMs consuming a large number of tokens (e.g., 33k) *before* even processing the user's actual prompt. This "pre-prompt" token usage leads to:

*   **Increased Costs:** Developers pay for tokens whether they are part of the core prompt or pre-prompt system instructions. Excessive pre-prompt usage inflates API costs.
*   **Slower Response Times:** More tokens to process means longer inference times, degrading the user experience and application responsiveness.
*   **Reduced Efficiency and Economic Viability:** The combined effect of higher costs and slower responses makes agentic AI applications less efficient and potentially economically unviable for certain use cases.

This project addresses this by providing a simple, client-side token estimation tool. It allows developers to pre-emptively check the token count of their system prompts and user prompts *before* sending them to an LLM API, enabling them to optimize and reduce unnecessary token consumption.

## Why this project shape/stack was chosen

A Python CLI was chosen because:
*   **Accessibility:** Python is widely used in the AI/ML community, making the tool easily accessible.
*   **Simplicity:** Tokenization libraries are readily available and easy to integrate in Python.
*   **Direct Developer Utility:** A CLI allows developers to quickly check token counts from their terminal or integrate it into their build/pre-commit hooks.
*   **No LLM Call Required:** The core problem is token estimation *before* the LLM call, so a standalone tool is sufficient and doesn't require an LLM API key.

## Setup and Usage Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Run the token estimator:**

    *   **Estimate a single string:**
        ```bash
        python token_estimator.py "This is my system prompt or user query."
        ```

    *   **Estimate from a file (e.g., a system prompt file):**
        ```bash
        echo "You are a helpful AI assistant." > system_prompt.txt
        python token_estimator.py --file system_prompt.txt
        ```

    *   **Estimate multiple strings/files (sums them up):**
        ```bash
        echo "You are a helpful AI assistant." > system_prompt.txt
        echo "Write a Python script for a simple web server." > user_query.txt
        python token_estimator.py --file system_prompt.txt "Hello world!" --file user_query.txt
        ```

    *   **Get help:**
        ```bash
        python token_estimator.py --help
        ```

## GEMINI_API_KEY Requirement

`GEMINI_API_KEY` is **not** required to run this tool. It operates entirely client-side using a common tokenization library.
