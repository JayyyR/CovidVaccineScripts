import requests
import time
import smtplib
import datetime
import config

lastStoreFound = ""
while True:

    zipToSearch = "10549"

    fetchStoresRiteAidUrl = 'https://www.riteaid.com/services/ext/v2/stores/getStores?address={}&attrFilter=PREF-112&fetchMechanismVersion=2&radius=25'.format(zipToSearch)
    fetchStoresResponse = requests.get(fetchStoresRiteAidUrl)

    nearbyStores = []

    data = fetchStoresResponse.json().get("Data").get("stores")

    for store in data:
        nearbyStores.append(store)

    storeWithApptAvailable = None

    if (len(nearbyStores) == 0):
        print("no nearby stores")
        break

    for store in nearbyStores:
        apptUrl = 'https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber={}'.format(store.get('storeNumber'))
        apptsAvailableResponse = requests.get(apptUrl)

        print(apptsAvailableResponse.text)
        
        apptAvailable = apptsAvailableResponse.json().get('Data').get('slots').get('1')

        print("{} : {}".format(store.get('storeNumber'), apptAvailable))

        if (apptAvailable != False):
            storeWithApptAvailable = store
            if lastStoreFound != storeWithApptAvailable.get('storeNumber'):
                break

        print("-------------")

    appointmentsAvailable = storeWithApptAvailable != None

    if appointmentsAvailable == False:
        print("none available")
        lastStoreFound = ""
    else:
        print("appointments available")

        if (lastStoreFound == storeWithApptAvailable.get('storeNumber')):
            print("same store found")
            time.sleep(20)
            continue

        lastStoreFound = storeWithApptAvailable.get('storeNumber')

        storeAddress = "{}, {}, {}, {}".format(storeWithApptAvailable.get('address'), storeWithApptAvailable.get('city'), storeWithApptAvailable.get('state'), storeWithApptAvailable.get('zipcode'))
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


