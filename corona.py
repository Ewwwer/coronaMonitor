#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import re
import time
import math
import datetime
import logging
import sys
sys.path.insert(1, "./lib") #Adds lib folder in this directory to sys

import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

def main():
    try: 
        while True:
            print ("Update " + str(datetime.datetime.now()))

            #URL de página datos
            url_c = "https://corona.help/country/senegal"
            page_c = requests.get(url_c)
            soup_c = BeautifulSoup(page_c.text, 'html.parser')
        
            # Ajustar: Coge los activity timeline, texto en ingles explicando la evolución (quiero poner max. 2 )
            #for litag in soup_c.find_all('ul', {'class': 'activity-timeline timeline-left list-unstyled'}):
            #for ultag in soup_c.find_all('ul', {'class': 'activity-timeline timeline-left list-unstyled'}):
        
                #for litag in ultag.find_all('li'):
                    #print(litag.text[2])



            

            
            history = re.findall('^\s+data: \[([0-9,]+)\],$',str(soup_c),re.MULTILINE)

            history_cases = history[0].split(',')
            history_deaths = history[1].split(',')
            history_cured = history[2].split(',')

            # Print
            
            current_day_all_infected = infections_c = soup_c.select('h2')[1].text.strip()
            current_day_0_infected_today = soup_c.select('h2')[2].text.strip()
            current_day_all_death = soup_c.select('h2')[3].text.strip()
            current_day_0_death_today = soup_c.select('h2')[4].text.strip()
            all_recoveries_total = soup_c.select('h2')[5].text.strip()
            current_day_0_recoveries = soup_c.select('h2')[6].text.strip()
            total_tests = soup_c.select('h2')[11].text.strip()
            today_current_tests = soup_c.select('h2')[12].text.strip()
            activity_timeline = soup_c.select('h4')[1].text.strip()
            
            #Casos confirmados totales
            current_day_all_infected = current_day_all_infected.encode('ascii', 'ignore')
            infected_h = current_day_all_infected
            infected_value_all= "Total casos confirmados:  " + str(current_day_all_infected)
            print (infected_value_all)

            #Casos confirmados hoy
            current_day_0_infected_today = current_day_0_infected_today.encode('ascii', 'ignore')
            infeccion_diaria_h = current_day_0_infected_today
            infeccion_diaria_value= "Casos confirmados de hoy: " + str(current_day_0_infected_today)
            print (infeccion_diaria_value)
            quita_coma_calculo_incidencia_confirmados_diarios = infeccion_diaria_value.replace("," , "")
            

            #Muertes totales
            current_day_all_death = current_day_all_death.encode('ascii', 'ignore')
            muertes_totales = current_day_all_death
            muerte_tota_value= "Total muertes: " + str(current_day_all_death)
            print (muerte_tota_value)

            #Muertes Diarias
            current_day_0_death_today = current_day_0_death_today.encode('ascii', 'ignore')
            muertes_hoy = current_day_0_death_today
            muerte_hoy_value= "Muertes hoy: " + str(current_day_0_death_today)
            
            print (muerte_hoy_value)

            #Tests diarios
            today_current_tests = today_current_tests.encode('ascii', 'ignore')
            test_hoy = today_current_tests
            test_hoy = "Tests realizados: " + str(today_current_tests)
            quita_coma_calulo_incidencia_test = test_hoy.replace(",'" , "")


            
            

            #Calulo positividad diaria
            #print(quita_coma_calculo_incidencia_confirmados_diarios)
            #porcentaje_diario_contagio = (quita_coma_calulo_incidencia_test) * (quita_coma_calculo_incidencia_confirmados_diarios) / 100

            #intentamos conectar con la pantalla: 
            try:
                epd = epd2in13_V2.EPD() # get the display
                epd.init(epd.FULL_UPDATE)           # initialize the display
                print("Clear...")    # prints to console, not the display, for debugging
                epd.Clear(0xFF)
                #Mostramos en pantalla resultados 
                title = ImageFont.truetype("pic/Font.ttc", 25)
                font = ImageFont.truetype("pic/Font.ttc", 15)
                fontlittle = ImageFont.truetype("pic/Font.ttc", 12)
                logging.info("1.Drawing on the image...")
                image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
                draw = ImageDraw.Draw(image)
                draw.text((55, 5), "SPEEDTEST", font = title, fill = 0)
                draw.text((75, 30), str(now.strftime("%d-%m %H:%M")), font = fontlittle, fill = 0)

                draw.text((20, 71), str(ping), font = font, fill = 0)
                draw.text((20, 90), "ping", font = fontlittle, fill = 0)

                draw.text((103, 71), str(download), font = font, fill=0)
                draw.text((103, 90), "download", font = fontlittle, fill=0)

                draw.text((180,71), str(upload), font = font, fill=0)
                draw.text((180, 90), "upload", font = fontlittle, fill=0)

                epd.display(epd.getbuffer(image))




    finally:
        print("none")

# Run
if __name__ == "__main__":
    main()