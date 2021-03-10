import requests
import time
import smtplib
import datetime
import config

lastStoreFound = ""
while True:

    zipToSearch = "10014"

    cvsUrl = 'https://www.cvs.com/Services/ICEAGPV1/immunization/1.0.0/getIMZStores'

    payloadData = {
        "requestMetaData": {
            "appName": "CVS_WEB",
            "lineOfBusiness": "RETAIL",
            "channelName": "WEB",
            "deviceType": "DESKTOP",
            "deviceToken": "7777",
            "apiKey": "a2ff75c6-2da7-4299-929d-d670d827ab4a",
            "source": "ICE_WEB",
            "securityType": "apiKey",
            "responseFormat": "JSON",
            "type": "cn-dep"
        },
        "requestPayloadData": {
            "selectedImmunization": [
            "CVD"
            ],
            "distanceInMiles": 25,
            "imzData": [
            {
                "imzType": "CVD",
                "ndc": [
                "59267100002",
                "59267100003",
                "59676058015",
                "80777027399"
                ],
                "allocationType": "1"
            }
            ],
            "searchCriteria": {
            "addressLine": "10566"
            }
        }
    }

    headers = {
        'origin': 'https://www.cvs.com',
        'referer': 'https://www.cvs.com/vaccine/intake/store/cvd-store-select/first-dose-select',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'content-type': 'application/json',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '493',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'cookie': 'pe=p1; acctdel_v1=on; adh_new_ps=on; adh_ps_pickup=on; adh_ps_refill=on; buynow=off; sab_displayads=on; dashboard_v1=off; db-show-allrx=on; disable-app-dynamics=on; disable-sac=on; dpp_cdc=off; dpp_drug_dir=off; dpp_sft=off; getcust_elastic=on; echomeln6=off-p0; enable_imz=on; enable_imz_cvd=on; enable_imz_reschedule_instore=off; enable_imz_reschedule_clinic=off; flipp2=on; gbi_cvs_coupons=true; ice-phr-offer=off; v3redirecton=false; mc_cloud_service=on; mc_hl7=on; mc_home_new=off1; mc_ui_ssr=off-p2; mc_videovisit=on; memberlite=on; pivotal_forgot_password=off-p0; pivotal_sso=off-p0; pbmplaceorder=off; pbmrxhistory=on; ps=on; refill_chkbox_remove=off-p0; rxdanshownba=off; rxdfixie=on; rxd_bnr=on; rxd_dot_bnr=on; rxdpromo=on; rxduan=on; rxlite=on; rxlitelob=off; rxm=on; rxm_phone_dob=off-p1; rxm_demo_hide_LN=off; rxm_phdob_hide_LN=on; rxm_rx_challenge=on; s2c_akamaidigitizecoupon=on; s2c_beautyclub=off-p0; s2c_digitizecoupon=on; s2c_dmenrollment=off-p0; s2c_herotimer=off-p0; s2c_newcard=off-p0; s2c_papercoupon=on; s2c_persistEcCookie=on; s2c_smsenrollment=on; s2cHero_lean6=on; sft_mfr_new=on; sftg=on; show_exception_status=on; v2-dash-redirection=on; ak_bmsc=F9641332895CC328D5070E1B8EAA4A46ACE80754F02E000066F4426023069073~plHLIXwAW/fieoDRnIop63E3ui+Y10Hy9HETAg/272iImaOC0x4hXEqLKTHfLH44RD9Tl/sF5F9BPouJc5GXLsb9CDTlv8x07OwCFGDaC8Dn8rrsef9f0hq1fLAMGG3N6VigCfz3YN1sDFWGYjCYCKVRsVkEZvK18i7h3VUUY1mwKWwecbVVQzEbuCK9A+EbSb1CPD6G9dlz82q87sx2+6cMbYXcH7EMlzd6qONqZ6kXQ=; bm_sz=FE22CAC21614AED0590C8B808904C968~YAAQVAforPKwOc13AQAAGrKKBQuXYXx6jx4RvbXRaqpqKTe0Aqa+bQOjpmO5x/3yF3aNaUeU7+aMjqDMU1y3IO/fifXxnYTol6x4HeCOAdSnyTy5HvV4iL5WfZh/BpFidqMfsYnXesm+IpXVbs0qqjmPvk1EFxmcke5/JmPJiaQZHCZ1Mq0Mh8DpAZE9; mt.v=2.927859722.1615000679054; _group1=quantum; mt.sc={"i":1615000679230,"d":[]}; AMCVS_06660D1556E030D17F000101@AdobeOrg=1; AMCV_06660D1556E030D17F000101@AdobeOrg=-330454231|MCIDTS|18693|MCMID|12576002784729104012047202548104481733|MCAAMLH-1615605479|7|MCAAMB-1615605479|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1615007879s|NONE|MCAID|NONE|vVersion|3.1.2; CVPF=CT-USR; s_cc=true; _gcl_au=1.1.165531170.1615000680; gbi_sessionId=cklx5pgc300003h98uyg22uoj; gbi_visitorId=cklx5pgc300013h988bel0qkk; _4c_mc_=2be5685b-b566-4ed7-a309-aab94796a08c; QuantumMetricSessionID=f8cface9ca0b117c33c37611cd9210bf; QuantumMetricUserID=5bd2b0daa091b5f977340d0768fb0d0a; akavpau_vp_www_cvs_com_vaccine=1615001290~id=fc1e28400b84fb0f26293dcbb9753a56; akavpau_vp_www_cvs_com_vaccine_covid19=1615001290~id=fc1e28400b84fb0f26293dcbb9753a56; mt.cem=210216-MCcom-Header-Banner - B-JUST-the-homepage-header; mt.mbsh={"fs":1615000691384,"sf":1,"lf":1615000736430}; akavpau_www_cvs_com_general=1615001644~id=3b09b1cc6fb94f2f285f6f9a8ac74993; s_sq=[[B]]; gpv_e5=cvs|dweb|vaccine|intake|store|cvd-store-select|rx: immunizations: first dose scheduler; gpv_p10=www.cvs.com/vaccine/intake/store/cvd-store-select/first-dose-select; RT="z=1&dm=cvs.com&si=0ddb1c81-df07-480c-a1bd-0039074efe91&ss=klx5pf2y&sl=k&tt=2nh&bcn=//36a3fec2.akstat.io/"; ADRUM_BT=R:75|i:1684|g:56d62b52-031b-4ef0-84ad-fa50253db9f0309640|e:191|n:customer1_d6c575ca-3f03-4481-90a7-5ad65f4a5986; bm_sv=447DFC867E1CB1EBCD64FCE3122BF4ED~RkS5i1g/onwbFJjiFxXDU88HlUeYZWCaJIRcv6Q7kNIx+2icsQlYPYrW9RgsTmBdaS0z3cKF1pSi33aEJsX7QqoDm0Pdbmgy9co1k4t4WX4gA86cCJPG+X3eFVH3OpXBQI0VVzbWGShp50wtWU/tmw==; _abck=CA9157650030B2D4AD713CD651E48D48~0~YAAQVgforHtl//93AQAA2PmUBQUT8A38gKbanJokYD0afNNuyLNhtJa/W3sLZMFh1lRGvXvO3Vitukub5mB3yogQdcUKVprEnfXe9+vazUHmaUtxOpJKgYY/9pOFqEMmFtcGiHj/hGsgzF1ftT7g5sneKS84VsZR6X4pnxuExK1se0z+xwotA+MQ6k49p7AAy/4u8AudbrkoZyZ4Hc71NaeWNHy1wCkyHRPGn5SadUALSebsAbghgzR3ZjG+cVwjhDdsgwCYhkl4oaezVAU+znTq4x2MUhZKZEISdlvJ6x3aArghBq93xvT/HucHWTepRVhEaYaW0OV+2KmUpw3fKlG/ZpnYkFgXgv1GwxI/MHX4TnWUS5JYPEcc9qO/Mvsdr7bbsM4gcBP95xGyTpVEPGoZuNy4~-1~-1~-1; qmexp=1615003164605; utag_main=v_id:0178058ab3240015e623824b282703079003207100b7e$_sn:1$_ss:0$_pn:2;exp-session$_st:1615003164632$ses_id:1615000679204;exp-session$vapi_domain:cvs.com'
    }

    cvsResponse = requests.post(cvsUrl, json = payloadData, headers = headers)
    print(cvsResponse.text)

    foundAppts = cvsResponse.json().get('responseMetaData').get('statusDesc')

    appointmentsAvailable = foundAppts == "Success"

    if appointmentsAvailable == False:
        print("none available")
        lastStoreFound = ""
    else:
        print("appointments available")

        responsePayload = cvsResponse.json().get('responsePayloadData')

        locationText = ""
        if responsePayload != None:
            locations = responsePayload.get('locations')
            locationText = locations[0].get('addressCityDescriptionText')
            print(locationText)
        

        fromaddr = config.senderEmail
        toaddrs  = config.toAddrses

        text = "CVS: {} -- https://www.cvs.com/vaccine/intake/store/cvd-store-select/first-dose-select".format(locationText)
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

    time.sleep(5)
    continue


