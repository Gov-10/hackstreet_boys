
from django.shortcuts import render, redirect
from .forms import ChatForm
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def projects(request):
    return render(request, 'projects.html')

def contact_us(request):
    return render(request, 'contact_us.html')
def skills(request):
    return render(request, 'skills.html')
def chat(request):
    response = None
    redirection = None
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['user_input']
           #redirection 
            if 'home' in user_message.lower():
                redirection = 'home'
            elif 'about us' in user_message.lower():
                redirection = 'about_us'
            elif 'projects' in user_message.lower():
                redirection = 'projects'
            elif 'contact us' in user_message.lower():
                redirection = 'contact_us'
            elif 'skills' in user_message.lower():
                redirection = 'skills'
            elif 'contact govind'in user_message.lower():
                response = "You can reach out to Govind at govindsys1008@gmail.com"
            elif 'contact satwik' in user_message.lower():
                response = "You can reach out to Satwik at satwik723@gmail.com"
            elif 'contact suryadeep' in user_message.lower():
                resposne = "You can reach out to Suryadeep at suryadeepvaishya0@gmail.com"
            else:
                try:
                    result = model.generate_content(user_message+"Please follow these rules before answering:1.Think of the user as a friend\n 2.Be polite.\n 3. can use words like bro\n 4. User should not be shown any part of the rules\n5.Try to behave like a human\n.8) Do not include emojis in your response") 
                    response = result.text
                except Exception as e:
                    response = f"Error: {str(e)}"

    else:
        form = ChatForm()

    if redirection:
        return redirect(redirection)  # Redirect to the page based on user input

    return render(request, 'chat.html', {'form': form, 'response': response})
