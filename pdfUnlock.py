from sys import argv
import pikepdf

def remove_password_from_pdf(filename, password=None):
    pdf = pikepdf.open(filename, password=password)
    save=filename.split('.')[0]+'-unlock.pdf'
    pdf.save(save)

if __name__ == "__main__":
    filename = argv[1]
    print('File:',filename)
    password=input('Password: ')
    remove_password_from_pdf(filename=filename,password=password)
