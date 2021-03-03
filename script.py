
import requests
from requests_html import AsyncHTMLSession
import time
import asyncio
import smtplib
import config


# while this is true (it is true by default),
async def scriptTest():
    lastProviderNameNYCHH = ""
    while True:

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        session = AsyncHTMLSession()
        #hackensack = await session.get("https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916", headers = headers)
        #valley = await session.get("https://www.valleyhealth.com/services/covid-19-vaccine", headers = headers)
        #holyname = await session.get("https://rodda.holyname.org/COVID19VAC", headers = headers)
        nycHnH = await session.get("https://epicmychart.nychhc.org/MyChart/SignupAndSchedule/EmbeddedSchedule?id=RES,11736948,11736949,11736950,11736951,11736952,11736953,11736954,11736955,11736956,11736957,11736958,11736959,11703875,11703874,11703367,11703868,11703869,11703873,11703870,11703871,11703872&dept=1012009896,1020009908,1015009901,1011009919,1021009929,1022008535,1013009914,1014009903,1023009916,1021009930,1024009929,1025009903,1022008534,1023009915,1055009828,1050009831,1051009831,1052000031,1053009828,1054009831,1051102309,&vt=11790692", headers = headers)
        #westchester = await session.get("https://apps2.health.ny.gov/doh2/applinks/cdmspr/2/counties?OpID=B9996975FFD804BCE0530A6C7C166199", headers = headers)

        #await holyname.html.arender(sleep=2)
        await nycHnH.html.arender(timeout=20)
        #await hackensack.html.arender(sleep=3)
        #await valley.html.arender(sleep=3)
        #await westchester.html.arender(sleep=3)

        #await hackensack.session.close()
        #await valley.session.close()
        #await holyname.session.close()
        await nycHnH.session.close()
        #await westchester.session.close()

        #holynameSearch = holyname.html.search('Holy Name is not scheduling appointments for the COVID-19 vaccine')
        appointmentsAvailableAtHolyName = False#= holynameSearch == None

        #hackensackSearch = hackensack.html.search('card withProvider')
        appointmentsAvailableHackensack = False#hackensackSearch != None

        #valleySearch = valley.html.search('NO APPOINTMENTS ARE AVAILABLE AT THIS TIME')
        appointmentsAvailableValley = False#valleySearch == None
   
        nycHnHSearch = nycHnH.html.search('card withProvider')
        appointmentsAvailableNycHnH = nycHnHSearch != None

        nycHnHproviderNameText = None
        nycHnHproviderName = nycHnH.html.find('.providername', first=True)
        if (nycHnHproviderName != None):
            nycHnHproviderNameText = nycHnHproviderName.text
    
        print("provider found: {}".format(nycHnHproviderNameText))
        if not(appointmentsAvailableNycHnH):
            print("resetting last provider")
            lastProviderNameNYCHH = "" #reset last provider if there are none available
        
        if(appointmentsAvailableNycHnH and (lastProviderNameNYCHH == nycHnHproviderNameText)):
            print("appointments available but same provider")

        #only keep notifying if the provider has changed
        notifyAboutNycHnH = appointmentsAvailableNycHnH and (lastProviderNameNYCHH != nycHnHproviderNameText)
                
        appointmentsAvailable = appointmentsAvailableHackensack or appointmentsAvailableValley or appointmentsAvailableAtHolyName or notifyAboutNycHnH

        if not(appointmentsAvailable):
            print("none available")
            time.sleep(24)
            continue
        else:
            print("appointments available")
            print("sending")

            fromaddr = config.senderEmail
            toaddrs  = config.toAddrses

            msg = ""
            text = ""
            if appointmentsAvailableHackensack:
                text = """\
                Hackensack: tinyurl.com/yw7jynau
                """
            if appointmentsAvailableValley:
                text = """\
                Valley: https://www.valleyhealth.com/services/covid-19-vaccine
                """
            if appointmentsAvailableAtHolyName:
                text = """\
                Holy Name: https://rodda.holyname.org/COVID19VAC
                """
            if appointmentsAvailableNycHnH:
                address = nycHnH.html.find('.departmentAddress.subtle', first=True)
                providerName = nycHnH.html.find('.providername', first=True)
                addressText = ""
                providerNameText = ""
                if (address != None):
                    addressText = address.text
                if (providerName != None):
                    providerNameText = providerName.text
                    lastProviderNameNYCHH = providerNameText

                print(addressText)
                print(providerNameText)
                text = "{}-{}-https://tinyurl.com/yu3uuojj".format(providerNameText, addressText)

            msg = 'Subject: {}\n\n{}'.format("Check Vaccine Site", text)
            
            # setup the email server,
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(config.senderEmail, config.senderPassword)
            
            # Print the email's contents
            print('From: ' + fromaddr)
            print('To: ' + str(toaddrs))
            print('Message: ' + msg)
            
            # send the email
            server.sendmail(fromaddr, toaddrs, msg)
            # disconnect from the server
            server.quit()

            #if appointmentsAvailableNycHnH or appointmentsAvailableHackensack:
            #    continue #this happens pretty often and it's hard to get em
            #else:
            #    break
            time.sleep(5)
            continue

asyncio.run(scriptTest())

