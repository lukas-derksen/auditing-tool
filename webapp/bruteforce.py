import urllib

def check_login_form(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    html = mybytes.decode("utf-8")
    fp.close()
    print(html)

    if not "<form" in html:
        return False

    html = html[html.index('<form'):html.index('</form')]

    if not any('name='+x in html for x in ['"username', '"user', '"password', '"pass']):
        return False

    return True