import subprocess
import atexit

from prometheus_client import Gauge

class NethogMonitor(object):
    def __init__(self, delay=10) -> None:
        self.running = True
        self.delay = delay

        self.in_gauge = Gauge('process_in_rate', 'KBps incoming for process', ['process_name'])
        self.out_gauge = Gauge('process_out_rate', 'KBps outgoing for process', ['process_name'])

    def stop(self):
        self.running = False

    def run(self):
        cmd = ['nethogs', '-t', '-d', str(self.delay)]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

        atexit.register(p.terminate)
        entries = []
        wait_for_start = True

        for line in iter(p.stdout.readline, b''):

            if not self.running:
                break

            # print(line)
            if b"Refreshing" in line:
                if wait_for_start:
                    wait_for_start = False

                for entry in entries:
                    self.in_gauge.labels(entry['process']).set(entry['in_rate'])
                    self.out_gauge.labels(entry['process']).set(entry['out_rate'])

                entries = []
            else:
                if wait_for_start:
                    continue
                data = line.split()
                if len(data) < 3:
                    continue

                entry = {
                    "process": data[0],
                    "in_rate": data[-2],
                    "out_rate": data[-1]
                }

                entries.append(entry)

