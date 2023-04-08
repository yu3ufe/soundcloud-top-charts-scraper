# SoundCloud Top Charts Scraper

## Description
This is a Python script that uses the `requests`, `BeautifulSoup`, and `pandas` libraries to scrape the top charts of the House genre from SoundCloud's website. The script extracts information such as title, singer name, publish date and time, and song link, and stores it in a CSV file.

## Support

If you find this project useful and would like to support its development, you can buy me a coffee by clicking the button below:

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/yu3ufe)

Your support is greatly appreciated!

## Usage
To use this script, you need to have Python 3.x installed on your system. You also need to install the required packages by running the following command:

```
pip install requests beautifulsoup4 pandas
```

Once you have installed the required packages, you can run the script by navigating to the directory where the script is located and running the following command:

```
python soundcloud_top_charts.py
```

This will run the script and save the extracted data to a CSV file named `output.csv` in the same directory.

## Customization
You can modify this script to meet your specific needs by changing the following parameters:

- `url`: The URL of the SoundCloud page that you want to scrape. You can change this to scrape data from a different genre or country.
- `output_file`: The name of the CSV file where the extracted data will be saved. You can change this to save the data to a different file.

You can also modify the code itself to extract different information or perform additional processing on the extracted data.

## Contributions

Contributions are welcome! If you find any bugs or have suggestions for improving the script, please open an issue or submit a pull request.

## Disclaimer
This script is provided for educational purposes only. Make sure to review SoundCloud's terms of service before using this script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
