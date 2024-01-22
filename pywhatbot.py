import log
import time
import webbrowser as web
import pyautogui as pg
import core as c

pg.FAILSAFE = False


class PyWhatBot:
    def __init__(self, wait_time, delay):
        self.wait_time = wait_time
        self.delay = delay

    def send_message_to_numbers(self, names, phone_nos, message_list):
        """Send message list separately to all numbers"""
        new = True
        for name, phone_no in zip(names, phone_nos):
            self.safe_send_messages(name, phone_no, message_list, new)
            new = False

    def safe_send_messages(self, name, phone_no, message_list, new):
        try:
            self.send_messages(name, phone_no, message_list, new)
        except Exception as e:
            print(f"Skipped {phone_no} because of the following error:\n{e}")

    def send_messages(self, name, phone_no, message_list, new):
        """Send WhatsApp Messages to Phone Number"""

        phone_no = str(phone_no).replace(" ", "")
        web.open(f"https://web.whatsapp.com/send?phone=+{phone_no}", new=int(new))
        time.sleep(self.wait_time)
        # pg.click(c.WIDTH / 2, c.HEIGHT / 2)
        for message in message_list:
            if len(message) == 1:
                [msg] = message
                msg = msg.replace("[NAME]", str(name))
                c.type_message(msg)
                pg.press("enter")
                log.log_message(_time=time.localtime(), receiver=phone_no, message=msg)
            elif len(message) == 2:
                [img_path, caption] = message
                caption = caption.replace("[NAME]", str(name))
                c.type_message(caption)
                c.copy_paste_image(img_path)
                c.click_send()
                log.log_image(
                    _time=time.localtime(),
                    path=img_path,
                    receiver=phone_no,
                    caption=caption,
                )
            time.sleep(self.delay)
        c.close_tab()
