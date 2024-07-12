import matplotlib.backends
import streamlit as st
import pandas
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

st.title('WIKI-FINDER')
st.markdown('author: Adrian')

url = str(st.text_input(label=('Wikipedia url: ')))
topic = str(st.text_input(label=('Topic to search: '))).title().replace(' ','_')

if not url:
    st.stop()

lurl = 'https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'

lan_page = requests.get(lurl)
lan_soup = BeautifulSoup(lan_page.content, 'html.parser')

try:
    page = requests.get(url)
except:
    st.error('NOT A WIKIPEDIA LINK')
    st.stop()

soup = BeautifulSoup(page.content, 'html.parser')
repeat, variation, ress = [],[],[]
count = 0
lang = soup.find('html').get('lang')
topic_times = 0
page_default = []
languague = []

total = 0

def iswiki(link):
    if link != None:
        if topic not in link: 
            return False
        if 'Special:' in link:
            return False 
        if str(link).count('/') > 2 and (lang in link or 'wikipedia' not in link):
            return False
        if 'Main_Page' in link:
            return False
        if '//' in link and lang in link:
            return False
        if 'wiki/' not in link:
            return False
        if '//www' in link:
            return False
        if '#' in link:
            return False
        if 'w/' in link:
            return False
    return True

for hyper in soup.find_all('a'):
    link = hyper.get('href')
    if str(link) in repeat:
        continue
    if iswiki(link) == True and link != None:
        count += 1
        if 'wikipedia.org' not in link:
            page_default.append(f'https://{lang}.wikipedia.org{link}')
            topic_times += 1
        else:
            variation.append(link)
        repeat.append(str(link))
    total += 1

data_default = {
    'Page':page_default,
    }

try:
    if len(page_default) != 0:
        pd = pandas.DataFrame(data_default)
        st.write(pd)
except:
    pass

if count == 0:
    st.text('\nNo links found\n')
elif len(variation) > 0 and topic == '':
    st.text('\nDifferent languagues\n')

chart_page = []

if len(variation) > 0 and topic == '':
    languague, languague_page_list = [],[]
    overend = -1
    for renlenvar in range(len(variation)):
        for j in lan_soup.find_all('tr'):
            limit = 0
            for i in range(len(variation)):
                try:
                    dot = str(variation[i]).find('.')
                    if str(variation[i][8:dot]) in j.find_all('td')[1].string and str(variation[i][8:10]) not in ress and j.find_all('td')[0].string != None:
                        languague.append(j.find_all('td')[0].string)
                        languague_page_list.append(variation[i])
                        ress.append(str(variation[i][8:10]))
                        limit = 1
                except:
                    continue
        for j in lan_soup.find_all('tr'):
            for i in range(len(variation)):
                    if limit == 0 and str(variation[i][8:10]) not in ress:
                        languague.append('Unknown')
                        languague_page_list.append(variation[i])
                        ress.append(str(variation[i][8:10]))
        if len(ress) == overend:
            break
        overend = len(ress)

    data = {
    'Languague':languague,
    'Page':languague_page_list,
    }

    pd = pandas.DataFrame(data)
    st.write(pd)
else:
    if len(page_default) != 0:
        chart_page = [total,topic_times]
        fig = plt.figure(figsize=(10, 7))
        plt.pie(chart_page, labels=[f'TOTAL ({total})',f'TOPIC ({topic_times})'],autopct='%1.1f%%',colors=['brown', 'orange'])
        st.pyplot(fig)

def create_pdf(languague):
    if len(chart_page) != 0:
        chart_file = "chart.png"
        plt.figure(figsize=(11, 9))
        plt.pie(chart_page, labels=[f'TOTAL ({total})',f'TOPIC ({topic_times})'],
                autopct='%1.1f%%',
                colors=['brown', 'orange'],
                explode=(0,0.1),
                shadow={'ox': -0.04,'oy': 0.04},
                textprops={'size': 'smaller'}, 
                radius=0.75)
        plt.xlabel('')
        plt.ylabel('')
        plt.title('TOPIC PERCENTAGE')
        plt.savefig(chart_file)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(200)
    'pdf.set_auto_page_break(auto=True, margin = 0.0)'
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(36, 99, 242)
    for i in range(len(page_default)):
        pdf.multi_cell(190, 6, str(page_default[i]), 1, 1, 'L')

    if len(languague) != 0:
        pdf.cell(190, 8, 'Different languagues', 0, 1, 'L')
        for i in range(len(languague)):
            pdf.cell(35, 6, str(languague[i]), 1, 0, 'L',True)
            pdf.multi_cell(155, 6, str(languague_page_list[i]), 1, 1, 'L')
    else:
        pdf.add_page()
        pdf.image(chart_file,x=-75,y=60)

    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    
    return pdf_bytes

if len(page_default) != 0:
    pdf_bytes = create_pdf(languague)
    st.download_button('DOWNLOAD',pdf_bytes,'Link_List.pdf','application/pdf')
