import json

def lambda_handler(event, context):
    # Extract user input from the event
    user_input = event['inputTranscript']
    
    # Implement your logic to generate a response
    response = get_chatbot_response(user_input)
    
    # Create the response in the Lex format
    lex_response = {
        "sessionAttributes": event['sessionAttributes'],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": response
            }
        }
    }
    
    return lex_response

def get_chatbot_response(user_input):
    # You can use if-else statements, switch cases, or even integrate with other AWS services
    # For simplicity, let's return a static response in this example
    if user_input.lower() == 'hello':
        return 'Hi there!'
    else:
        return "I'm sorry, I didn't understand that."

# Prepare the event data
event = {
    'inputTranscript': 'Hello',
    'sessionAttributes': {}
}

# Call the lambda_handler function with the event data
response = lambda_handler(event, {})

# Extract and print the response content
response_content = response['dialogAction']['message']['content']
print(response_content)
