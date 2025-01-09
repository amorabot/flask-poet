from flask import Flask, Response
# from controller.summary_controller import serve_user_profile
from controller import summary_controller
from controller import user_search_controller

def setup(app: Flask)->None:

    #Sets up all summary routes (/summary)
    summary_controller.setup(app)

    #Sets up all user-seach routes (/search)
    user_search_controller.setup(app)