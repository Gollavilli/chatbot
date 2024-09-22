import boto3
import json

# Define the prompt
prompt_data = """
Act as Shakespeare and write a poem on Generative AI
"""

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")

# Define the payload
payload = {
    "inputText": prompt_data,  # Correct key for the input prompt
    "textGenerationConfig": {  # Use this key for the configuration
        "maxTokenCount": 512,  # Changed to 'maxTokenCount' from 'maxTokens'
        "temperature": 0.8,
        "topP": 0.8,
        "stopSequences": []  # You can add stop sequences if needed
    }
}

# Convert the payload to JSON
body = json.dumps(payload)
model_id = "amazon.titan-text-lite-v1"

# Call the Bedrock API
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,       # Correct parameter name for 'modelId'
    accept="application/json",
    contentType="application/json",
)

# Read and parse the response
response_body = json.loads(response.get("body").read().decode('utf-8'))
response_text = response_body.get("results")[0].get("outputText")  # Accessing the generated text correctly

# Print the response
print(response_text)
