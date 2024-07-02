import os
import json
from openai import AzureOpenAI

# Ensure environment variables are set
assert "AZURE_OPENAI_API_KEY" in os.environ, "Environment variable AZURE_OPENAI_API_KEY is not set."
assert "AZURE_OPENAI_ENDPOINT" in os.environ, "Environment variable AZURE_OPENAI_ENDPOINT is not set."
assert "AZURE_OPENAI_EMBEDDING_MODEL_SMALL" in os.environ, "Environment variable AZURE_OPENAI_EMBEDDING_MODEL_SMALL is not set."

# Set up your Azure OpenAI credentials
api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = "2024-02-01"
embedding_model = os.getenv("AZURE_OPENAI_EMBEDDING_MODEL_SMALL")

# Pretty print the variables
variables = {
    "API Key": api_key,
    "Azure Endpoint": azure_endpoint,
    "API Version": api_version,
    "Embedding Model": embedding_model
}

print("Variables being used:")
print(json.dumps(variables, indent=2))

# Initialize the AzureOpenAI client
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=azure_endpoint
)

# Sample text to create embedding for
text = "This is a sample text for generating embeddings."

try:
    # Request an embedding
    response = client.embeddings.create(
        input=text,
        model=embedding_model
    )

    # Print the embedding response
    print("Embedding response:")
    print(response.model_dump_json(indent=2))

except Exception as e:
    print("Error:", e)
