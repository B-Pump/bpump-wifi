import network
import time


def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        print("Connexion au WiFi...")
        wlan.active(True)
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            time.sleep(1)

    print("Connecté au WiFi:", wlan.config("essid"))
    print("Adresse IP:", wlan.ifconfig()[0])


# Remplacez "nom_du_ssid" et "mot_de_passe" par les informations appropriées
connect_to_wifi("nom_du_ssid", "mot_de_passe")
