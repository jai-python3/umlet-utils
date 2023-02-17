# umlet-utils

Software for generating Umlet class diagrams of a Python code base

Reference: https://www.umlet.com/

## Set-up Python virtual environment

```shell
cd ~/umlet-utils
virtualenv -p python3.8 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Enable the umlet-util aliases

Add the following line to your .bashrc

```
echo "source ${HOME}/umlet-utils/aliases.txt" >> ${HOME}/.bashrc
```

Execute the following to enable the umlet-utils

```
source ${HOME}/.bashrc
```

## Execution

Invocation via the Python script

```shell
source ${HOME}/umlet-utils/venv/bin/activate
python ${HOME}/umlet-utils/src/python_api_to_umlet.py
```

Invocation via the wrapper shell script

```shell
bash ${HOME}/umlet-utils/src/python_api_to_umlet.sh
```

Invocation via the  alias


This will execute umlet-utils/src/python_api_to_umlet.py on the current directory:

```shell
uuu
```

Specify an input directory other than the current like this:


```shell
uuu --indir [some directory with Python code base containing some classes]
```

## Contact

Jaideep Sundaram
