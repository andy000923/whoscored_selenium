from selenium import webdriver #pip install selenium==3.141.0, 버전 확인
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

f = open("player_defensive_stat_info.csv", "w", encoding="UTF-8")
# 헤더 추가하기
f.write("Player,Tackle,Inter,Fouls,Clear,Drb,Blocks")

driver = webdriver.Chrome('./chromedriver') #크롬 드라이버 설치해서 상위폴더에 넣기, 버전 확인
driver.implicitly_wait(3)
# url에 접근한다.
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login
driver.get('https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/9075/Stages/20934/PlayerStatistics/England-Premier-League-2022-2023') # whoscored statics URL로 이동하기
driver.find_element_by_xpath('//*[@id="stage-top-player-stats-options"]/li[2]').click() #Defensive 버튼클릭하기

html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기

notices = soup.select('#player-table-statistics-body > tr')

for n in notices:
    player = n.select_one("td.col12-lg-2.col12-m-3.col12-s-4.col12-xs-5.grid-abs.overflow-text > a.player-link > span").text.strip()
    tackle = n.select_one("td:nth-child(5)").text.strip()
    inter = n.select_one("td:nth-child(6)").text.strip()
    fouls = n.select_one("td:nth-child(7)").text.strip()
    clear = n.select_one("td:nth-child(9)").text.strip()
    drb = n.select_one("td:nth-child(10)").text.strip()
    blocks = n.select_one("td:nth-child(11)").text.strip()

    print(player,tackle,inter,fouls,clear,drb,blocks)

    f.write("\n" + player + "," + tackle + "," + inter + "," + fouls + "," + clear + "," + drb + "," + blocks)

# 작업이 끝난 파일을 닫습니다.
# 반복문 밖에서 닫아줍니다.
f.close()
