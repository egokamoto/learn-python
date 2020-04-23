# Instalando o Python

## Docker 

```docker
docker run --rm -it python:3.9-rc-alpine3.10 /bin/sh
```
or
```docker
docker run --rm -it python /bin/bash
```
```bash
echo "alias py='python3.8'" >> ~/.bashrc
source ~/.bashrc
```

## Ubuntu

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
# interactive... press [enter]
sudo apt install python3.8
# test
python3.8 --version

echo "alias py='python3.8'" >> ~/.bashrc
source ~/.bashrc
```

## Windows
Caso ainda não esteja habilitado, será necessário executar:

```powershell
Set-ExecutionPolicy Unrestricted
```

Instalar

```powershell
Invoke-WebRequest "https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe" -OutFile ~/downloads/python-installer.exe
iex("~\Downloads\python-installer.exe /passive")
```

Desinstalar

```powershell
#Invoke-WebRequest "https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe" -OutFile ~/downloads/
iex("~\Downloads\python-installer.exe /uninstall /passive")
```