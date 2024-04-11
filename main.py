from time import sleep

from yf_service_proxy import YFserviceProxy

yf_service = YFserviceProxy()


expiry_dates = {
    '16-01-2026': 250,
    '18-12-2026': 300,
    '18-06-2026': 350
}


while True:
    yf_service.schedule.run_pending()

    last_options = yf_service.last_options
    expirations = yf_service.expirations

    if expirations and last_options:
        print(len(last_options))
        print(len(expirations))

    sleep(1)
