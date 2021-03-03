import requests
import time
import smtplib
import datetime
import config

while True: 
    walgreensUrl = 'https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability'
    fetchStoresRiteAidUrl = 'https://www.riteaid.com/services/ext/v2/stores/getStores?address=10014&attrFilter=PREF-112&fetchMechanismVersion=2&radius=25'


    riteAidUrl = 'https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber=1225'

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    formattedTomorrow = tomorrow.strftime("%Y-%m-%d")

    monseyWalgreensData = {
    "serviceId": "99",
    "position": {
        "latitude": 40.96064,
        "longitude": -74.12322
    },
    "appointmentAvailability": {
        "startDateTime": formattedTomorrow
    },
    "radius": 25
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'x-xsrf-token': 'W7E3ol2WhoavYg==.kmNQhvVtPzeNJmlyEW5MurLQe+q28cetHyZF1sRW1cU=',
        'cookie' : 'mt.v=2.668312861.1612548470314; _gcl_au=1.1.1966866915.1612548472; liveagent_oref=https://www.walgreens.com/login.jsp?ru=%2Ffindcare%2Fvaccination%2Fcovid-19%2Flocation-screening%3Fflow%3Dcovidvaccine%26register%3Drx; liveagent_ptid=049dc0a6-c531-4280-b2c8-c66a04af2f89; USER_LOC=5K48AZ9EjJvMFONTAYYCCQuAIjJ7tdA3Dsgx%2F3ufIvHTo6c5I8JPZUljDA5Jtoqd; XSRF-TOKEN=wNRdLKl9xHHskg==.ciMjJ1I/sCHgfudnJdPCHko5fORkMrjw0I486G536SE=; rxVisitor=1613663484886OJVNVUS4NSPFJNRISBPPKITGKRM8RL24; uts=1613663485553; dtCookie=3$7E68B184F5420819FF1AF6C003EE035D|0eed2717dafcc06d|1; gRxAlDis=N; at_check=true; AMCVS_5E16123F5245B2970A490D45%40AdobeOrg=1; s_cc=true; headerReset=true; IM_throttle_1223=off; nsl=1; p_s=1; session_id=84c863ff-0f91-47c5-b3bb-773b749a2e3d; _uetvid=b23e32e06eec11ebac7159175c77ef8b; fc_vnum=22; liveagent_sid=8d9d387c-ef9d-4f75-880d-d6cf8b8ea894; liveagent_vc=9; encLoyaltyId=ChFmJndbYztfeLplNOpHLQ==; myWagId=201203178003854; 3s=w4XEncSgxIAjxZ90xa40wrA=; profileId=8653501330; FirstName=Joseph; 2fa=c6d0163019ca7e83a5cec69b51625e8b; AMCV_5E16123F5245B2970A490D45%40AdobeOrg=-1124106680%7CMCIDTS%7C18687%7CMCMID%7C06886892074255565162072098022670121179%7CMCAAMLH-1615160361%7C7%7CMCAAMB-1615160361%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1614562761s%7CNONE%7CvVersion%7C5.2.0%7CMCCIDH%7C-1091728757; JSESSIONID=kZszNwyB63ApTwHZb4B1RuJJ.p_dotcom88; wag_sc_ss_id=1830154027629832077; Adaptive=true; mbox=PC#d5ae5171e7564f19a8740ceb30a8601a.34_0#1677800560|session#dccf1b378bd34ef5a8081f2b6c460f39#1614557342; _4c_=%7B%22_4c_s_%22%3A%22jVTbTuMwEP0VlAeeSBO7cS6V0KoUkFhtWyiIfYzceNqYJnGw3aYF9d%2FXbgJESCuRh2TmzJnx3Jx3p8mhckYoRAEhJApD87pwNnBQzujdkZzZz84ZOTiM4oSQlesPV8wNVoy41MeBSxOSUTzMGAoS58LZ21gY%2BUmC%2FDBG5HjhZHUX493JBAMTCyUDFAyG7koZD%2F1mEHfo%2B0aupWDbTKf6UFteA8szxTbGwGDHM0gbznRuA0QJ%2FkJz4OtcWxhhG4XV0iZspIZXTDSfbnESfoGfXolvqUspGgXWcZJLUcJZHBtUmDY4U5oZUcIKpDwxcq1rNfK8pmkGDS3WEqBSg0yUHs0ysa20p0GWKs1ExbjmorJ1Kq5PNfX5HWza3bcYdD59WqRXN%2BPJfNY7T5WgJc%2FUt0OXnlLeCaqUh7zfjy4eYDzw3evoYeYpkoQxiaOYhCEm5Nf44eoSnZecXZoBxWGcYD8KjIGExEzOj7CfxD424%2FYRRqbR5%2BOHm0tkchpfpRqU7diXglutoetU2V1xyiJYKlU2NV6zl%2Bo1etlv3l6h4IZUQVPnQgvDmtlZ9%2BSsoErxrA%2FdS17CUw6S1rDVpmiD39JCgbE9c9O1vwCb4jBmHf%2BETcS2tt3uhZhSXqSPj%2FOe%2B2L%2FJBagjaHlT0S14rKkdlL3dG2ntOqof8R6DSy9q9o6O3W%2B1d%2F1dChZiy32%2FdgtdmtWbkIlzETT5XazA3kQFUzsunwkrAbwTCXCpPVacpnlS7FPl0C3%2BpCqXNQd89NUU6krkCrnH6Z61y3%2FaYemk7tro%2F9s1M6xu8AoCAOMQh%2BF5megdeGM4jDw7XNsDzjdZ%2FwTdnuvXKj%2B7xah727H4z8%3D%22%7D; atgjwt=1614556548269; s_sq=walgrns%3D%2526c.%2526a.%2526activitymap.%2526page%253Dwg%25253Afindcare%25253Acovid19%252520vaccination%25253Aland%2526link%253DGet%252520started%2526region%253DuserOptionButtons%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dwg%25253Afindcare%25253Acovid19%252520vaccination%25253Aland%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.walgreens.com%25252Ffindcare%25252Fvaccination%25252Fcovid-19%25252Flocation-screening%2526ot%253DA; bm_sz=C99DD1D77E6953A4CD34ADFAE69D81BD~YAAQJPo7F8ZuFvF3AQAATVsB9grpcqLm8CI3tvm956V2yOdOjUoBJoSAgmXUotVT2AwBENz/GImcnAPNyTlUp5KdpdIv6/SPwBOx83yPWQxw3pIWHPzHTJu3huhtib5HK2wPnZQRTqMXsZTRlFyYjWbyfOI8mf348cfoxj6iA6b5jA08WVsxQyfUkbsUENcN6pp4; wag_sid=onghkrhsvlulj2a5rf7cr1r0; ak_bmsc=B0434C4CB9EF2DA02E12717BF00E8AE1173BFA24EC11000034FA3E60EC7DB042~pljLPOD4HRkty3swetrb1j3SDEQLVGX3eG67v/LvSkEEZi2X0dYQRdVDtvwEU9jh2Xmv5dYiKFCOQMotMzguWl95Npw5euPDxuRY17Nd1V1sTdWeRShqRHgjUv6cDa48rs5re47sYdlHBeeN295dwlThpgNz1MaoNFs2Ygbwpc/gSu6Rb5slSWqzWlJa5Vm4xwJ4Iw5+Ym3qz8qPwK9ulRgpYmc1wvcJOXTeNavkGLzZW+rcfo4RH65XCTcDCuRZ4s; dtSa=-; dtLatC=1; _abck=E1F48C114D3AC4B472CD84EEA1FAF038~-1~YAAQ9b7CF5LIlcx3AQAAiFEp9gW39VGwKxx2Agmj8qY44reR3JDqNj0A0aNd4ME/dV74Xk7CuO2rb7NM7xuvz3o08Cw5vOeWlvqQgnoYaoLVEP0W0D3mcEA35fNptgSWBAT/5KuXnRMtZOvwUU4LVFZZlK4PUUbf3i+UWdLsUeXvqYuhQY90mX9/yAy7u2hx1lb5Zj7EopSVO/Z5Muq9hRn6tOYNdAKF6lcFKPavtv3ddWZKnQyF+xbjLCO7jZwV+0m9AaqteTC78ixzTAXLzRyWT6ve9uZSxHtiXAIn6O1nzAzT63xFJx/3xulnz2BUkDdc0Im77+sG3qHlOR9aj2hCJ8RkHG4eTfRbD9xE4WeVm4u89GCwLNBdhI/waPsve2YEhR6E2UlpLbL5cVR+naCtXti0L32Nb7f1~0~-1~-1; akavpau_walgreens=1614742940~id=23ee1d3c3d5cd2c09096cc63423d5801; bm_sv=F5A6EBC5830910726E1B4CFD11526C3A~ZNh9V1OLxopKIhWbOBqDYLfOX+MgbohKEQHsvJKFzVaPvUtLfo4HHepIB9N+I919PIJZGLDNJROZ8MBd3TQpunjGe6JxkAC1IiJIoQZzEA+0Ytf1J5BxalKIKAWg4rS3/2Zlm7ME7t56P5Ri5YpAn5LxNpewILBow7aU1g5cUuA=; rxvt=1614744443790|1614741823744; dtPC=3$142633520_462h8vAHJEBDWRLWSCDQSUAWCMQLDFRDMHALEK-0e2'}

    walgreensResponse = requests.post(walgreensUrl, json = monseyWalgreensData, headers = headers)
    walgreensAppointmentsAvailable = walgreensResponse.json().get("appointmentsAvailable")

    print(walgreensAppointmentsAvailable)
    print(walgreensResponse.text)
    appointmentsAvailable = walgreensAppointmentsAvailable

    if appointmentsAvailable != True:
        print("none available")
    else:
        print("appointments available")
        print("sending")

        fromaddr = config.senderEmail
        toaddrs  = config.toAddrses

        text = """\
        Walgreens: https://www.walgreens.com/findcare/vaccination/covid-19/location-screening
        """
        msg = 'Subject: {}\n\n{}'.format("Check Vaccine Site", text)

         # setup the email server,
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # add my account login name and password,
        server.login(config.senderEmail), config.senderPassword)
        
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


