# We need:
#
#     pip install requests
# 

import requests

# mimic a form request
form_data = {"chickens": "lucy", "cat": "pookie"}

r = requests.post("http://jeremyosborne.com/class/formtest.php",
                  data=form_data)

# Display the response data.
print r.text
