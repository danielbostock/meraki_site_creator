
# Meraki Site Creator

> The streamlined & consistent way to deploy Meraki Networks

## Table of Contents (Optional)

- [Requirements](#requirements)
- [Features](#features)
- [Installation](#installation)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

---

## Purpose

The reason for starting to make an application like this is because I really am a big fan of consistency in network configuration. When managing a large number of sites with a small team with a small team it is important that configuration is consistent. Meraki templates are a way of delivering this consistency without great complexity. I envisaged a time within the organisation I work at that even in templates there will eventually become inconsistencies or rather the application of the templates to the correct sites.

To overcome this challenge I therefore started looking at the Meraki APIs in how I could use Python to consistently create sites for my organisation. With all this in mind, the overall purpose of this application is to provide a framework for the assignment of templates and naming conventions.
## Requirements

In order to get started you will need to have already built your own Meraki configuration templates. If you are not familiar with Meraki templates and how they work, click on the link below to understand how you can start leveraging them today.

Meraki Configuration Templates Overview - https://documentation.meraki.com/General_Administration/Templates_and_Config_Sync/Managing_Multiple_Networks_with_Configuration_Templates

Meraki Configuration Templates Best Practices - https://documentation.meraki.com/Architectures_and_Best_Practices/Cisco_Meraki_Best_Practice_Design/Best_Practice_Design_-_MX_Security_and_SD-WAN/MX_Templates_Best_Practices

## Project Status

<b>Release Status: Alpha Release</b>

> Currently the release is in Alpha stage, there is very little to no error checking, the entire application is not completely dynamic. Review the Coming Features section to see what features are planned for the next release.

## Features

### Consitent Site SD WAN Provisioning Process

The application will provide a consistent framework for deploying a new site. This will be done by binding a sites network to an existing agreed template for the respective brands site as per configuration of brands and their respective templates.

### Consistent Naming Conventions

This applicaiton will prevent the whole issue naming conventions, the naming convention will be assigned via the choices the user makes and the devices will be labelled accordingly.

### IP Addressing

This application will make use of Meraki templating feature along with handling IP address allocation so much so that the user and whole of IT team now don't have to wonder or worry what IP address is assigned to what site. This application aims to remove the need to know this information and even record it so it can be referenced at any time. Finally the application will ensure that DNS entries are added and other relevant monitoring or management is also added/updated.

## Usage

In order to get started with using the application, all you will need to do is start with running the Python file - main.py

## Steps
#### Brands Assignment
1. Navigate to config/site_data/brands.csv
2. Change the 'Brand' column with your respective brand or brands and 'BrandCode' with your own shortened/abbreviated Brand Code. *NOTE* If you have a brand in multiple countries only Brand3 will deal with multiple countries at this time. This will be changed in the next feature release.
3. Change the 'Country' column to match your brands respective countries, change 'CountryCode' as well, I recommend using either the two char or three char naming convention which is outlined and listed in the following ISO - https://www.iso.org/iso-3166-country-codes.html
4. (OPTIONAL) Classes are not currently implemented, but in preparation for this release, you can put your brands in one of 3 types or all types. If you don't use classes or know how you want to classify your sites as of yet, leave this blank. This feature will be an optional one in the future as well as it is not broadly applicable.

### Static Variables
> Unfortunately due to the early stage of development there are some hardcoded variables that will eventually be pulled dynamically, but for now you will have to edit the code slightly to enable it to work in your enviornment. This is on the feature list for the next release.

##### menu Static Variables
   1. > function country_selector()
      1. Within the menu.py file you will need to modify at this time the following line.
      2. ```menu.py line 19: country_selection = int(input((brand) + ' is in the following countries.\n1. COUNTRY1 \n2. COUNTRY 2\n3. COUNTRY3\n4. COUNTRY4\n' + (COUNTRY)))```
      3. Currently this only works when option 3 is selected, so if you have a brand available in multiple countries, put the countries in step 2. *NOTE* Currently only supports two 4 countries, the number potential will be dynamic in next release.
      4. > country_selector.country_selection
         1. lines 21, 24, 27, 30
         2. ```country = 'C1'``` - Modify the various country codes to whatever you want as per the lines indicated above.

##### meraki_importer Static Variables
   1. > function device_importer()
      1. api_key - This variable references whatever your environment variable for your Meraki API. Modify line 13 - ```('meraki_api_key')``` if you have created a unique variable.
      2. org_id - This variable is unique to whichever organisation you are using in your Meraki dashboard. Refer to Meraki API documentation on how to retrieve this.

##### site_creator Static Variables
   1. > class orgNetwork()
      1. constructor
         1. timeZone: This variable is not required but will default to LA time if you don't configure it. Uncomment and add your timezone in here to have it applied to the network.
         2. tags: You can use your own tags for multiple reasons here if so desired but not mandatory
         3. productTypes: 1 or more are required, when entering more than one, Meraki will convert to a combined network, there is no string entry for combined presently.
         4. meraki_api_key: As described elsewhere this is done in your installation phase of the Meraki SDK and initial configuration as outlined by Meraki SDK documentation.
---



## Installation

- Python3
- Python Modules: Meraki SDK

> Meraki SDK Documentation - https://developer.cisco.com/meraki/

### Setup

- Python Modules Setup

> Install Meraki SDK & Requests Module


>> Windows - Pip3


```powershell
PS > pip3 install meraki
```


>> Linux/MacOS
```bash
$ pip3 install meraki
```


#### Meraki SDK Setup (OPTIONAL)

Meraki SDK is a super handy and makes working with the Meraki API in Python much easier. I have leveraged it in this application rather than using native requests module which the SDK is doing under the hood. However there are some caveats at this time with the Meraki SDK which I encourage you to spend a moment configuring. 

Not configuring these steps will not prevent you from using the application.

 1. Navigate to the Python modules folder and then find the Meraki module folder. This location should be the following.


    Windows

    ```Windows
    C:\Users\your.username\AppData\Local\Programs\Python\Python38\Lib\site-packages\meraki
    ```
    ### Linux Distributions
    #### Arch

    ```bash
    /home/your.username/.local/lib/python3.x/site-packages/meraki
    ```
    #### Debian
    ```bash
    Debian - TBC
    ```
    #### RHEL
    ```bash
    RHEL - TBC
    ```

    #### MacOS

    ```MacOS
    /usr/local/lib/python<ver>/site-packages/meraki
    ```



 2. Modify the configurations file by opening the config.py file
 3. *Optional* - Meraki API logs all requests, which is helpful but also will make the repo folder git too big, so you want to put these logs into a log folder and then gitignore the whole folder or you can put in a completely different folder on your computer.
 4. Add log folder to your .gitignore file

    ```Python
    #Path to output log; by default, working directory of script if not specified
    LOG_PATH = 'path\to\folder\meraki_site_creator\folder\meraki_api'
    ```
---

## Contributing

> I firmly believe in the power of the open source community and sharing my code that maybe taken further and to heights which I am not even aware at the moment. Also I appreciate feedback on writing code better. So if you feel that you can contribute either by adding code to do more or know what can be changed to make it work better plaese feel free to start by letting me know and we can go from there. The best ways to contact me are listed below in the Support section.

---

## FAQ

- *Features Missing*
    - Yes features are missing! There is a lot of development still to do including this README!

---

## Support

Reach out to me at one of the following places!

- My website - danielbostock.com
- Email - danielbotock@outlook.com
- GitHub - Discussions or Issues

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**