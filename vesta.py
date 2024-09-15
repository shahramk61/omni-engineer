import os
from dotenv import load_dotenv
from colorama import init
from anthropic import Anthropic

# Initialize colorama for colored output
init(autoreset=True)

# Load environment variables from the .env file
load_dotenv()

# Correct model name with date suffix for Messages API
DEFAULT_MODEL = "claude-3-5-sonnet-20240620"


# Function to initialize the Anthropic client
def initialize_client():
    try:
        # Load the API key from environment variables
        api_key = os.getenv("ANTHROPIC_API_KEY")
        print(f"Using API Key: {api_key}")

        # Initialize the Anthropic client
        client = Anthropic(api_key=api_key)
        print("Anthropic client initialized successfully")
        return client
    except Exception as e:
        print(f"Error initializing Anthropic client: {e}")


# Call the function to initialize the client
client = initialize_client()

# Define system prompt
SYSTEM_PROMPT = """You are an incredible developer assistant. You have the following traits:
- You write clean, efficient code
- You explain concepts with clarity
- You think through problems step-by-step
- You're passionate about helping developers improve
"""


# Function to send a prompt to the Anthropic API using the Messages API
def send_prompt_to_anthropic(client, human_prompt):
    try:
        # Format the messages as required by Anthropic API
        messages = [
            {"role": "user", "content": human_prompt}
        ]

        # Make a request to the Anthropic API with required arguments using Messages API
        response = client.messages.create(
            model=DEFAULT_MODEL,  # Updated to the correct model name
            max_tokens=300,  # Define how many tokens you want in the response
            messages=messages,
            system=SYSTEM_PROMPT  # System prompt is passed as a top-level parameter, not in messages
        )

        # Extract and print the text from the response's content
        response_text = ''.join(block.text for block in response.content if hasattr(block, 'text'))
        print(f"Response from Anthropic: {response_text}")

    except Exception as e:
        print(f"Error sending prompt: {e}")


# Example prompt to test the API
test_prompt = "Can you summarize how I can fix a connection error?"
send_prompt_to_anthropic(client, test_prompt)
