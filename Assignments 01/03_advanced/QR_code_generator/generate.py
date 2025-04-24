import qrcode
from PIL import Image

def generate_qr_code(data, color, size, file_path):
    """
    Generates a QR code with the specified data, color, and size, then saves it to a file path.

    :param data: The data/content for the QR code (e.g., a URL).
    :param color: The color of the QR code in hexadecimal (e.g., "#000000" for black).
    :param size: The size of the QR code (width and height).
    :param file_path: Path where the QR code image will be saved.
    """
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # The size of each box in the QR code grid
        border=4,     # The thickness of the border
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image with the color provided by the user
    img = qr.make_image(fill=color, back_color="white")

    # Resize the image to the specified size
    img = img.resize((size, size))

    # Save the image to the specified path
    img.save(file_path)
    print(f"QR Code saved at {file_path}")

def main():
    # Ask for user inputs
    data = input("Enter the data for the QR code (e.g., a URL): ")
    color = input("Enter the color for the QR code in hex format (e.g., '#000000' for black): ")
    size = int(input("Enter the size of the QR code (e.g., 300): "))

    # File path where the QR code will be saved
    file_path = r"D:\code\python\sirziaassignments\Assignment-4\Assignments 01\03_advanced\QR_code_generator\qr_code.png"

    # Generate and save the QR code
    generate_qr_code(data, color, size, file_path)

if __name__ == "__main__":
    main()
