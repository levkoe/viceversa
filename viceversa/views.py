from django.shortcuts import render


def home(request):
    """View for /home

    Args:
        request (django.HttpRequest): request from user

    Returns:
        django.HttpResponse: render for home.html
    """
    return render(request, "home.html")


def reverse(request):
    user_text = request.GET["usertext"]
    word_count = len(user_text.split())
    reversed_text = user_text[::-1]
    return render(
        request,
        "reverse.html",
        {"usertext": user_text, "reversedtext": reversed_text, "wordcount": word_count},
    )
