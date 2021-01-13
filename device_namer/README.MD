# Meraki Device Namer

### Purpose:
This function performs the role of creating names for devices when a site is created.

### Dependencies:

<br />

##### <b> Application functions </b>

```site_creator()```

```meraki_importer()```

##### <b> Data </b>

```(serials,site_name)```

#### <b> Overview: </b>

Obtains variable data from application. The serials data is a list, and the site_name is a string variable which includes the whole name which the device name will be appended to.

The class will make two API calls. The first API call is a <i>get</i> api call which uses the serial number and then gets back json data. Currently the code has loops that match a criteria based on a particular key and value in the json returned data. Specifically the code is looking for what 'model' is returned. If the model matches, then the loop begins and it iterates over all respective serials.

The loop will create a device name and number depending on the model and number of devices matching that loop. It will do an api call <i>update</i> to the Meraki dashboard matching the respective serial number and update it with it's respective name.

Once this work is done it will then break out to the application to continue next steps.

#### Device Groups:

> Switches = SW

> Access Points = AP

> Security Appliances = MX 

#### Examples:

##### Meraki MX Device

> FF-AU-SITE3-MX1

##### 2x Meraki Switches

> FF-AU-SITE3-SW1
> FF-AU-SER3-SW2

