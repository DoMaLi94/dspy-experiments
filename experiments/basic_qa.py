"""
Basic DSPy Example: Simple Question Answering

This example demonstrates a basic DSPy pipeline for question answering.
"""

import dspy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def setup_language_model() -> dspy.LM:
    """Set up the language model for DSPy with Ollama as default."""
    try:
        # Try to use Ollama first (default)
        print("Setting up Ollama as the language model...")
        lm = dspy.LM(
            "ollama_chat/gemma3:1b",
            api_base="http://localhost:11434",
            api_key="",
            structured_output=True,
        )
        dspy.configure(lm=lm)
        print("Ollama model configured successfully!")
        return lm
    except Exception as e:
        print(f"Failed to connect to Ollama: {e}")
        raise


class BasicQA(dspy.Signature):
    """Answer questions with short factual answers."""

    question = dspy.InputField()
    answer = dspy.OutputField(desc="often between 1 and 5 words")


def main() -> None:
    """Main function to demonstrate basic DSPy usage with Ollama."""

    print("Setting up DSPy Basic QA Example with Ollama...")
    print("=" * 60)

    # Setup language model
    setup_language_model()

    # Create a predictor using the signature
    generate_answer = dspy.Predict(BasicQA)

    # Example questions
    questions = [
        "What is the capital of France?",
        "Who wrote Romeo and Juliet?",
        "What is 2 + 2?",
        "What is the largest planet in our solar system?",
    ]

    print("\nGenerating answers...")
    print("=" * 50)

    for question in questions:
        try:
            # Generate prediction
            pred = generate_answer(question=question)
            print(f"Q: {question}")
            print(f"A: {pred.answer}")
            print("-" * 30)
        except Exception as e:
            print(f"Error processing question '{question}': {e}")

    print("\nBasic QA example completed!")


if __name__ == "__main__":
    main()
