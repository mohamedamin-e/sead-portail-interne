from rest_framework.views import exception_handler
from rest_framework import status

def sead_exception_handler(exc, context):
    # Appelle le gestionnaire d'exception par défaut de DRF pour obtenir la réponse
    response = exception_handler(exc, context)

    if response is not None:
        custom_error_data = {
            "code": "SERVER_ERROR",
            "message": str(exc),
            "details": response.data
        }

        # On adapte le code d'erreur selon le status HTTP
        if response.status_code == status.HTTP_404_NOT_FOUND:
            custom_error_data["code"] = "NOT_FOUND"
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
            custom_error_data["code"] = "UNAUTHORIZED"
        elif response.status_code == status.HTTP_403_FORBIDDEN:
            custom_error_data["code"] = "FORBIDDEN"
        elif response.status_code == status.HTTP_400_BAD_REQUEST:
            custom_error_data["code"] = "VALIDATION_ERROR"

        response.data = custom_error_data

    return response