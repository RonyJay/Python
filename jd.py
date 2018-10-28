import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

def get_first(n):
    baseurl='https://search.jd.com/search?keyword=%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&psort=3&ev=exbrand_%E5%B0%8F%E7%B1%B3%EF%BC%88MI%EF%BC%89%5E&page='+str(2*n-1)+'&s=1&click=0'
    response = requests.get(baseurl)
    response.encoding = "utf-8"
    page_html=response.content
    soup=BeautifulSoup(page_html,'html.parser',from_encoding='utf-8')
    goodList=soup.find('div',id='J_goodsList').find('ul',class_='gl-warp clearfix')
    items=goodList.find_all('li',class_='gl-item')
    with open('JD_Phone.csv', 'a', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        for data in items:
            p_name = data.find('div',class_='gl-i-wrap').find('div',class_='p-name p-name-type-2').em.text
            p_price = data.find('div',class_='gl-i-wrap').find('div',class_='p-price').i.text
            p_commit=data.find('div',class_='gl-i-wrap').find('div',class_='p-commit').strong.a.text
            p_shop = data.find('div', class_='gl-i-wrap').find('span', class_='J_im_icon').a.text
            write.writerow([p_name, p_price,p_commit,p_shop])
    f.close()

def get_last(n):
    a = time.time()
    b = '%.5f' % a
    baseurl2='https://search.jd.com/s_new.php?keyword=%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&psort=3&ev=exbrand_%E5%B0%8F%E7%B1%B3%EF%BC%88MI%EF%BC%89%5E&page='+str(2*n)+'&s'+ str(48 * n - 20)+'&scrolling=y&log_id'+str(b)


    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA',
            'scheme': 'https',
            'referer': 'https://search.jd.com/search?keyword=%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&psort=3&ev=exbrand_%E5%B0%8F%E7%B1%B3%EF%BC%88MI%EF%BC%89%5E&page=1&s=1&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'pinId=5028vX7Bm_61ffsfn98I-w; qrsc=3; shshshfpa=a0bed453-30e6-a683-3e4a-fb0bd59723d3-1531145836; shshshfpb=17ab315e8f985410697d15e5605825b54c506fd49641b0a4b5b13e0782; pin=Ronalnie; unick=Ronalnie; _tp=VH2ZopEFzfW7a2OnnIEjeA%3D%3D; _pst=Ronalnie; TrackID=1u3U1dyzjdNwL4QGu7TODWfrQ2-Y0pZe6GdlDwoVBHaEWfTGSparzowDj4EYoAIpVh6AZQfiYmtW3sCNJK8m84pJuxrh-4OCKsICbGEIWyEc; xtest=9789.cf6b6759; ipLocation=%u56db%u5ddd; ipLoc-djd=22-1930-49324-52513.2147483645; cn=5; __jdu=183112675; __jdc=122270672; __jdv=122270672|direct|-|none|-|1540731442859; rkv=V0300; shshshfp=494fb6182a728d1c440853773d1afddd; __jda=122270672.183112675.1528029302.1540731443.1540734671.13; PCSYCityID=1930; 3AB9D23F7A4B3C9B=OA2KA6ZFETR35H32ZBO2MIJZCRIAFWFFFLBYEGARJRRDJSGDPYOHLAELAS7CVOTMC7F3QXYJOMILCXG6CEC2BVREUM; __jdb=122270672.12.183112675|13.1540734671; shshshsID=7b622763ed69a9eadcbb28ebd0d913b4_12_1540737741628'
            }
    response = requests.get(baseurl2,headers=head)

    response.encoding = "utf-8"
    page_html=response.content
    soup=BeautifulSoup(page_html,'html.parser',from_encoding='utf-8')
    items=soup.find_all('li',class_='gl-item')
    with open('JD_Phone.csv', 'a', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        for data in items:
            p_name = data.find('div',class_='gl-i-wrap').find('div',class_='p-name p-name-type-2').em.text
            p_price = data.find('div',class_='gl-i-wrap').find('div',class_='p-price').i.text
            p_commit=data.find('div',class_='gl-i-wrap').find('div',class_='p-commit').strong.a.text
            p_shop = data.find('div', class_='gl-i-wrap').find('span', class_='J_im_icon').a.text
            write.writerow([p_name, p_price, p_commit,p_shop])
    f.close()

if __name__ == '__main__':
    for i in range(1, 4):
        print('first_page' + str(i))
        get_first(i)
        print('first_page' + str(i) + 'finish')
        print('last_page' + str(i))
        get_last(i)
        print('last_page' + str(i)+'finish')