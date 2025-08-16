from django.http import HttpResponse  # Importing the HttpsResponse class to handle HTTP responses.

def home_page(request): # This function handles the home page request. The request is must in a views function.
    print("This is the home page")
    return HttpResponse("Welcome to the Home Page")  # Returns a simple HTTP response with a welcome message.
