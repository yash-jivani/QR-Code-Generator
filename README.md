# Generate QR codes.

## What is a QR Code?
A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols)

## Installation

For a standard install (which will include pillow for generating images), run:


```bash
pip install qrcode[pil]
```

## Usage
For more control, use the QRCode class. For example:

```python
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
```
# qrcode - Functions
The <version> parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix). Set to <None> and use the <fit> parameter when making the code to determine this automatically.

<fill_color> and <back_color> can change the background and the painting color of the QR, when using the default image factory. Both parameters accept RGB color tuples.


The <box_size> parameter controls how many pixels each “box” of the QR code is.

The <border> parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).
