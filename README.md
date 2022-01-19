### **Sum Of Numbers API**
---

#### **Project Description** 
- This project is a REST API which has one endpoint total.
Total takes a JSON object from a back-end service containing a list of numbers and returns the total of the list back as a JSON object.
The URL of the endpoint is http://localhost:5000/total

#### **Installing the environment** 
- In order to run this project the environment containing all packages and dependencies is saved down in the env.yml. 

- This environment can be created locally by running the following command: `conda env create -f environment.yml`

#### **Script Descriptions**
*sumofnumbers.py*
- This script contains the code which creates the API using a flask framework. 
- Run this code to create the application and host the API at the above URL.

*test_sumofnumbers.py*
- This script contains the tests that have been completed on the endpoint /total.
- Tests have been written within the pytest framework and been completed on a Windows operating System.

#### **Assumptions**
- The request from the back-end service should be in a JSON format and it is a JSON format that is requried for the response. 


