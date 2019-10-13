import os
import subprocess
import sys
from django.shortcuts import render, redirect
# added for final
from final_display_app.fetch_data import fetch_from_db, mysql_connect


def submit_pin(request):
 #   print("in submit", fetch_from_db(1452))
    # if request.method == 'POST'
    #     pin_Number = request.POST['unique_number'] #input_box.text
    #     return render(request,'final_display.html', pin_Number)
    # else:
    return render(request, 'submit.html')

# added for final


def final_display(request, uid):
    answer = fetch_from_db(uid)
    print(uid)
    # fetch_from_db(pin_Number)
    return render(request, "final_display.html", {'final_answer': answer})


# added for final
def script():
    os.chdir("D:\\ibm_think_booth_idea_2\\final_display_app")
    print("in script")
    return subprocess.call([sys.executable, 'app.py'])


