class eUICC:
    def __init__(self, iccid):
        self.iccid = iccid  # eSIM unique ID
        self.profiles = {}  # Stores carrier profiles

    def install_profile(self, carrier, apn):
        self.profiles[carrier] = {"apn": apn}
        return f"Installed {carrier} profile"

# Test
esim = eUICC("1234567890")
print(esim.install_profile("TestTelco", "internet"))
