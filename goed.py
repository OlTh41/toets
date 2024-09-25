from gpiozero import LED, Button
import time

# Pinconfiguratie met gpiozero
auto_rood = LED(17)
auto_oranje = LED(27)
auto_groen = LED(22)
voetganger_rood = LED(23)
voetganger_groen = LED(24)
drukknop = Button(25)

# Starttoestand: auto's groen, voetgangers rood
auto_groen.on()
auto_rood.off()
auto_oranje.off()
voetganger_rood.on()
voetganger_groen.off()

# Variabele voor blokkering
laatste_oversteek_tijd = 0

    while True:
        # Als er op de knop is gedrukt en er zijn meer dan 60 seconden voorbij sinds de laatste oversteek
        if drukknop.is_pressed and time.time() - laatste_oversteek_tijd > 60:
            # Auto's stoppen: Oranje -> Rood
            auto_groen.off()
            auto_oranje.on()
            time.sleep(3)
            auto_oranje.off()
            auto_rood.on()

            # Voetgangers groen licht geven
            voetganger_rood.off()
            voetganger_groen.on()
            time.sleep(120)  # Voetgangers krijgen 2 minuten groen

            # Terug naar standaard: auto's groen, voetgangers rood
            voetganger_groen.off()
            voetganger_rood.on()

            auto_rood.off()
            auto_oranje.on()
            time.sleep(3)
            auto_oranje.off()
            auto_groen.on()

            # Blokkering van 60 seconden
            laatste_oversteek_tijd = time.time()

        time.sleep(0.1)  # Kleine pauze om de CPU te ontlasten


