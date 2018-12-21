import urllib.request
import re

nothing = {
    "previous": 0,
    "current": 12345,
    "iter": 0,
    "result": False
}

def divide_by_two(number):
    return number / 2

special_cases = {
    "Yes. Divide by two and keep going.": divide_by_two
}

while not nothing.get("result") and nothing.get("current") and (nothing.get("iter") < 400):
    nothing["iter"] = nothing["iter"] + 1
    data = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d' % (nothing.get("current"))).read().decode('utf-8')
    print(data)
    next_nothing = re.search('(?<=is )([0-9]+)', data)
    result = re.search('\w+.html', data)
    if next_nothing:
        nothing["last"] = nothing.get("current")
        nothing["current"] = int(next_nothing.group(0))
    elif result:
        nothing["result"] = data
    elif special_cases.get(data):
        func = special_cases.get(data)
        nothing["current"] = func(nothing.get('last'))
    else:
        nothing = False