import urllib.request

def pull(n):
    #replacements = ['<p class="monospace center">', "<br />\\n'","<br /></div>\\n'","<br /></p>\\n'","b'<p>","</p>\\n'","<br />\n'","b'","<br />","</p>"]
    link = (f"https://projecteuler.net/minimal={n}")
    raw = []

    with urllib.request.urlopen(link) as url:
        data = url.readlines()

    for num in data:
        temp = str(num).replace('<p class="monospace center">', "").replace("<br />\\n'", "").replace("<br /></div>\\n'", "").replace("<br /></p>\\n'", "").replace("b'<p>","").replace("</p>\\n'", "").replace("<br />\n'", "").replace("b'", "").replace("<br />", "").replace("</p>", "").replace(" ", "").replace('<br>', '').replace("\\n'", '')
        try:   
            raw.append(int(temp))
        except:
            pass
    return raw