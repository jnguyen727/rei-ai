import openai
import os

# Set your API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Step 1: Upload the JSONL file for fine-tuning
file_path = "D:/Code/Chatbot/lain_dialogue.jsonl"  # Update with the actual file path

try:
    # Upload the file for fine-tuning
    upload_response = openai.File.create(
        file=open(file_path, "rb"),  # Ensure binary mode
        purpose='fine-tune'
    )
    print(f"Uploaded file ID: {upload_response['id']}")
    
except Exception as e:
    print(f"Error uploading file: {e}")
    exit(1)  # Exit the script if the file upload fails

# Step 2: Start the fine-tuning process using the uploaded file (for GPT-4)
try:
    fine_tune_response = openai.FineTuningJob.create(  # This is the updated API call
        training_file=upload_response['id'],
        model="gpt-4",  # Fine-tuning on GPT-4
        n_epochs=4  # Adjust the number of training epochs as needed
    )
    print(f"Fine-tuning job started: {fine_tune_response['id']}")
    
except Exception as e:
    print(f"Error starting fine-tuning: {e}")
    exit(1)

# Step 3: Monitor the fine-tuning process
print("Monitoring fine-tune process...")

try:
    # Monitor fine-tuning status
    status = openai.FineTuningJob.list()
    print(status)
    
except Exception as e:
    print(f"Error monitoring fine-tune status: {e}")
