import os

from licensing.models import *
from licensing.methods import Key, Helpers

rsa_pub_key = "<RSAKeyValue></RSAKeyValue>"
token = "WyIy...4iXQ=="
product_id = 15899


def authenticate_user():
    if os.path.isfile("licensefile.skm"):
        with open("licensefile.skm", "r") as f:
            license_key = LicenseKey.load_from_string(rsa_pub_key, f.read())
        if license_key is not None and Helpers.IsOnRightMachine(license_key, v=2):
            return True
    return False


def activate_user():
    key = input()
    result = Key.activate(
        token=token,
        rsa_pub_key=rsa_pub_key,
        product_id=product_id,
        key=key,
        machine_code=Helpers.GetMachineCode(v=2),
    )
    if result[0] is None or not Helpers.IsOnRightMachine(result[0], v=2):
        return False
    with open("licensefile.skm", "w") as f:
        f.write(result[0].save_as_string())
    return True
