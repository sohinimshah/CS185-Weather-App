import openai
import config

api_key = config.DevelopmentConfig.OPENAI_KEY
openai.api_key = api_key

def generateChatResponse(weather_info):
    messages = []
    messages.append({"role": "system", "content": "You are a helpful assistant."})

    prompt = "I am providing data on weather in Dhaka, Bangladesh. " + weather_info + " In two sentences, please summarize the temperature (in celsius) and likelihood of percipitation. Then give recommendations on how to dress and what to do as tourists in Dhaka that day."

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    
    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        answer = 'Oops you beat the AI, try a different question, if the problem persists, come back later.'

    return answer

# def generateChatResponse(prompt):
#     messages = []
#     messages.append({"role": "system", "content": "You are a helpful assistant."})

#     question = {}
#     question['role'] = 'user'
#     question['content'] = prompt
#     messages.append(question)

#     response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    
#     try:
#         answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
#     except:
#         answer = 'Oops you beat the AI, try a different question, if the problem persists, come back later.'

#     return answer