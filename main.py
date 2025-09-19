import time
from typing import cast

import serial
import yaml


def main() -> None:
    with open("sketch.yaml") as settings_file:
        settings: dict[str, str] = cast("dict[str, str]", yaml.safe_load(settings_file))
    port: str = settings.get("default_port", "/dev/ttyACM0")

    with serial.Serial(port, 115200, timeout=1) as serial_monitor:
        time.sleep(1)

        serial_monitor.reset_input_buffer()

        while True:
            line_bytes = serial_monitor.readline()
            if not line_bytes:
                continue

            line = line_bytes.decode().strip()

            try:
                mouse_part, click_part = line.split("\t")
                _, x_str, y_str = mouse_part.split()
                _, switch_str = click_part.split()

                x = int(x_str)
                y = int(y_str)
                switch = int(switch_str)

                print(f"x={x}, y={y}, switch={switch}")
            except ValueError:
                continue


if __name__ == "__main__":
    main()
