# -----------------------------------------
#                 NOTES 
# -----------------------------------------
"""
Dieter Steinhauser
10/2023

PowerPico

Drone Maestros Power Management and Measurement Pico. Controls DC/DC converters over I2C, 
Measures Rail outputs, Measure battery Charging/Discharging, and Solar output.

"""

# -----------------------------------------
#               IMPORTS
# -----------------------------------------

import gc
import time
from machine import Pin, Timer, ADC, freq, I2C, UART, WDT

# -----------------------------------------
#         CONSTANTS/VARIABLES
# -----------------------------------------   

# ------------------

DEBUG = False # Debug output on/off
I2C_EN = False # I2C Communication at the start of system.
WATCHDOG_EN = False # Watchdog timer usage

# ------------------

REFRESH_RATE = 5 # Frequency in Hz
REFRESH_PERIOD = int((1 / REFRESH_RATE) * 1000) # delay in milliseconds


# -------------------------------------------------------------
#           INITIALIZATION
# -------------------------------------------------------------

# -----------------------------------------
#           SYSTEM CLOCK
# -----------------------------------------

DEFAULT_SYS_CLK = 125_000_000
STABLE_OVERCLOCK = 270_000_000
UNDERCLOCK = 270_000_000

# Pico can go up to 270MHz before needing to flash to the eeprom directly.
system_clock = UNDERCLOCK

# if the system clock is not the default, apply the clock speed.
if system_clock !=  DEFAULT_SYS_CLK:
    freq(system_clock)

# print(f'Clock: {freq()/1e6}MHz')

# -----------------------------------------
#               PINOUT
# -----------------------------------------

    """

  _______________________________________________________________________________________  
  |     Variable/Pin     |    Pin    |  Pin  |  Pin  |    Pin    |     Variable/Pin     |
  |       Name/Use       |   Label   |  Num  |  Num  |   Label   |       Name/Use       |
  |                      |           |       |       |           |                      |
  |______________________|___________|_______|_______|___________|_______________ ___ __|
  |                      |   GP0     |   1   |  40   |   VBUS    |    USB 5V Supply     |
  |                      |   GP1     |   2   |  39   |   VSYS    |  Filter/Protect 5V   |
  |      Ground Ref      |   GND     |   3   |  38   |   GND     |      Ground Ref      |
  |                      |   GP2     |   4   |  37   |   3V3_EN  | WPU,SC GND ->3v3 OFF |
  |                      |   GP3     |   5   |  36   |   3V3_OUT | 3.3V out from DC/DC  |
  |                      |   GP4     |   6   |  35   |   ADC_REF |    ADC ref pin       |
  |                      |   GP5     |   7   |  34   |   GP28    |    ADC2 Channel      |
  |      Ground Ref      |   GND     |   8   |  33   |   GND     |    ADC Ground Ref    |
  |                      |   GP6     |   9   |  32   |   GP27    |    ADC1 Channel      |
  |                      |   GP7     |  10   |  31   |   GP26    |    ADC0 Channel      |
  |       UART TX        |   GP8     |  11   |  30   |   RUN     | WPU, SC->GND to RST  |
  |       UART RX        |   GP9     |  12   |  29   |   GP22    |   ADC Muxing Switch  |
  |      Ground Ref      |   GND     |  13   |  28   |   GND     |      Ground Ref      |
  |   CHARGE_ORIENT_1    |   GP10    |  14   |  27   |   GP21    |      Mux CTRL D      |
  |   CHARGE_ORIENT_2    |   GP11    |  15   |  26   |   GP20    |      Mux CTRL C      |
  |   H-BRIDGE IN2       |   GP12    |  16   |  25   |   GP19    |      Mux CTRL B      |
  |   H-BRIDGE IN1       |   GP13    |  17   |  24   |   GP18    |      Mux CTRL A      |
  |    Ground Ref        |   GND     |  18   |  23   |   GND     |      Ground Ref      |
  |  I2C Serial Data     |   GP14    |  19   |  22   |   GP17    |                      |
  |  I2C Serial Clock    |   GP15    |  20   |  21   |   GP16    |                      |
  |______________________|___________|_______|_______|___________|______________________|

"""

# LEDs
# ----------------------------
led_onboard = Pin("LED", Pin.OUT)

# -----------------------------------------
#            I2C Devices
# -----------------------------------------

# TODO In final development use hardware settings to change I2C address.

# i2c_bus =  I2C(1, sda=Pin(14), scl=Pin(15, Pin.OUT), freq=100_000)


# -----------------------------------------
#           ADC
# -----------------------------------------

# See ADC.py

# adc0 = ADC(26) # Connect to GP26, which is channel 0
# adc1 = ADC(27) # Connect to GP27, which is channel 1
# adc2 = ADC(28) # Connect to GP28, which is channel 2
# adc_reading = adc0.read_u16() * VOLT_PER_BIT # read and report the ADC reading

# -----------------------------------------
#           WATCHDOG TIMER
# -----------------------------------------

# enable the WDT with a timeout of 5s (1s is the minimum)
if WATCHDOG_EN:
    wdt = WDT(timeout=5000)
    wdt.feed()

# -----------------------------------------
#           METHODS
# -----------------------------------------


# -----------------------------------------
#           PROCESS 1: IO
# -----------------------------------------

STARTUP = True

if STARTUP is True:
    led_onboard(1)
    time.sleep(1)
    led_onboard.toggle()

if WATCHDOG_EN:
    wdt.feed()

while True:
         
    # -----------------------------------------
    led_onboard.toggle()
    time.sleep_ms(REFRESH_PERIOD)
    gc.collect()
    if WATCHDOG_EN:
        wdt.feed()
    
    




