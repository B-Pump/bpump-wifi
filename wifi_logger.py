import network
import time

def connect_to_wifi(ssid, password, max_attempts=30):
    wlan = network.WLAN(network.STA_IF)
    attempt_count = 0

    if not wlan.isconnected():
        print("WiFi connection in progress...")

        wlan.active(True)
        wlan.connect(ssid, password)

        while not wlan.isconnected() and attempt_count < max_attempts:
            time.sleep(1)
            attempt_count += 1

        if wlan.isconnected():
            print("Connected to WiFi :", wlan.config("essid"))
            print("IP address :", wlan.ifconfig()[0])
        else:
            print("Failed to connect to WiFi. Please check your credentials")

    else:
        print("Already connected to WiFi :", wlan.config("essid"))
        print("IP address :", wlan.ifconfig()[0])

connect_to_wifi("nom_du_ssid", "mot_de_passe")