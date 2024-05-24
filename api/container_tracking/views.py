from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.decorators import permission_classes
from rest_framework import permissions
import re
import environ
from django.conf import settings
import requests


@permission_classes((permissions.AllowAny,))
class ContainerTrackingListView(viewsets.ViewSet):

    def list(self, request):
        if re.search(
            "^[A-Z]{4}[0-9]{7}$",
            request.query_params.get("container_number"),
        ):
            return Response(
                self.get_container_info_from_api(
                    request.query_params.get("container_number")
                )
            )

        return Response(
            {
                "status": "error",
                "message": "Invalid container number. Please provide a valid container number.",
                "data": None,
            },
            status=400,
        )

    def get_container_info_from_api(self, container_number):
        base_url = "https://tracking.cargotime.ru/v1/container"
        api_key = settings.TRACKING_API_SECRET
        company = "AUTO"
        url = f"{base_url}?api_key={api_key}&company={company}&container_number={container_number}"
        print(url)
        response = requests.get(url, headers={"accept": "application/json"})
        return response.json()
