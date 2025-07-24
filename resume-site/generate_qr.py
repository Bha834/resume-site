import qrcode
from PIL import Image

# जब आप GitHub Pages पर host कर लेंगे, इस link को actual page से replace करें
# data = "https://your-username.github.io/resume-site/"
data = "https://github.com/Bha834/resume-site/raw/main/resume-site/Bhavesh_Patidar_resume3.pdf"

qr = qrcode.QRCode(
    version=2,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("resume_qr.png")
Image.open("resume_qr.png").show()




