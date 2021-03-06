# Import section
from flask import Blueprint, jsonify,abort,request,render_template
from libs.EvernoteManager import list_searches
import safeglobals
from libs.functions import handle_exception,send_response
from libs.ConfigManager import get_access_token

# Initializing the blueprint
access_token = ""
mod_search = Blueprint("mod_search",__name__)
# Initializing "tags" route
@mod_search.route("/list/<string:responseType>")
def searches(responseType):
   
    # Getting access token
    access_token = get_access_token()
    if access_token == "":
        abort(safeglobals.http_bad_request,{"message":safeglobals.ERROR_NO_TOKEN})
    
    # Getting a list of Saved Searches
    searches = list_searches(access_token,False)

    # Returing the response based on specified format
    return send_response(searches,responseType,{safeglobals.TYPE_HTML:'list.searches.html'})

   
