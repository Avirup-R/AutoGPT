import openai
from youtube_transcript_api import YouTubeTranscriptApi
from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup

def video_summarizer(code):
    dic=YouTubeTranscriptApi.get_transcript(code)
    text=''
    for i in dic:
        text+=i['text']

    # print(text)
    
    openAI_token = ""
    openai.api_key = openAI_token
    question = "Summarize the given text"+text
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": question}])
    output=response.choices[0].message.content
    return (output)



def code_completion(text):
    openAI_token = ""
    openai.api_key = openAI_token
    question = text+'code in python, return just only the code'
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": question}])
    output=response.choices[0].message.content
    return (output)


def online_search(q):
    params = {
    "api_key": "",
    "engine": "google",
    "q": q,
    "location": "New Delhi, Delhi, India",
    "google_domain": "google.co.in",
    "gl": "in",
    "hl": "en"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    options=results['organic_results']
    links=[]
    count=0
    for option in options:
        links.append(option['link'])

    for link in links:

        url=link
        try:
        # Step 1: Fetch the website's HTML content
            response = requests.get(url)
            response.raise_for_status()  # Check for any request errors

            # Step 2: Parse the HTML content with Beautiful Soup
            soup = BeautifulSoup(response.text, 'html.parser')  # You can use a different parser if needed

            # Step 3: Extract the text from the parsed HTML
            # In this example, we'll extract all the text within <p> tags
            paragraphs = soup.find_all('p')

            # Concatenate the text from all paragraphs into a single string
            website_text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])
            break
        except:
            continue

    openAI_token = ""
    openai.api_key = openAI_token
    question = "Take out the informative part from the given text"+website_text
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": question}])
    output=response.choices[0].message.content
    return (output)

# print(video_summarizer("xGi7Ytq5ibM"))