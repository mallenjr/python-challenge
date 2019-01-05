import re, zipfile

nothing = {
    "previous": 0,
    "current": 90052,
    "iter": 0,
    "comments": [],
    "result": False
}

def divide_by_two(number):
    return number / 2

special_cases = {
    "Yes. Divide by two and keep going.": divide_by_two
}

channel = zipfile.ZipFile('channel.zip', 'r')

while not nothing.get("result") and nothing.get("current"):
    nothing["iter"] = nothing["iter"] + 1

    data = channel.read('%d.txt' % (nothing.get('current'))).decode('utf-8')
    nothing["comments"].append(channel.getinfo('%d.txt' % (nothing.get('current'))).comment.decode('utf-8'))

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
        nothing["result"] = True

print('\n',''.join(nothing["comments"]))