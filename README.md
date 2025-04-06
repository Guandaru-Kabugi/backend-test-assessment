# backend-test-assessment

# The project is about handling employee data

>>> It has two separate django apps. 
>>>>>>>>One app handles accounts, which involves signing up and logging in an user
>>>>>>>>The second app handles crud operations related to the employee

>>Under Employees, I made use of Django Rest Framework
>>I used class based views, which come in different forms like create,delete,update,retrieve, and get.
>> The project also has the urls.py under each django app, which handles the http requests 
>> The project also had some security feature, which was JWT token.
>> The user must be registered to get a token.
>> The user must use the token so that they can make different requests related to the employees.
>> It ensures that unauthorized users cannot access the data.
>> I made use of postgres.
>> I ensured security of my database details use a .env file and os.getenv 

The project uses serializers to jsonify the output for easier readability.

I used POSTMAN to test the different endpoints to ensure they worked according to the program.