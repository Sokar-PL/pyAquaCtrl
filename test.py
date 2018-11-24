#import smbus2 as smbus
from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD('PCF8574', 0x3f, cols=16, rows=2, auto_linebreaks=False)
#lcd.cursor_mode()
lcd.home()
lcd.write_string("22:03:22  NOC\r\n23/11/18 A 100%")

for s in range(60):
#    msg="22:03:{}".format(s)
    lcd.home()
#    print(lcd._get_cursor_pos())
#    lcd.home()
    lcd._set_cursor_pos((0, 6))
    lcd.write_string("{} ".format(s))
#    for __ in range(10):
#        sleep(0.5)
#        lcd.shift_display(-1)
#    input("next?")
    sleep(0.2)
#    lcd.write_string("1234567890123456\r\n1234567890123456")
#    sleep(0.1)
#    lcd.clear()
