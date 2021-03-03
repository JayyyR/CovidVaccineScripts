import requests
import time
import smtplib
import datetime
import config

while True:

    zipToSearch = "10014"

    fetchStoresRiteAidUrl = 'https://www.riteaid.com/services/ext/v2/stores/getStores?address={}&attrFilter=PREF-112&fetchMechanismVersion=2&radius=50'.format(zipToSearch)
    fetchStoresResponse = requests.get(fetchStoresRiteAidUrl)

    nearbyStores = []

    data = fetchStoresResponse.json().get("Data").get("stores")

    for store in data:
        nearbyStores.append(store)

    storeWithApptAvailable = None

    for store in nearbyStores:
        apptUrl = 'https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber={}'.format(store.get('storeNumber'))
        apptsAvailableResponse = requests.get(apptUrl)

        print(apptsAvailableResponse.text)
        
        apptAvailable = apptsAvailableResponse.json().get('Data').get('slots').get('1')

        print("{} : {}".format(store.get('storeNumber'), apptAvailable))

        if (apptAvailable != False):
            storeWithApptAvailable = store
            break

        print("-------------")

    appointmentsAvailable = storeWithApptAvailable != None

    if appointmentsAvailable == False:
        print("none available")
    else:
        print("appointments available")

        storeAddress = "{}, {}, {}".format(storeWithApptAvailable.get('address'), storeWithApptAvailable.get('city'), storeWithApptAvailable.get('state'))
        print("Found store: {}".format(storeAddress))
        

        fromaddr = config.senderEmail
        toaddrs  = config.toAddrses

        text = "RiteAid: {} -- https://www.riteaid.com/pharmacy/apt-scheduler".format(storeAddress)
        msg = 'Subject: {}\n\n{}'.format("Check Vaccine Site", text)

         # setup the email server,
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # add my account login name and password,
        server.login(config.senderEmail, config.senderPassword)
        
        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
        
        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()

    time.sleep(20)
    continue


