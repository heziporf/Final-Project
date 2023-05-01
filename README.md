## **Full Stack Automation Final Project**
[Short Video - Demonstration](https://drive.google.com/file/d/19zr8x8U3KihSHw9sduhP-Qw3haEHExqF/view)
### **_This project created to demonstrate my knowledge and skills in Automation Testing._**
***
### _About_
The project demonstates a smart automation infrastructure. It is built in hierarchy order of modules. The modules contain number of classes with methods.
There are main/common/helpers/actions/page_object modules.
In this way, the tests can be created in very simple way with a minimum lines of code.
Also the infrastructure allows to work with differend kinds of applications.
**Big advantage of the infrastructure is that it can be easy maintained!**

![image 1](https://www.linkpicture.com/q/pc_5.png)

### _Project Overview_

The project is an example of infrastructure for automation testing of different kinds of applications:
* Web based application
* Mobile application
* Web API
* Electron application
* Desktop application

### **_Infrastructure project includes using of:_**
* Page Object Design Pattern
* Project Layers(Extensions/Work Flows/Test Cases...)
* Support of Different Clients/Browsers
* Failure Mechanism
* Common Functionality
* External Files Support
* Reporting System (including screenshots)
* Visual Testing
* DB support
* CI support  

***

### _List of applications were used in this project:_
* atid.store - Web based e-commerce site
* Mortgage calculator - Mobile application
* https://reqres.in - Web Test API
* Electron application - Todolist Ap application
* Desktop application - Windows calculator 

### _Tools & Frameworks used in the project:_
* Pytest- Testing Framework
* Listeners - interface used to generate logs and customize the TestNG reports
* MySQL Free Online DB - used for login to Grafana web page
* [Jenkins](https://www.jenkins.io/)- for tests execution
* REST Assured - for API testing
* [Allure](http://allure.qatools.ru/) Reports - as the main reporting system

### Tests Execution:
> Each of the applications has a few tests for demonstration purpose.
These tests can be developed in a very simple way, due to a lot of work with the infrastructure.
[[Sanity Tests]](https://github.com/heziporf/Final-Project/tree/master/test_cases)

### _Known Issues:_
Sometimes can be conflicts with some dependencies the applications are using.
Hence, the project is for DEMO purpose only. In production it should be divided into several projects.
Nevertheless the file : requirements.txt is attached for using the same extensions or versions of any tool 
for using your own system for the entire tests.

![image 2](https://www.linkpicture.com/q/allure.png)
