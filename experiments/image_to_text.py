import os

import dspy

# Get the absolute path to the image
image_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "images", "dog01.png"
)

# Set up dspy to use Ollama with the multimodal LLaVA model
lm = dspy.LM(
    "ollama_chat/llava:7b",
    api_base="http://localhost:11434",
    api_key="",
)

# Configure DSPy to use this language model
dspy.configure(lm=lm)


# Define a signature for image description
class ImageDescription(dspy.Signature):
    """Describe what you see in the given image."""

    image = dspy.InputField()
    description = dspy.OutputField(desc="A short description of the image")


# Create a predictor for image description
describe_image = dspy.Predict(ImageDescription)

print(f"Image path: {image_path}")
print(f"Image exists: {os.path.exists(image_path)}")

# Run the image description
try:
    response = describe_image(image=image_path)
    print("Image Description:", response.description)
except Exception as e:
    print(f"Error describing image: {e}")
    print("Make sure the llava:7b model is installed")
