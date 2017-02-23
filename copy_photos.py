import os
import shutil
from PIL import Image
import arrow

def get_date(file_name):
    """Get picture date from EXIF data."""
    im = Image.open(file_name)
    date_time = im._getexif()[306]
    date = date_time.split()[0]
    return arrow.get(date)

def get_year_month(dob, pic_date):
    """Compute the year and month given the day of birth and picture's date."""
    year = pic_date.year - dob.year
    year -= ((pic_date.month, pic_date.day) < (dob.month, dob.day))
    year += 1 # We consider the period of the first year
    month = ((pic_date.month - dob.month) % 12) + 1
    return (year, month)


if __name__ == '__main__':

    dob = arrow.get('2015-06-11')
    base_dir = '/path/to/destination/photos/'
    source_dir = '/path/to/source_dir'

    for fn in os.listdir(source_dir):
        if not fn.lower().endswith('.jpg'):
            continue
        pic_date = get_date(os.path.join(source_dir, fn))
        year, month = get_year_month(dob, pic_date)
        year_dir = 'anio_{:02}'.format(year)
        month_dir = 'mes{:02}'.format(month)
        dest_dir = os.path.join(base_dir, year_dir, month_dir)
        os.makedirs(dest_dir, exist_ok=True)
        source = os.path.join(source_dir, fn)
        if os.path.exists(os.path.join(dest_dir, fn)):
            print('{} already exists. Skipping this file'.format(fn))
        else:
            print('Copying {} to {}'.format(source, dest_dir))
            shutil.copy2(source, dest_dir)
