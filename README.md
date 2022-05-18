# About

I wanted a way to monitor what process was sending and receiving data on my server in my Grafana dashboard. Since I already had a PrometheusDB setup it made sense to add a new scraping target.

# Build

Uses the fydeinc/pyinstaller docker image to build the project into a single file executable that can run on most linux installs

```
docker pull fydeinc/pyinstaller
./build.sh
```

The compiled executable will be located in `./dist/linux/` as `netapp_monitor`

# Run

Run the built executable with `./netapp_monitor`

You can run the script in the background with:

```
sudo ./netapp_monitor &
disown
```
