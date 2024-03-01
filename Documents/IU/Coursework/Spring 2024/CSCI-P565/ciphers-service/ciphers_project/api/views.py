from django.shortcuts import render
from django.http import JsonResponse
from .ciphers import ceasar_encode

def greetings(request):
    result = {"message": "Welcome to the ciphers service!"}
    return JsonResponse(result)

def encode(request, plaintext, shift):
    parameters = dict(request.GET)
    print(parameters)
    cipher = ceasar_encode(plaintext, shift)
    return JsonResponse({"cipher": cipher})