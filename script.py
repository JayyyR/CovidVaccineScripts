
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

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'Cookie': 'JSESSIONID=1yYElbPDFBvNVI9D3rI8UayGOQTZ0GxpwUuvZXETNeyAOG3Dm6d3!1138710338; TSb775c79f_75=TSb775c79f_rc=1&TSb775c79f_id=5&TSb775c79f_cr=08f09154e8ab28005c736a2e327f3fa23865581e59f810371b1f3373f8143e6bcc7c532b8da752419911a557de8657da:085a78dfa604b0007203b39a120f4607cd45053594b852317f99414d748cb294afd0eac4aab96db7d3f4d7dd5d8d4f8bb8ba8c21da0ca7105468999b69df835e3ca0183bbef7be246476834f57ad3978108b72a22ea26d0559f7ff5815f8d908eb3f702fde2c95f0d23e802ce9dd1ce00100739c2fb96c7e776f9886821b7c3eef7e3b6cd1f0937f0b817a4a86c1a98829b5f355b591fae614ccc3e9e523131c586b6f741959aa2bd738aca3f9123bda790df6badaeb1c37&TSb775c79f_ef=&TSb775c79f_pg=0&TSb775c79f_ct=0&TSb775c79f_bg=08f09154e8ab20003c2b2e15c3f888b765f70cceefee1700d9a3b4add5b5eba1a06f2795a7c412fa08d4c56ec70a2800a7eec3a2914adef9efc6fec22ff5c8b8c83c0d295d54022cd3894bddf16b52e9feb6268c5d5b1ef1&TSb775c79f_rf=https%3a%2f%2fapps7.health.ny.gov%2fdoh2%2fapplinks%2fcdmspr%2f2%2fcounties%3fOpID%3dE9986975FF8F14BCE0530A6A7B166129; tc_ptidexpiry=1668800728722; tc_ptid=5MHtTac6qJ60sFsJ6bXwQw; nmstat=b778e704-a528-b6e1-6ede-1c0f020643c4; _ga=GA1.3.1213286563.1605728729; __cfduid=d0e833b577cbd4509a17cb17ccb4c759a1614004335; rxVisitor=1614004367234QKJ8VSRF1EADNRAMS7C8O9EN3MKNLSSJ; BIGipServer~HEALTH~DOH_CDMS_APPS7_PROD_POOL=462777354.42255.0000; dtCookie=3$0F136E5615CF421A80844D1BF6B655AB|bc6d9b76d1b6ad10|1|59a18996d8b41ffb|1|7472e692e0fa4d9e|1|ecb158f5b759a391|1|651ade742d742d05|1; arp_scroll_switch=1; _gid=GA1.2.1389152933.1614984757; _ga=GA1.1.1213286563.1605728729; rxvt=1614986724919|1614984623453; dtPC=3$384924694_421h-vRNKFARHRMPCGBFPKRLFPGHHUDFOFFPIK-0e39; dtLatC=1; dtSa=true%7CKD%7C-1%7CPage%3A%20counties%3FOpID%3DE9986975FF8F14BCE0530A6A7B166129%7C-%7C1614985862683%7C384924694_421%7Chttps%3A%2F%2Fapps7.health.ny.gov%2Fdoh2%2Fapplinks%2Fcdmspr%2F2%2Fcounties%3FOpID%3DE9986975FF8F14BCE0530A6A7B166129%7CWelcome%20to%20CDMS%20Registration%7C1614984926009%7C%7C; _ga_4N4QD1GFGL=GS1.1.1614984623.64.1.1614985862.0; TSPD_101=08f09154e8ab28005c736a2e327f3fa23865581e59f810371b1f3373f8143e6bcc7c532b8da752419911a557de8657da:',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Host': 'apps7.health.ny.gov',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive'
        }

        
        session = AsyncHTMLSession()
        hackensack = await session.get("https://mychart.hmhn.org/MyChart/SignupAndSchedule/EmbeddedSchedule?dept=1110101656,1110301124&vt=112916", headers = headers)
        #valley = await session.get("https://www.valleyhealth.com/services/covid-19-vaccine", headers = headers)
        #holyname = await session.get("https://rodda.holyname.org/COVID19VAC", headers = headers)
        nycHnH = await session.get("https://epicmychart.nychhc.org/MyChart/SignupAndSchedule/EmbeddedSchedule?id=RES,11736948,11736949,11736950,11736951,11736952,11736953,11736954,11736955,11736956,11736957,11736958,11736959,11703875,11703874,11703367,11703868,11703869,11703873,11703870,11703871,11703872&dept=1012009896,1020009908,1015009901,1011009919,1021009929,1022008535,1013009914,1014009903,1023009916,1021009930,1024009929,1025009903,1022008534,1023009915,1055009828,1050009831,1051009831,1052000031,1053009828,1054009831,1051102309,&vt=11790692", headers = headers)
        #westchester = await session.get("https://apps2.health.ny.gov/doh2/applinks/cdmspr/2/counties?OpID=B9996975FFD804BCE0530A6C7C166199", headers = headers)
        #javitsJnJ = await session.get("https://apps7.health.ny.gov/doh2/applinks/cdmspr/2/counties?OpID=E9986975FF8F14BCE0530A6A7B166129", headers = headers)

        #await holyname.html.arender(sleep=2)
        await nycHnH.html.arender(timeout=40)
        await hackensack.html.arender(timeout=40)
        #await valley.html.arender(sleep=3)
        #await westchester.html.arender(sleep=3)
        #await javitsJnJ.html.arender(timeout=40)

        await hackensack.session.close()
        #await valley.session.close()
        #await holyname.session.close()
        await nycHnH.session.close()
        #await westchester.session.close()
        #await javitsJnJ.session.close()

        #print(javitsJnJ.html.html)

        #holynameSearch = holyname.html.search('Holy Name is not scheduling appointments for the COVID-19 vaccine')
        appointmentsAvailableAtHolyName = False#= holynameSearch == None

        hackensackSearch = hackensack.html.search('card withProvider')
        appointmentsAvailableHackensack = hackensackSearch != None

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
            time.sleep(8)
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
                text = "NYCHHVac {}-{}-https://tinyurl.com/yu3uuojj".format(providerNameText, addressText)

            msg = 'Subject: {}\n\n{}'.format("Vaccine!", text)
            
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

