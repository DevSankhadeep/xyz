import google.generativeai as genai

# Configure your API key
genai.configure(api_key="") # Replace with your actual API key

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Generate a response
response = model.generate_content("You are a virtual assistant so please give short answers")

# Print the response
print(response.text)
