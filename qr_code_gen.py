import qrcode

#I created a class named MyQR to simplify the process of creating qr_code_gen.

class MyQR:
    def __init__(self, size: int, padding: int ):
        self.qr = qrcode.QRCode(box_size = size, border = padding,)


# A function that asks for a link
    def create_qr(self, file_name: str,fg: str, bg: str):
        user_input: str = input('Add your link here: ')


        try:
            self.qr.add_data(user_input)

            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f'Image saved successfully! ({file_name})')
        except Exception as e:
            print(f' Error: {e}' )

#Main function of qr_code_gen

def main():
    myqr = MyQR(size=6, padding=2)
    myqr.create_qr('qr_image.png',
                 fg = 'black',
                 bg = 'white')


if __name__ == '__main__':
    main()
