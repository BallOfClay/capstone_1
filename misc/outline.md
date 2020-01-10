# Basic Info

Original Database: https://www.gsmarena.com/

Data Pipeline Tasks:
* Understand GSMArea C Webscrape
* Convert C Webscrape to Python
* Execute C Webscrape for 2017-Present
* Execute Python Webscrape for 2017-Present
* Parse out network technology
* Parse out each antenna band
* Parse out network speed
* Parse out pixel density and/or screen size
* Parse out CPU speed
* Parse out Wi-Fi Protocols
* Parse out sensors
* Parse out battery capacities

EDA Tasks:
* Attributes: brand	 model	network_technology	2G_bands	3G_bands	4G_bands	network_speed	GPRS	EDGE	announced	status	dimentions	weight_g	weight_oz	SIM	display_type	display_resolution	display_size	OS	CPU	Chipset	GPU	memory_card	internal_memory	RAM	primary_camera	secondary_camera	loud_speaker	audio_jack	WLAN	bluetooth	GPS	NFC	radio	USB	sensors	battery	colors	approx_price_EUR	img_url	
* Numerical Data: 2G_bands  3G_bands    4G_bands    network_speed   dimensions  weight_g    weight_oz   display_resolution  display_size    CPU mememory_card   internal_memory RAM primary_camera  secondary_camera    battery approx_price_EUR
* Additional Data: 5G   SIM_multiple    form_factor keyboard    notch OIS   telephoto   ultrawide   pop-up_camera   dual_speakers   barometer   heart_rate  fingerprint infrared    removable   charging_speed  wireless_charging   popularity

Data Addition Tasks:
* Determine which countries/regions manufacture focuses on
* When each Network/Protocal was adopted
* Which bands available each region and when
* Parse out tablets vs phones (7 in screen or bigger, https://www.cnet.com/news/what-makes-a-tablet-a-tablet-faq/)

Possible Data Products:
* Number of handsets released each year, theme: consolidation
* When phones are released in year
* When new frequency bands are available vs network adoption
* Does CPU performance correlate to Moore's Law (may have to find way to equate speeds and number of transistors)
* Progression of megapixels cameras
* Progression of display size
* Progression of pixels
* Progression of battery capacity vs phone weight

Country of Origin:
* US
* China
* Korea
* Taiwan
* France
* Sweden
* Japan

Target Markets:
* US
* China
* India
* Europe
* Latin America?
* Africa?

Telecom Governing Bodies:
http://summitdata.com/Documents/Regulatory_Domains.pdf
* ITU
* ETSI
* TIA
* FCC
* CE
* TELEC (Japan)
* MKK (Japan)
* KCC (Korea)
* China (MITT?)
* MOC (Israel)
* Singapore
* Taiwan

Network Technologies (Year Released, Samsung Release, Network Generation):
* GSM (1990s, 2G)
* GPRS
* UMTS (Early 2000s, 2003, 3G)
* HSPA (Mid 2000s, 2006, 3G)
* EDGE
* CDMA / EVDO (Late 2000s, 2009, 3G)
* LTE (Early 2010s, 2010, 4G)

Relavent Features:
* Sensors
** Accelerometer
** proximity
** compass
** gyro
** barrometer
** Fingerprint
** Iris Scanner
** heart rate ^
** humidity ^
** UV, UV light
** gesture ^
** tempurature ^
** altimeter ^
** SpO2 ^
* network_technology
* network_speed
* Radio
* GPS
* CPU speed
* NFC
* Screen type
* SIM type
* Display type
* Display size
* Internal Memory size
* RAM size
* Bluetooth level
* WiFi level
* Battery size
* Secondary camera


Things I completed:
* Adjusted shifted data, Lines 821 6060 6663
* Flip attribute names for display size and display resolution
* Adjusted 1 Q to 1Q for one phone


Data Functions:
* Remove additional spaces where dataframe is 41 wide
* Convert weight_g to weight_oz (to remove wi-fi)?
* Find unique values
* Ecumulator
* Value Seperator
* Extract Numerical Value
* Scaling
* Drop Row (no cellular connectivity, insignificant manufactures)
* Company Country of Origin
* Device Target Market
* Is Tablet or Phone (Greater than 7 inches)
* Is Flagship
* Is Budgetary Phone
* Date Announced Conversion
* Classes for each phone?
* Remove no Cellular

Analysis Functions:
* Aggregate per year
* Battery Capacity vs Weight
* Features per Dollar
* Screen growth over time
* Network technology over time
* Year over year trend
* Price over time
* Price per feature
* Uptake Comparison

Data Products:
* Comparing Apple attribute uptake compared to competition
* Screen size growth over time
* Battery capicity over time
* Battery capicity versus weight over time
* Audio Jack Removal


Next Steps:
* Feature Class
** "Is Unique" Function *Maybe outside of class*
** "Is First" Function(population, manufacture=Nan, Model=Nan)
** "Find Average"(sampling bounds, within year, since last iphone, )
** "Find Largest"
** "Is Flagship"
** Plot over time (sampling bounds, excluded brand)

** "Find Weighted Unit" looks for number unit
** "Parse Attribute"

* Date Parser
* Is unique
* Is Tablet
* Country of Manufacturing
* Remove Object Where
* Find Metric Function *Number only* could look for Wi-Fi protocols
* Encode via Number of phones made by manufacture

* Target Market
* Frequency band chart (over time) <if you have time>