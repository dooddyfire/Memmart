import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.memmert.com/en/products/selector?fbclid=IwY2xjawH-QaRleHRuA2FlbQIxMAABHZIrgMs51TEzGLazIPQ2kvFcDdnLmhMyLzDAwOLErS5pJJK7TSB-RqM0_w_aem_rLFEpos-aa1eV6MPncRy0Q#!filters=%7B%7D'
res = requests.get(url)

soup = BeautifulSoup(res.content,'html.parser')


url_lis = []
title_lis = []
desc_lis = []
headline_lis = []
img_lis = []
brochure_lis = []
option_lis = []
spec_lis = []
intro_lis = []
model_lis = []

for i in soup.find_all('div',{'class':'pim-series-item-content'}): 

    url = 'https://www.memmert.com'+i.find('a')['href']
    url_lis.append(url)

    title = i.find('h4').text.strip() 
    print(title)

    title_lis.append(title)

    img = 'https://www.memmert.com'+i.find('img')['src']
    img_lis.append(img)
    print(img)

    desc = i.find('p',{'class':'pim-short-description'}).text.strip() 
    print(desc)
    desc_lis.append(desc)

    resx = requests.get(url)
    soupx = BeautifulSoup(resx.content,'html.parser')

    headline = soupx.find('div',{'class':'header-slider-content'}).text.strip() 
    headline_lis.append(headline)


    btn_prod_info_lis = [ k['href'] for k in soupx.find_all('a',{'class':'btn-productinfo'})]
    print(btn_prod_info_lis)

    brochure =  'https://www.memmert.com'+btn_prod_info_lis[0]
    print('Brochure : ',brochure)
    brochure_lis.append(brochure)

    option = 'https://www.memmert.com'+btn_prod_info_lis[-1]
    print('Option : ',option)
    option_lis.append(option)

    intro = soupx.find('div',{'class':'pim-introduction'}) 
    print(intro)

    introduction = intro.find('div',{'class':'col-sm-12'}).text.strip() 
    intro_lis.append(introduction)
    print('Introduction : ',introduction)

    spec = intro.find('ul',{'class':'pim-introduction-hardfacts'}).text.strip() 
    spec_lis.append(spec)
    print('Spec : ',spec)

    model = "\n".join([ c.text.replace('Description','').replace('Details','').strip() for c in soupx.find('table',{'class':'pim-models-table'}).find_all('tr')]) 
    model_lis.append(model)

df = pd.DataFrame()
df['Title'] = title_lis 
df['Description'] = desc_lis 
df['Image'] = img_lis 
df['Headline'] = headline_lis 
df['Brochure'] = brochure_lis 
df['Option'] = option_lis 
df['Spec'] = spec_lis 
df['Introduction'] = intro_lis 
df['Model'] = model_lis 
df.to_excel('all2312568.xlsx')