from django.shortcuts import render
from .forms import ChatForm
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")
def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def chat(request):
    response = None
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['user_input']

            try:
                result = model.generate_content(user_message) 
                response = result.text
            except Exception as e:
                response = f"Error: {str(e)}"

    else:
        form = ChatForm()

    return render(request, 'chat.html', {'form': form, 'response': response})
