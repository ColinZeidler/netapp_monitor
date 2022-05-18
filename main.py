from prometheus_client import start_http_server

from nethog_monitor import NethogMonitor

def run():
    monitor = NethogMonitor()
    monitor.run()

if __name__ == "__main__":
    # TODO argparse, handle different ports
    start_http_server(9988)
    try:
        run()
    except KeyboardInterrupt:
        print("Bye")