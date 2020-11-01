# CE186_cyber_physical_systems

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# **Smart Air Bears**

_empowered personal pollution monitoring_

_for all_

**Smart Air Bears**

CE 186 Fall 2017 Final Project

Team Members: Garima Raheja, Matt Choi, John Stuart, Brian Tam

**ABSTRACT** Smart Air Bears is a low-cost, high-quality air quality monitoring system which connects to a web app to provide granular measurements of heterogeneous air quality, and also provides personalized health recommendations for a diverse user community. Smart Air Bears is unique in the following ways: i) it is affordable, pricing at $59, while most personal air quality sensors cost upwards of $200, ii) it is personal, sensing air quality around a user, becoming more useful than government-monitored air quality maps of large regions that do not capture heterogeneity in a user&#39;s personal environment, iii) it is helpful, providing not only air quality data but also scientific information-backed contextualization and personalized health recommendations. While the primary goal of this product is the improvement of health and environmental awareness among users, a &quot;back-of-the-envelope&quot; estimate indicates large economic benefits as well. In the United States alone, this product could help users reduce the estimated $46 billion/year in lost GDP caused by air pollution, with potential gains reaching even higher in other nations such as China, which loses up to $280 billion/year due to air quality related healthcare costs, reduced agricultural yield, and lost worker productivity (OECD, 2016).

**MOTIVATION AND BACKGROUND** 1 billion people suffer from respiratory illnesses aggravated by contaminated air. 85% of the world&#39;s population lives in areas that do not meet WHO Air Quality guidelines. 1 in 8 global deaths are attributed to poor air quality.

Impacts of poor air can be felt even by those in the Bay Area -- consider the air Bay Area residents experienced during the days of the Napa wildfire in October. Poor air quality most severely impacts those already hit hard by society, including homeless folks for whom the lines between indoors and outdoors are blurred, and also those whose professions mandate manual labor in outdoor conditions. The air impacts us all, and for many, it is a highly personal issue.

We are motivated by the environmental justice and societal scale problem of air quality, and hope to create a product to aid communities most in need. In response to this epidemic, our team of civil and environmental engineers sought to bring our unique set of skills to bear on finding a solution. With backgrounds in climate modeling, building science, hardware development, and civil infrastructure as well as past experience with NASA, CBE (Center for the Built Environment), and BAAQMD (Bay Area Air Quality Management District), we began to apply our expertise to our proposed solution, Smart Air Bears.

![](RackMultipart20201101-4-zw7kqh_html_731fbbf5358de3a4.gif)

Figure 1 - 2060 Projected reductions

in GDP due to poor air quality

**RELEVANT LITERATURE** Delving deeper into the root of the issue, another motivation for the development of this product was the general neglect of health -- and more specifically air quality -- in current building design practices as well as the lack of access to air quality information among the general public. As the developing world continues its rapid industrialization, the economic impact of air quality is expected to dramatically increase, ballooning to 1% of global GDP ($2.6 Trillion) by 2060 as a result of sick days, medical bills, and reduced agricultural output according to OECD and causing 6 to 9 million premature deaths per year by then (OECD, 2016). Poor air quality is currently responsible for as much as 3 million deaths per year as of 2010, meaning this number is expected to double or triple over the next half century while world population is only expected to grow by 40% over that timespan. Rapid urbanization is largely to blame for this since currently 96% of people in large cities are exposed to pollutant levels that are above recommended air pollution limits (Kumar et al., 2015). ![](RackMultipart20201101-4-zw7kqh_html_fc5d819f2cd84476.png)

![](RackMultipart20201101-4-zw7kqh_html_e5aeac6f30cc196.png)

Figure 2 - 2060 Projected deaths
 per million population

 ![](RackMultipart20201101-4-zw7kqh_html_731fbbf5358de3a4.gif)

Even in the US, there there is limited public understanding about air quality. The Air Quality Index for example, is an oversimplification that aggregates all criteria pollutants and reports a single number of low specificity and low geographic granularity, which is itself a problem. However, while the EPA does at least regulate and report on outdoor air quality, it does not monitor or regulate indoor air quality at all (US EPA, 2017). Because of this, most air quality requirements in the building codes are based only on design intent industry standards, rather than performance based measurements. These standards place limits on ambient pollutants such as PM, Ozone, and NOx as well as indoor-specific pollutants such as CO, VOCs, excessive CO2, bioaerosols, and also extremely high or low relative humidity (Dales et al., 2008) due to its links to allergen growth, disease transmission, and ozone production (Arundel et al., 1986). Since Americans spend more than 90% of their lifetime indoors on average, this makes the quality of indoor spaces of paramount importance because that is where most pollutant exposure occurs (US EPA, 2009).

![](RackMultipart20201101-4-zw7kqh_html_bb0f223ce0ca582f.gif)

Figure 3 - Commonly used ASHRAE
 maximum recommended limits

In response, extensive academic and industry research has been conducted on the topics of indoor air quality monitoring. One meta-analysis of K-12 school IAQ investigations found that a great number of studies indicate widespread air quality problems in U.S. schools. This included extensive documentation of CO2, PM, and mold issues (Daisey et al., 2003). The same study also found found that on average, schools with hard flooring showed 42% fewer instances of allergy and asthma symptoms than schools with carpeting, showing that simple changes in lifestyle and home furnishings can have dramatic impacts on health. ![](RackMultipart20201101-4-zw7kqh_html_8d2e839124a722b4.png)

One pollutant class that received little attention though was VOCs, likely due to low public awareness and the cost associated with measurements for such studies. There are a wide variety of VOCs present in our everyday environment and there is still a long way to go before they are significantly reduced in building products and everyday consumer goods. A study conducted on the prevalence of such compounds showed which products are most likely to contain and off-gass them as well as their expected health effects (Mølhave, 1982). Of these products, most are still abundant in our lives to this day.

Others have found that air quality in the workplace can have significant productivity and happiness impacts. In one study on ventilation rates in offices, researchers observed statistically significant increases in productivity of at least 1.7% among tested office workers when varying ventilation rate between 5, 15, and 30 cfm as well as much more significant increases in reported occupant comfort (Wargocki et al., 2000). While this may seem like a small increase, for such productivity and thermal comfort studies, these effect sizes can be expected due to the large number of factors affecting an occupant&#39;s productivity and perception of their environment.

Many pollutants though can affect health and comfort without us even realizing it. Researchers conducting an air quality survey of european office buildings concluded that unlike many other IEQ phenomena, surveys usually yield positive results while measurement reveals unhealthy air and failure to meet IAQ standards, making measurement more effective than surveys for IAQ measurement and improvement. CO for example cannot be detected at all by humans but is deadly at even small concentrations. Thus measurement plays a key role in design for and regulation of air quality (Bluyssen, 1996).

Typically government agencies are responsible for monitoring air quality on a regional scale. However, conventional approaches to air quality monitoring are based on networks of static and sparse measurement stations. These are prohibitively expensive when trying to capture tempo-spatial heterogeneity and identify pollution hotspots, which is required for the development of robust real-time strategies for exposure control (Kumar et al., 2015). To address the public health and life safety issue of air quality, a rapidly deployable, easily adopted, granular system would be required. Thus, many in academia are working on solving the technical issues of making these sensors more available to the masses (Yu et al., 2013).

However, in our initial assessment of existing IAQ monitoring technologies, we found that all commercially available systems tended to cost hundreds of dollars or more (Lewis, Edwards, 2016), with more utilitarian models being unfriendly to users and more geared towards the scientific community (Kumar et al., 2015) or for professional use such as HVAC commissioning, IAQ complaint investigation, and building management (Vuetilovoni, 2015). Home IAQ monitors on the other hand are marketed more as luxury goods and are isolated from the outside world, providing information only to the user and keeping air quality data cloistered in the hands of very few as more of a novelty than a tool for widespread change.

With a cloud based system that aggregates data though, you would be able to do analysis on the whole data set, map hotspots for air quality, and allow users to anonymously rank themselves among their neighbors. This has been shown to be the most effective way of motivating people to change their energy habits and could easily be applied to improving air quality if given the correct tools and advice (Laskey, Kavazovic, 2011). Existing commercial products also neglect to include comprehensive information on how to actually improve your air quality. The efficacy of different strategies could thus be tracked on a cloud based system from other units and used to make recommendations to newer units. Acting as a network, this could make personal air quality monitors smarter for their users and for society.

**FOCUS OF THIS STUDY** We created an air quality tool with these key focuses: i) the tool should be affordable, especially since it seeks to aid communities with low socioeconomic status, ii) the tool should be personal, more so than the government monitoring of regional air quality, and iii) the tool should provide personal recommendations and contextualization of air quality data. The system architecture of this tool is detailed below in Figure 4.

**CPS SCHEMATIC**

![](RackMultipart20201101-4-zw7kqh_html_c2a0429cb1c79c1f.png)

Figure 4 - Cyber-Physical Integration

 ![](RackMultipart20201101-4-zw7kqh_html_731fbbf5358de3a4.gif)

**BILL OF MATERIALS**

| **Item Name** | **Description** | **Price Per Item** | **Quantity** | **Total Cost** | **Supplier** |
| --- | --- | --- | --- | --- | --- |
| **Arduino Uno** **(or less expensive microcontroller such as STM32 Discovery for mass large scale production)** | Microcontroller | ($9.88) | 1 | $00.00 | CE186 |
| **SparkFun HIH6130** **(DHT11 RH sensor may be used to reduce cost in the future)** | Digital Humidity Temperature Sensor | ($2.00) | 4 | $07.99 | Geeetech |
| **SparkFun Air Quality Breakout CCS811** | VOCs, CO2, MOX Sensor | $19.95 | 1 | $19.95 | SparkFun |
| **GP2Y1010AU0F** | PM 2.5 Sensor | $18.99 | 1 | $18.99 | WaveShare |
| **Wall Adapter Power Supply 5V DC 2A** | Arduino Power Supply | $5.95 | 1 | $05.95 | SparkFun |
| **Plywood 1/8&quot;x15&quot;x30&quot;** | Russian Birch Wood | $1.50 | 3 | $04.50 | Jacobs |

**HARDWARE DESCRIPTION** Our prototype contained 3 main multifunctional sensors, with initial plans to include wifi and location data in the future. The sensors in Smart Air Bears include:

![](RackMultipart20201101-4-zw7kqh_html_77d1dc5035dd81c5.png)

The sensor node is comprised of the air quality sensors and Arduino Uno microcontroller secured in a Russian birch plywood box with routered vents to allow sufficient airflow over the sensors. The PM sensor is located atop the box in order to have full exposure to any particle deposition that otherwise could be blocked by the louvered walls of the enclosure.

The encapsulation box is built with the needs of the sensors in mind, and accommodates their tolerances by maintaining temperature and ventilation conditions. Initial designs of the encapsulation box are shown in Figure 5. However, this encapsulation box turned out to be very difficult to laser cut, due to closely packed cutting edges.

![](RackMultipart20201101-4-zw7kqh_html_8623e0e06119b79d.jpg) ![](RackMultipart20201101-4-zw7kqh_html_8623e0e06119b79d.jpg) ![](RackMultipart20201101-4-zw7kqh_html_7a80371c6c8a3eb.jpg)

![](RackMultipart20201101-4-zw7kqh_html_496e2814154e14df.png)

Figure 5 - (Design Iteration #1) Initial Prototypes of Encapsulation Box

 ![](RackMultipart20201101-4-zw7kqh_html_731fbbf5358de3a4.gif)

We decided to create a simpler design that was more reliable in fabrication, and decided to archive the designs in Figure 5 to be included in future models with more exciting, organic designs.. The current prototype is shown below in Figure 6.

![](RackMultipart20201101-4-zw7kqh_html_363c700aa84a7420.png)

Figure 6 - (Design Iteration #2) Final Version of Smart Air Bears Sensor Node

 ![](RackMultipart20201101-4-zw7kqh_html_731fbbf5358de3a4.gif)

**SOFTWARE DESCRIPTION**

**Wallflower.pico-based web platform**

_Wallflower\_pico\_server.py_

Runs the server on a local port and allows for communication between the software modules.

_Index.html_

Defines the overall structure of the wallflower server semantically and sets up the appearance of the web document. The Index.html embeds images, interactive forms such as side tabs and pulldown menus, and other objects to the rendered web page, creating structured documents by outlining structural semantics for text. These include paragraphs, headings, links, lists, etc.

_extend\_dashboard.js_

Makes the Wallflower.pico webpages interactive, adding functionalities to HTML elements created in Index.html. For instance, it collects data in specific objects defined in the webpage and logs the data to the JS console. Additional features includes making HTTP requests from the web server through $.ajax() method, appending contents of HTML files to specific objects in the webpage. The javascript file adds dynamic element to HTML documents that would otherwise remain static.

_table.html_

Outlines a structure for data visualization in the form of data table with rows for each air quality pollutant and columns for measured and interpreted values. It defines a skeleton for the table to which javascript and css files posts data and adds graphical element.

_bootstrap.css and dashboard.css_

Defines the visual style of the web interface.

**Cyber-Physical System**

_IAQListenAndSend.py_

Communicates with arduino to receive data from the air-quality sensors. Creates objects into the webserver and posts the numerical data obtained from the sensors into specific streams within the server.

_IAQListenAndProcess.py_

Aggregates data and uses a flow-chart decision tree approach to come up with personalized health recommendations. Calculates total exposure, relative health risk, saves user data over time, and later uses user input of what their personal histories have proven to see if recommendations worked. This serves as the personal IAQ assistant of the user. User inputs data about the building system that opens and closes the options in the actuation decision tree. While the basic rating system depends on simple industry established cutoff points, branches referencing multiple metrics allow the system to guess what the source of an air quality problem may be, such as indicating the presence of a water intrusion or mold problem if both relative humidity and VOCs are found to be high.

_SendData.ino_

Sends PM, VOC, CO2, humidity, temperature data from SparkFun sensors to Arduino Uno microcontroller through serial communication and uses RH and temperature data to calibrate the VOC sensor, which is dependent upon these quantities.

**ANALYSIS METHODS** Our data analysis uses a combination of built in highcharts regression tools and a simple set of running averages to help users better understand their air quality and the effect they can have on it. From the raw data, IAQListenAndProcess.py categorizes each reading on a scale from &quot;good&quot; to &quot;terrible&quot; (1 - 4) for each measured quantity and outputs the result. It also incorporates that result into a running average in order to report a summary over any time scale to the user. The averages are calculated with each new measurement using the following formula:

Where &#39;x&#39; is any input and &#39;i&#39; is the number of readings made at that point in time. The user is also able to input a desired timeframe they would like to gather data over, and the user-defined averages can be output as well. By default, it outputs daily and hourly averages in addition to the lifetime metrics reported on the results page. While we were not able to successfully visualize this data as a visually pleasing table due to debugging issues and time constraints, it is available to the user as a JSON with with user-friendly key values that clearly explain what each entry in the string represents.

**RESULTS** Using our prototype, we collected data on several spaces throughout campus to to validate our findings and gain insight into the typical air quality experienced by Berkeley students. The following data was collected during dead week in spaces with low occupancy. The results are summarized as follows:

| Location | Average Temperature (C) | Average PM (μg/m^3) | Average CO2 (ppm) | Average RH (%) |
| --- | --- | --- | --- | --- |
| Residential | 22 | 9 | 414 | 33 |
| Unit 1 Basement | 21 | 5 | 456 | 29 |
| Wurster Hall | 21 | 4 | 417 | 29 |
| 5th floor Davis Lab | 22 | 3 | 454 | 22 |
| 3rd floor Davis Lab | 22 | 6 | 578 | 26 |

Figure 7 - Data Collected from Campus Locations

 ![](RackMultipart20201101-4-zw7kqh_html_99b085d067053642.gif)

**VISUALIZATION**  **One of the main roadblocks in the development of our system was our web interface data visualization, which was cut back from our previous goals due to debugging issues in our javascript. With more time, we would expand upon our visualization to display additional tables and bar charts to better present our analysis results and allow users to compare their results to other similar spaces. Some examples of our visualized data are provided below along with our analysis results from a residential setting, imported into our proposed table design.**

![](RackMultipart20201101-4-zw7kqh_html_375ce775342f91db.png)

Figure 8 - PM2.5 (Particulate Matter) Data Visualized on Wallflower.pico

 ![](RackMultipart20201101-4-zw7kqh_html_731fbbf5358de3a4.gif)

![](RackMultipart20201101-4-zw7kqh_html_29613ba554c5f34e.png)

Figure 9 - CO2 (Carbon Dioxide) Data Visualized on Wallflower.pico

 ![](RackMultipart20201101-4-zw7kqh_html_731fbbf5358de3a4.gif)

![](RackMultipart20201101-4-zw7kqh_html_de4cac9238881db4.png)

Figure 10 - Contextualized Data Shown in Table Form, With Raw Data and Translated Analysis (Data → Conditions)

 ![](RackMultipart20201101-4-zw7kqh_html_731fbbf5358de3a4.gif)

Smart Air Bears also seeks to create a mobile application powered by the sensor network. The mobile application has three major components:

1. HEALTH

The mobile application will provide recommendations about health activities, including personalized recommendations based on a user&#39;s medical history. Recommendations range from &quot;great time to go for a run,&quot; &quot;use N95 air mask,&quot; to &quot;consult a doctor.&quot;

1. HOME

The mobile application will provide recommendations about home systems, such as ideas on changing carpets that trap pollutants. The app also connects with smart home devices across the Internet of Things (IoT) to actuate devices (such as air purifiers) and building components (windows, HVAC, fans, etc).

1. CITY

The mobile application aggregates data from sensor nodes around the user to generate a high-density map of air conditions in the area. This map provides users with an idea of the general air quality around them, and empowers users to find locations with safer air conditions.

![](RackMultipart20201101-4-zw7kqh_html_1706d4cb361bf1c1.png)

Figure 11 - Mockup of Smart Air Bears Mobile Application

 ![](RackMultipart20201101-4-zw7kqh_html_731fbbf5358de3a4.gif)

**DISCUSSION** With a simple, scalable, low-cost, user-friendly, cloud-based and personalizable system such as ours, a widespread network of air quality monitoring could be built both for personal use and for societal use. Though all nations could benefit from improvements in air quality, based on the cost and sensitivity of our product, Smart Air Bears is currently best suited for use in &quot;hotspots&quot; of particularly high and variable pollution within the US and for use in developing nations such as China and India. Tackling poor air quality on a broad, but still household by household basis makes it personal to more people and increases interest in solving this societal scale problem by simplifying complex air quality measurements and allowing people to experiment with their air quality and see the effects their actions can make in real time.

Beyond the societal benefits, governments can expect to see economic benefits as well. According to a press release by the World Bank (2016) air quality causes 6 times more premature deaths than malaria, and was responsible for $225 billion globally in premature deaths alone, not including the cost of healthcare, lost productivity due to merely illness, and lost agricultural yield. As the previously cited OECD report states, these numbers are expected to greatly increase as the world industrializes and urbanizes, costing as much as $2.6 trillion due to all those factors by 2060.

If a widespread system of personalized air quality monitors were adopted and users were successful in making lifestyle changes based on their results, in the US alone they could help cut down on the expected 0.25% loss in GDP expected by 2060. For reference, 0.25% of GDP today is $46 billion, which is greater than the entire energy and environment budget of the US federal government in 2015. Other nations have even greater potential to save, with China expected to lose 2.5% of GDP to poor air quality by 2060, which equates to $280 billion if calculated in 2017.

Widespread adoption of our product could also go beyond just personal lifestyle changes and allow for even greater change if governments are given access to an anonymized stream of the data, allowing them to craft better policy that emphasizes exposure control in addition to source control. Together, these could lead to billions of dollars in economic gains and immeasurable social and health benefits.

Scaling this project may face different challenges though. While 4 out of 5 of our prototyped sensors proved sufficient for this application, the cost of the VOC sensor measured against its sensitivity is still an issue, and should be omitted until better, cheaper technology is available, as this is often a problem in other air quality sensor products. Furthermore, the product should eventually be linked to actuators such as automatic windows, HVAC controls, fans, and air purifiers in order to optimize ventilation strategies when there is no clear course of action for the user. This of course has the challenge of integrating the different languages and control mechanisms of the variety of HVAC systems in the world. However this appears to be something other companies (such as Nest) specialize in and thus they may prove to be a valuable partners or clients. For immediate expansion of the project though, the primary goals should be to improve our web interface, reduce the cost of the microcontroller and sensors, search for more viable VOC sensors, and link simple actuators to make it easier for users to create changes in their ventilation effectiveness.

**SUMMARY** To tackle the problem of air quality, Smart Air Bears provides a broad spectrum of users with the tools they need to make a change in their health and their environment. Our system has three key aspects: i) it is affordable, pricing at $59, while most personal air quality sensors cost upwards of $200, ii) it is personal, sensing air quality around a user, becoming more useful than government-monitored air quality maps of large regions that do not capture heterogeneity in a user&#39;s personal environment, iii) it is helpful, providing not only air quality data but also standards based metrics and recommendations. Overall, Smart Air Bears empowers users to understand the environment they live in and gives them the power to control their well-being in this environment.

**WORKS CITED**

1. Air Pollution Deaths Cost Global Economy US$225 Billion. World Bank. http://www.worldbank.org/en/news/press-release/2016/09/08/air-pollution-deaths-cost-global-economy-225-billion. Accessed December 8, 2017.

2. Bluyssen PM, De Oliveira Fernandes E, Groes L, et al. European Indoor Air Quality Audit Project in 56 Office Buildings. _Indoor Air_. 1996;6:221–238.

3. Arundel AV, Sterling EM, Biggin JH, Sterling TD. Indirect health effects of relative humidity in indoor environments. _Environ Health Perspect_. 1986;65:351–361.

4. Mølhave L. Indoor air pollution due to organic gases and vapours of solvents in building materials. _Environment International_. 1982;8:117–127.

5. Daisey JM, Angell WJ, Apte MG. Indoor air quality, ventilation and health symptoms in schools: an analysis of existing information. _Indoor Air_. 2003;13:53–64.

6. Laskey A, Kavazovic O. OPOWER. _XRDS: Crossroads, The ACM Magazine for Students_. 2011;17:47.

7. Dales R, Liu L, Wheeler AJ, Gilbert NL. Quality of indoor residential air and health. _Canadian Medical Association Journal_. 2008;179:147–152.

8. US EPA O. Regulatory Information by Topic: Air. US EPA. February 22, 2013. https://www.epa.gov/regulatory-information-topic/regulatory-information-topic-air. Accessed December 7, 2017.

9. Assessment UENC for E. Report to Congress on indoor air quality. Volume 2: Assessment and control of indoor air pollution. March 15, 2009. https://hero.epa.gov/hero/index.cfm/reference/details/reference\_id/1065604. Accessed December 8, 2017.

10. _The Economic Consequences of Outdoor Air Pollution_. OECD Publishing; 2016. June 9, 2016. http://www.oecd-ilibrary.org/environment/the-economic-consequences-of-outdoor-air-pollution\_9789264257474-en. Accessed December 7, 2017.

11. Wargocki P, Wyon DP, Sundell J, Clausen G, Fanger PO. The Effects of Outdoor Air Supply Rate in an Office on Perceived Air Quality, Sick Building Syndrome (SBS) Symptoms and Productivity. _Indoor Air_. 2000;10:222–236.

12. Kumar P, Morawska L, Martani C, et al. The rise of low-cost sensing for managing air pollution in cities. _Environment International_. 2015;75:199–205.

13. Lewis A, Edwards P. Validate personal air-pollution sensors. _Nature News_. 2016;535:29.

14. Vuetilovoni J. Why monitor Indoor Air Quality (IAQ)? Aeroqual. October 14, 2015. https://www.aeroqual.com/why-monitor-indoor-air-quality. Accessed December 7, 2017.

15. Yu T-C, Lin C-C, Chen C-C, et al. Wireless sensor networks for indoor air quality monitoring. _Medical Engineering &amp; Physics_. 2013;35:231–235.
