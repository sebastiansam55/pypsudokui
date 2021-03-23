# pypsudokui

Basic python script to try and find if a valid sudoku exists within the digits of pi.

I have checked about 30 megabytes of data with no results. But have run into scaling problems when attempting to check larger amounts of digits.


I have been rearranging my storage space to make room to download a significant amount of digits but figured I would share
the script in case anyone else had a wack ton of extra hard drive space/compute power burning a hole in your pocket.

## Downloading the digits
You can use either the script I have provided here or any other method. Right now the `main.py` file is expecting the digits to be in json format, if you want to change that to
a file that is just one line of the digits all you have to do is comment/uncomment the marked lines in the `main.py` file. (line 80)

In order to download the bulk digits directly you have to use the `gsutil` tool. To install this on ubuntu systems; `sudo snap install google-cloud-sdk --classic`. 
The tool does not appear to be in the apt repositories.

`gsutil cp "gs://pi50t/Pi - Dec - Chudnovsky/Pi - Dec - Chudnovsky - 0.ycd" ./pi.ycd`

The above command will copy the digits to a file in your local directory named `pi.ycd`.

This is a **300+GB file**. Thankfully it appears that you don't have to have the entire file downloaded in order to decompress it.

The ycd file extension is some kind of special format used by the y-cruncher tool which you will also need to download.

### y cruncher
This tool is not super user friendly but as far as I can tell is the only way to extract the digits we are trying to get at.

You can download the appropriate version [here](http://www.numberworld.org/y-cruncher/#Download).

In order to extract the digits;

- `./y-cruncher`
- Select `5` for digit viewer.
- Enter the path of the `pi.ycd` file.
- Select `2` for Extract digits into a `.txt` file
- Select `1` for the first digit.
- For the "Ending Digit"
    - Select `-1` to dump all
    - Select whatever other value
- Select the path you want the `.txt` file to be created.

Your mileage may vary, it's a spotty tool. I can sometimes view but not dump to txt file. There also doesn't appear to be any type of arguments on the command line meaning
that you have to enter all of the options over and over again when the program is having issues.


