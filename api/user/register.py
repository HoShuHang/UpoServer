from rest_framework.decorators import api_view
from core.account.user_manager import UserManager
from core.utility.error_exceptions import Error
from core.utility.json_response import JSONResponse
from core.utility.request_checker import RequestChecker


@api_view(['POST'])
def register(request):
    try:
        request = RequestChecker(request)

        # header

        # POST data
        data = {
            "fb_token": request.get_data("fb_token"),
        }

        # action
        user = UserManager.register(data["fb_token"])

        return JSONResponse.output({"access_token": user.token})

    except Error as error:
        return JSONResponse.output(error)
