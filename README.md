<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Riverwatch</h3>

  <p align="center">
    A telegraf input plugin for capturing USGS stream data.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]

Riverwatch is a <a href="https://www.influxdata.com/time-series-platform/telegraf/">Telegraf</a> exec input plugin that fetches data for a specified list of stream sites from USGS and inserts it into Telegraf's metric database. From there the data can be exported using any of the available Telegraf output plugins to an appropriate storage and/or graphing application. The example above was created using <a href="https://prometheus.io/">Prometheus</a> and <a href="https://grafana.com/">Grafana</a> to create time series plots of various metrics.

I wrote this plugin to monitor conditions on various rivers in my region for various outdoor sports such as kayaking, fishing, etc, and to monitor the general health of my region's rivers.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This plugin was written under Python 3.11.5 but should work under any stable Python3. Additional module requirements are listed in requirements.txt.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

You will need a working telegraf installation on a host or container with Python3 installed. 

### Installation

Clone the repo to your telegraf host, change into the repo directory and install the necessary Python modules by running `pip install -r requirements.txt`.

The plugin has been pre-populated with a list of monitoring sites in the Carolinas, but you can find your own list of sites by going to the <a href="https://dashboard.waterdata.usgs.gov/app/nwd/en/?region=lower48&aoi=default">USGS National Water Dashboard</a> and browsing the map for sites of interest to you. The site code will be a multi-digit number like "Monitoring location USGS <u>03508050</u>". Add this number to the "sites" dictionary in riverwatch.py.

Add the following to your `telegraf.conf` file:

```
[[inputs.exec]]
commands = ["python3 /path/to/riverwatch/repo/riverwatch.py"]
timeout = "15s"
name_suffix = "_riverwatch"
data_format = "influx"
```

Restart telegraf and after a couple minutes you should see the _riverwatch metrics showing up in whatever telegraf output endpoints you have configured. In my example using the prometheus_output_plugin the endpoint at :9273/metrics looks like this:

```
# HELP temperature_riverwatch_value Telegraf collected metric
# TYPE temperature_riverwatch_value untyped
temperature_riverwatch_value{host="rome",siteID="02176930",siteName="Chattooga River At Burrells Ford Nr Pine Mtn"} 2.3
temperature_riverwatch_value{host="rome",siteID="03441000",siteName="Davidson River Near Brevard"} 1.9
temperature_riverwatch_value{host="rome",siteID="03451500",siteName="French Broad River At Asheville"} 2.6
temperature_riverwatch_value{host="rome",siteID="03456991",siteName="Pigeon River Near Canton"} 2.2
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
