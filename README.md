# **Web Automation Selenium 4.x | **Selenium (Python)


1. What is Selenium?
2. Don’t use Selenium here
3. Selenium vs Playwright vs Cypress
4. WebDriver Architecture
5. Simple Selenium Program. 


## What is Selenium?
- Automate the Browsers
- Selenium is an open-source suite. ( multiple things) - [﻿github.com/SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium) 
    - Selenium WebDriver
    - Selenium IDE
    - Selenium Grid
- Selenium Version 3 - Old - (10-25%) - JSON wire protocol
- Selenium Version 4 ( 2023) -> 75% - Selenium 4) - W3C protocol), Selenium Manger, Relative Locators....


## Don't Use Selenium here
- Selenium is not well-suited for performance or load testing because it is resource-intensive and can slow down the system under test.
- When you need to test native mobile apps.
- Selenium may have difficulty interacting with custom controls or non-standard UI elements.
- Captcha / TWO-FACTOR AUTHENTICATION (2FA)
- FILE DOWNLOADS & VERIFICATION.
- AUDIO OR VIDEO STREAMING
- Security Testing
- API TESTING, mobile Appium is recommended. 


## Selenium IDE
- Record and Playback Tool
- < 1% people - Don't use it
- TC < 50 
- Problem. IDE
    - Maintaining is biggest program
    - code duplicate.
    - You have to learn selenium ide selene .side learn
    - When windows size, some environment Test case failed.  
[﻿www.selenium.dev/selenium-ide/](https://www.selenium.dev/selenium-ide/) 



## Selenium WebDriver
- Supports lot of Programing languages 
- Selenium RC + Webdriver(SS) - Selenium 3 
 **Selenium Version 3** - Old - (10-25%) - JSON wire protocol

- **Selenium Version 4 **( 2023) -> 75% - Selenium 4) - W3C protocol), Selenium Manger, Relative Locators....


Book - [﻿selenium-python.readthedocs.io/_/downloads/en/latest/pdf/](https://selenium-python.readthedocs.io/_/downloads/en/latest/pdf/) 





#### **WebDriver Architecture 3 **
- Write a Code ( Java, Python , Ruby ) -> HTTP REQUEST( Rest API) ( GET, POST, PATCH, DELETE) -> Browser Driver (Server) -> Give Command -> Browsers.


**Selenium Concepts**

- Chrome Options
- Quit and Close
- Navigation Commands
- Basic Programs




**Headless**

- No UI
- Fast - real browser but no UI to see.
- TC -> 5000 , Less Memory


**Non Headless**

- UI
- Slow
- High Memory 


---

**Test Script in Selenium **



**Mini Project #1**

- Open a URL
- **Find the Button - (HTML)**
- Click on the it
- Find the inputbox for username and password
- Enter the username and password
- Verify that the on clicking the submit button, user is logged in.


**Mini Project #2**

1. Open the [﻿app.vwo.com/#/login](https://app.vwo.com/#/login) 
2. Find the element email and Enter the email as admin@admin.com
3. Find the element password input box and Enter the password as admin.
4. Find the submit and Click on the submit button
5. Verify that after 1-2 sec , error message comes. 


**Actions**

1. Navigation - get, back, refresh, forward
2. Find Elements - findelement, findelemenets (SeachContext)
3. What exaclty we are finding - HTML elements(**Web Elements)**
    1. button
    2. inputbox
    3. checkbox
    4. Web tables... many more HTML elements
4. Verify 


**HTML Elements**

Anchor Tag - Which is used to give a user a Hyperlink.

<tagName attribute=value></tagName> 

<a 

id="btn-make-appointment" 

href="./profile.php#login" 

class="btn btn-dark btn-lg">

Make Appointment

</a>

# What is the Step we need to Follow?
- Find the element the anchor tag 
- Click on it


**Locators in Selenium**

- Basic -> id, className, name, tagName, linkText and PartialLinkText.
- Advance -> css Selector, xpath 


1. XPath
2. Css Selectors




**Basic Locators** - id, name className,  tagName , LinkText, Partial Link Text - a tag

**Advance**  - XPath and CSS Selector

Objective - To find the web element. Unique Locator 

#### 🛣️ **Mastering XPath**
What is XPath?

- XPath is a query language for selecting nodes from an HTML / XML document.
- XPath was defined by the World Wide Web Consortium ( W3C -> All major Browser)
- Chrome, Safari, IE, Opera, Edge.
- ****


## **Types XPath**
##### **Why do we need to MASTER Locators?**
- Probably the first question asked by the interviewer.
- You should always find small and efficient Locators.
- Max time - id, className, name attributes are not available - 90% or they change.
- UI Automation is all about finding locators.


Disclaimer -> Don't use tools at first.





- **Absolute XPath** - from the** root node** -> 
    - /html/body/header/div/a -> make appoinment 
    - `/html/body/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div[3]/form[1]/ul/li[1]/div/input -> app.vwo.com input box` 
- Dis
    - 1. Too big
    - 2. If any one element is updated or append it will break.


-   **Relative XPath **- Core Logic - **//tagName[@attribute='value']**
    - Short and simple to use. 
    - XPath - easy to maintain
    - Based on searching an element in DOM(HTML Page)
    - You can simply start by referencing the element you want and go from there.
- **//tagName[@attribute='value']**


```
//a[@id="btn-make-appointment"] - Make appointment Button
```
```
//a[@href='./profile.php#login'] - href attribtue 
```
1. Know Attribute - id, name, className
2. Custom or ->  href.
3. **XPath Functions**
    1. Full Visible Text  Match-  text() -> `//a[text()="Make Appointment"]` 
    2. Partial Visible Text - contains(),starts-with(), ends-with()
        1. `//a[contains(text(),"Make")]` 
        2. `//a[contains(text(),"Make App")]` 
        3. `//a[starts-with(text(),'App')]` 
        4. `//a[normalize-space(text())='Pramod'] -> ``<a class="btn btn-dark btn-lg">Pramod </a>` 
Operators - AND & OR

- `//a[text()="Make Appointment" and contains(@id,"btn-make-appointment")]` 


**XPath Axes**

- Ancestor
- Child, parent
- Descendant
- Following, following-sibling, preceding-siblings
- Self.


Shadow dom - Xpath

SVG - Xpath



**CSS Selectors**

CSS selectors are used to select elements in an HTML or XML document in order to apply styles or other manipulations to those elements. 

id -> #id

class -> .class

div span -> div.span

```
//a[@id='btn-make-appointment'] -> a#btn-make-appointment
```
```
div.first > span:nth-child(n) , first-child, last-child - 
```
## 


**⌛Selenium Concepts Waits **
Why Do We Need Waits In Selenium?

- time.sleep(5) ?
- Web applications are developed using AJAX and Javascript.
- Element load after sometime - e1 , e2 , e3 
- e1 loaded in 0, e2 loads 2, e3 loads - 5 -> Webdriver -> find the elements -> Drive will wait?
- time.sleep(4) -> 
    - Python It to stop for halt for 5
    - This is probably the worst type of wait you can use in the script.
- New JS frameworks are more advanced and use AJax, react, and angular,VueJS. 


**Implicit Wait**

- Selenium Web Driver has borrowed the idea of implicit waits from Watir.
- Global settings applicable to all elements.
- It tells the web driver to wait for the x time before moving to the next command.
- No concept condition here. 
- Gives No Such Element Exception.
- Once it is set it is applicable to full automation script.
- Implicit wait is maximum time between the two commands.
- Different from time.sleep - time.sleep() - I**t will sleep time for script/ Py Int.**
- Not good way to use it in script as it's sleep without condition.
- Do not mix implicit and explicit waits. Doing so can cause unpredictable wait times.




**Explicit Wait ( 97%) **

- Explicit Wait in Selenium is used to tell the Web Driver to wait for certain conditions (Expected Conditions) or maximum time exceeded before throwing “ElementNotVisibleException” exception.
- Little intelligent wait, wait for certain conditions.
- They **allow your code to halt program execution, or freeze the thread, until the condition you pass it resolves.**
- It provides better way to handle the dynamic Ajax elements.
- Replace Thread.sleep / time.sleep() with explicit wait always.
- Good fit for synchronizing the state between the browser and its DOM, and your. -> work with Ajax type of websites - EW
- **Element not visible** exception if element not found.


**Fluent Wait (3%)**

- Fluent Wait instance defines the maximum amount of time to wait for a condition as well as the frequency with which to check the condition
- Exception - NoSuchElementException
- Waiting 30 seconds for an element to be present on the page, checking for its presence once every 5 seconds.


**Misc Concepts**

- Select Demo
    - Static Dropdpwn - Select 
    - Dynamic Dropdowns
        - static with custom controls - [﻿app.vwo.com](https://app.vwo.com/) signup - JS , multi select
        - Pure dynamic ( JS, Actions, logic)
- Alert in Selenium
- Handling Checkboxes and Handling Radio Buttons
---

## **Selenium Exception**
What is an Exception?

-  Exceptions in Python are errors that occur during the execution of Selenium scripts.
- Disruption from the normal flow. 
- Understanding these exceptions is crucial for effective error handling in automated testing.


Error - are something that can't be handled -> StackoverflowError, OutofmemoryERROR, IOErrors

Exception - are something that can be handled  -> try and except. 



Types of Selenium Exception

1. **NoSuchElementException**


---

### 
**Actions, Windows and iframe.**
Actions - In built class in the Selenium. - w

1. Keyboard event
2. Mouse
3. Wheel events 


`from selenium.webdriver.common.actions_chains import ActionChains` 

`actions = ActionChains(driver)` 



- ActionChains are a way to automate low level interactions such as mouse
 movements, mouse button actions, key press, and context menu interactions.

- This is useful for doing more complex actions like hover over and drag and
 drop.


- Web Tables ( Unlock a video)
- Shadow DOM ( let me check)


- Web Tables, SVG, Shadow DOM
- Actions Class
---

- Page Object Model , Page Factory
- JavaScript executor** **
- Setting the Framework
- Jenkins Running GIT


Why we need to use any pattern or model with Selenium?

1. Proper Structure
2. Readability
3. Reusability 
4. Low Maintenance
5. Scalability - 10, -> 10,000


We follow the rules, so that, Whenever any JR QA. 





#### Page Object Model
- It is a design pattern in Selenium.
- creates a representation of web pages as classes.
    - **LoginPage.py **-> Python Class  -> It will contain Object Repo -> Page Locators,  + Page Actions 
        - **Page Locators** - > email, password, remember me, sign up button, submit button
        - **Page Actions** -> click on submit, enter email and password, remember button
    - DashboardPage -> Class Python -> It will contain ->Page Locators,  + Page Actions 
        - **Page Locators** -> user_logged_in
        - **Page Actions** ->  Verfication of the user_logged_in with get Text method == Aman JI
    - **Page Object Model -> All the pages ->  Page Locators  + Page Actions.**
- Each class contains methods and properties that corresponds to the elements and actions on that page


Key characteristics of POM include:

1. **Structure**
2. **Maintainability**
3. **Reusability**


1. Page Factory 
2. conftest.py - 
3. headless - 
4. logging
5. jenkins via GIT




---

## Page Factory
1.  Specific implementation of the Page Object Model.
2. It enhances POM.
3. It more optimzed.
4. They are predefind library in selenium to find the element on the page.
5. Its way to initize the web element you want to interact with or within page, when you are instance. (Page Object) - drver -> find them asap.)
- Prone to StaleElementException exception.


![image.png](https://eraser.imgix.net/workspaces/zPGHlPfHMUi1uDB0tyqX/WWS31TdyovhjTB1TVo9v2jWpPei1/j40FXQWEwPSdt58zIffEx.png?ixlib=js-3.7.0 "image.png")



**Jenkins via GIT (CI, CD)**

What is Jenkins?

- Jenkins -> Will help you to run your code automatically. It like a slave.
- 5 steps in Jenkins 
- Build, Trigger -> Post build It can send the emails, or generate the allure report also.
