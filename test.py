import requests from bs4 import BeautifulSoup as BS

page = 1

while True:
    r = requests.get("https://stopgame.ru/review/p" +str(page) +"?subsection=izumitelno")

    html = BS(r.content, 'html.parser')
    items = html.select("._card_8sstg_1")
    if(len(items)):
        for el in items: 
            title = el.select('._card__content_8sstg_390 > a')
            print(title[0].text)
        page += 1            
    else:
        break        
'''
s = requests.Session()
# get CSRF
auth_html = s.get("https://smartprogress.do/")
auth_bs = BS(auth_html.content, "html.parser")
csrf = auth_bs.select("input[name=YII_CSRF_TOKEN]")[0]['value']

payload = {
    "YII_CSRF_TOKEN": csrf, 
    "returnUrl": '/', 
    "UserLoginForm[email]": "priler96@gmail.com", "UserLoginForm(password]": "tester123", "UserLoginForm[rememberMe]": 1
}
answ = s.post("https://smartprogress.do/user/login/", data = payload) 
answ_bs = BS(answ.content,"html.parser")

print("Uмя: {}\nУровень: {}\nОпыт: {}".format(
    answ_bs.select(".user-menu__name")[0].text.strip(), 
    answ_bs.select(".user-menu__info-text--lvl")[0].text.strip(),
    answ_bs.select(".user-menu__info-text--exp")[0].text.strip()
)) 
'''





