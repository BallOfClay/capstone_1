
# Rotten Apple?


## Intro
* In tech hardware, there is a term called Designed (or 'Planned') Obsolescence
    * Designed Obsolescence = Designing Hardware and Software features so that there will be incentive to upgrade to the newest model year of a device
    * Upgrade, Repeat


## The Data
* I found a dataset on Kaggle of 8632 Mobile Devices
    * 108 unique manufactures, from 1994 to June 2017
* The dataset has 40 attribute columns, with many containing imbedded information
* This dataset comes from a Kaggle contributor named Arwin Neil Baichoo
* The scrapper program he used was written in C# and nearly 950 lines of code
* Scraped from a website called GSMArena which tracks release and hardware specifications for personal devices

![](imgs/GSMArena.png)

* Since it was web-scraped, a big challenge for me was cleaning
* Mostly hardware features, so software features like multitasking or video camera were not available

![](imgs/Embedded_Data.png)

## My Hunch
* One of the worst perpetrators of Designed Obsolescence is thought to be Apple 
    * I wanted see if there is data to prove this
* That Apple waits to release features significantly later than competitors
    * If you are able to wait to add more features into a new device, people are incentivized to upgrade
    * In hardware, sales consistency this is important to sustain cash flows

![](imgs/Apple_Article.png)

## Cleaning
* Since the data was web-scraped, there was bound to be some errors. Lots of unique formatting, extraneous words, unqualified NaN's
    *  Paramount was cleaning the dates
        * I found 20 different date formats for the month a device was announced
        
![](imgs/Dates.png)

* Thought it would also be important to extract feature data in a repeatable manor with a Class
    * However using a Class would require fully cleaned dataset

## EDA
* CLEAN, BREAK IT, CLEAN, BREAK IT...
* Find General Trends over time
    * Price Increase?
    * Screen Size Increase?
    * Battery Capacity Increase?
* Number of phone models
* Observe when features first appear and are generally adopted by the market
    * Determine when Apple introduced products
* Explore differences between US, Chinese, Korean and European manufactures

## Analysis
* Infer what general trends mean
    For Example - Average Price of Device

![](imgs/Average_Price.png)

* Make specific note of when Apple first introduced the first iPhone

![](imgs/iPhone_Release_Date.png)

* Conduct tests to determine whether Apple significantly delayes release of available technology

## Future Ambitions
* Implement Arwin's web-scraper Algorithm in C# or Python
    * Practice web-scraping
    * Hopefully make new data CLEANER
* Gather data between 2017-Present
### Has the 'game' changed?  
### Is Apple conducting Designed Obsolescence by removing features first?

