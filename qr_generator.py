import qrcode

def generate_qr(iccid, smdp_url="http://localhost:5000"):
    data = f"LPA:1${smdp_url}${iccid}"
    qrcode.make(data).save(f"esim_activation_{iccid}.png")

generate_qr("1234567890")
