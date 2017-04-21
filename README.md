# WebScanner
a  scanner to detect  file and directory  in a website


[![CRAN](https://img.shields.io/cran/l/devtools.svg)]()



## install

#### install python
```
sudo apt-get install python
sudo apt-get install python-pip
```
#### clone the repository
``` bash
git clone https://github.com/sarleon/WebScanner.git

```
#### install requirements
``` bash
pip install -r requirements.txt

```


## USE

simply use 
```
python WebScanner.py -u http://127.0.0.1/  
```

404 page will not be echo , if you want to print all the information,use -v like

```
python WebScanner.py -u http://127.0.0.1/ -v  
```
