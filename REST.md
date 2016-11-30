Rest API
=======

Rest API is one of the popular webservices in the world. This code implements Rest API for performing word count operation in a file, sorting array of numbers, checking whether a number is prime or not.
For implementing this API we used flask python frame work. For converting the results in to json format, we used jsonify python library

Usage
-----

### Making a request using POST or GET: ###

#### Sorting array of numbers ####
Sorting array of numbers is required for so many applications. We are providing REST API service for sorting array of numbers.
In this service we are going to pass query parameters to the http url. "array" parameter is of string data-type which we use to send array of numbers as string which are seperated by comma.
Below is the request for sorting 34,7,8,9,1 array of numbers. you can use either GET or POST requests for the below url  
##### API call #####
http://ec2-35-160-1-123.us-west-2.compute.amazonaws.com/api/sort?array={array of numbers}
##### Parameters #####
**array:**   array of numbers divided by comma where we pass it as string data type
##### Example of API call #####
```API
http://ec2-35-160-1-123.us-west-2.compute.amazonaws.com/api/sort?array=34,7,8,9,1
```
##### API Response #####
Response from server with header information
```Result
HTTP/1.1 200 OK
Date: Mon, 31 Oct 2016 17:23:48 GMT
Server: Apache/2.4.18 (Ubuntu)
Content-Length: 24
Content-Type: application/json

{"result":[1,7,8,9,34]}

```
From the above it is clear that server response is in the form of json data type

#### Prime number or not ####
* This service helps to check whether the number is prime or not
* Here we are using one query parameter "number" which is of integer data-type
Below is the request for checking whether a number is prime or not. you can use either GET or POST requests for the below url

##### API call #####
http://ec2-35-160-1-123.us-west-2.compute.amazonaws.com/api/prime?number={number}

##### Parameters #####
**number:** number to be checked, which is of int data type 

##### Example of API call #####
```API
http://ec2-35-160-1-123.us-west-2.compute.amazonaws.com/api/prime?number=17
```

##### API Response #####
Response from server with header information
```Result
HTTP/1.1 200 OK
Date: Mon, 31 Oct 2016 18:52:33 GMT
Server: Apache/2.4.18 (Ubuntu)
Content-Length: 26
Content-Type: application/json

{"result":"Prime Number"}
```
From the above it is clear that server response is in the form of json data type

#### Word frequency in a file ####
* This service helps to find the frequency of word in a file
* Here you have to send text file and a word which you want to know the frequency in a file 
Below is the sample request using curl. In the below request we are uploading a file named  "sample" and also sending "are" word to the server. Here we are finding the frequency of "are" word in sample text file. You can use either GET or POST requests for the below url

##### API call #####
curl -i -X POST  -F "file=@sample" -F "word=are" http://ec2-35-160-1-123.us-west-2.compute.amazonaws.com/api/wordfreq

##### Parameters #####
**file:** Source file

**word:** Target word, which is of string data type

##### Example of API call #####
```API
curl -i -X POST  -F "file=@sample" -F "word=are" http://ec2-35-160-1-123.us-west-2.compute.amazonaws.com/api/wordfreq
```

##### API Response #####
Response from server  with header information
```Result
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2016 16:13:20 GMT
Server: Apache/2.4.18 (Ubuntu)
Content-Length: 13
Content-Type: application/json

{"result":8}
```
From the above it is clear that server response is in the form of json data type

Weather API

##### API call:   
http://ec2-35-160-1-123.us-west-2.compute.amazonaws.com/api/weather?city={city name}

##### Parameters:   

city : city name and country code divided by comma, use ISO 3166 country codes

##### Example call : #####
```API
http://ec2-35-160-1-123.us-west-2.compute.amazonaws.com/api/weather?city=cincinnati
```
The output is in json format which consists of temperature, pressure, humidity metrics
##### Response : #####
```Result
{"coord":{"lon":-84.46,"lat":39.16},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"base":"stations","main":{"temp":287.94,"pressure":1007,"humidity":54,"temp_min":286.15,"temp_max":289.15},"visibility":16093,"wind":{"speed":6.7,"deg":170},"clouds":{"all":90},"dt":1480470720,"sys":{"type":1,"id":1128,"message":0.1654,"country":"US","sunrise":1480509466,"sunset":1480544134},"id":4508722,"name":"Cincinnati","cod":200}
```

