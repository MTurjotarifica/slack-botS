import logging

import azure.functions as func



def main(req: func.HttpRequest) -> func.HttpResponse:
    print("it works")
    return func.HttpResponse("hello world")
