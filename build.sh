docker run -v "$(pwd):/src" -e "PLATFORMS=linux" fydeinc/pyinstaller --name netapp_monitor main.py