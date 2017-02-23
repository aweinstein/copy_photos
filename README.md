# copy_photos

Copy photos based on a given directory structure and the photos' date. The program can be used to organize the photos of a given subject (child, pet, etc.).

This program copies a set of photos (JPG files) from a source directory to another destination directory. The destination directory has the structure (names in spanish):

```
destination_dir
|-- anio01
    |-- mes01
    |-- mes02
    |-- ...
    |-- mes12
|-- anio02
    |-- mes01
    |-- mes02
    |-- ...
    |-- mes12
|-- ..
```

The corresponding year and month are computed based on the photos's date, as stated in its EXIF data, and the day of birth (`dob`) of a subject.