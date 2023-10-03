import time
import os
import multiprocessing
from selenium import webdriver


def capture_screenshot(url, save_path):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    driver.save_screenshot(save_path)
    driver.quit()


def capture_process(url, interval, num_screenshots, output_directory):
    try:
        os.makedirs(output_directory, exist_ok=True)

        url_hash = hash(url)  # Create a hash of the URL for unique output directory
        timestamp = time.strftime("%Y%m%d%H%M%S")  # Generate a timestamp
        unique_output_directory = os.path.join(output_directory, f"{url_hash}_{timestamp}")
        os.makedirs(unique_output_directory, exist_ok=True)

        for i in range(num_screenshots):
            screenshot_path = os.path.join(unique_output_directory, f"screenshot_{i + 1}.png")
            capture_screenshot(url, screenshot_path)
            print(f"Captured screenshot {i + 1}/{num_screenshots}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Screenshot capture interrupted.")


def main():
    urls = []
    num_screenshots = int(input("Enter the number of screenshots to capture: "))
    interval = int(input("Enter the time interval in seconds: "))
    output_directory = "screenshots82223e/"

    for _ in range(5):
        url = input("Enter the URL of the webpage: ")
        urls.append(url)

    processes = []

    for url in urls:
        process = multiprocessing.Process(target=capture_process,
                                          args=(url, interval, num_screenshots, output_directory))
        processes.append(process)
        process.start()

    try:
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print("Screenshot capture interrupted.")
        for process in processes:
            process.terminate()


if __name__ == "__main__":
    main()
