from rest_framework import status
from rest_framework.response import Response


class ApiResponse:
    """
       Standard API response wrapper
       """

    @staticmethod
    def success(
            data=None,
            message="Success",
            status_code=status.HTTP_200_OK,
            meta=None
    ):
        payload = {
            "success": True,
            "message": message,
            "data": data
        }

        if meta is not None:
            payload["meta"] = meta

        return Response(payload, status=status_code)

    @staticmethod
    def error(
            message="Error",
            status_code=status.HTTP_400_BAD_REQUEST,
            errors=None
    ):
        payload = {
            "success": False,
            "message": message,
        }

        if errors is not None:
            payload["errors"] = errors

        return Response(payload, status=status_code)