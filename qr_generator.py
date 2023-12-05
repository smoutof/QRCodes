import os
import qrcode, qrcode.image.svg

path = "qr_codes"

if not os.path.exists(path):
   os.makedirs(path)

def clean():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

def make_png(path, filename, format):
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'{path}/{filename}.{format}')

    print(f'Saved to {path} as {filename}.{format}!')

def make_svg(path, filename, format):
    qr = qrcode.QRCode(image_factory=qrcode.image.svg.SvgPathImage)
    qr.add_data(data)
    qr.make(fit=True)

    svg = qr.make_image()
    svg.save(f'{path}/{filename}.{format}')

    print(f'Saved to {path} as {filename}.{format}!')

while True:
    filename = input("Filename: ")
    format = input("Format as png, svg or both? ")
    
    if format.lower() == "png" or format.lower() == "svg" or format.lower() == "both":
        pass
    else:
        print("ERROR: Not a valid format!\n")
        continue

    data = input("Enter the url: ")

    print("")
    if format.lower() == "png":
        make_png(path, filename, format)

    elif format.lower() == "svg":
        make_svg(path, filename, format)

    elif format.lower() == "both":
        make_png(path, filename, "png")
        make_svg(path, filename, "svg")

    else:
        print("ERROR: Not a valid format!\n")
        
    print("")
    input("Continue(Enter) or Close(CTRL+C)")
    clean()