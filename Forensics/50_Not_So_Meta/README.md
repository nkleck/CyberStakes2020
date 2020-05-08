
# Not So Meta

## Challenge
* Category: Forensics
* Points: 50

Look, it's the flag! Oh wait...it looks like we need to take a closer look... not_so_meta.jpg

### Hints
* How do images keep contextual information when they're created? (e.g., GPS data, creation timestamp, etc.)
* How do you encode binary data into common ASCII characters?


## Solution

Install exiftool available [here](https://exiftool.org/)

Or use an online exiftool like [this](http://metapicz.com/#landing)

Installation Instructions:
```
$ wget https://netix.dl.sourceforge.net/project/exiftool/Image-ExifTool-10.61.tar.gz
$ tar xvf Image-ExifTool-10.61.tar.gz
$ cd Image-ExifTool-10.61/

# perl Makefile.PL
# make
# make test
# make install
```
Now run exiftool against the .jgp file

```
$ exiftool not_so_meta.jpg
ExifTool Version Number         : 11.96
File Name                       : not_so_meta.jpg
Directory                       : .
File Size                       : 86 kB
File Modification Date/Time     : 2020:04:25 18:34:39+00:00
File Access Date/Time           : 2020:04:25 18:38:20+00:00
File Inode Change Date/Time     : 2020:04:25 18:38:55+00:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : cm
X Resolution                    : 270
Y Resolution                    : 270
XMP Toolkit                     : Image::ExifTool 10.80
Exif Version                    : 0220
Exif Image Width                : 1903
Exif Image Height               : 2048
Region Applied To Dimensions H  : 2048
Region Applied To Dimensions Unit: pixel
Region Applied To Dimensions W  : 1903
Region Area H                   : 0.4264919941775837
Region Area Unit                : normalized
Region Area W                   : 0.32127192982456143
Region Area X                   : 0.680921052631579
Region Area Y                   : 0.3537117903930131
Region Type                     : Unknown ()
Creator Tool                    : Picasa
Its The Flag                    : QUNJezZhYmI1Y2E0YTM2MzlhZTYxZDMzZDgyOWU1Y30=
Image Width                     : 1903
Image Height                    : 2048
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1903x2048
Megapixels                      : 3.9
```


base64 decode: QUNJezZhYmI1Y2E0YTM2MzlhZTYxZDMzZDgyOWU1Y30=

Use: https://www.rapidtables.com/web/tools/base64-decode.html

**ACI{6abb5ca4a3639ae61d33d829e5c}**
