# Paktolus


use deployed link - https://packlotus-task.netlify.app/

to run frontend -
1)install node modules using npm install
2)run nom start 

for backend -
1) make sure docker and pgadmin or postgresql is running
2) i used mannul command to create table 
3) using following commands first i check wheather it working fine or not.
# 
---------------------to create table with required constraint---------------

        CREATE TABLE user1 (
      	id serial PRIMARY KEY,
     	username VARCHAR (40) NOT NULL,
     	message VARCHAR (1000) NOT NULL,
     	comments varchar[]
           );

    # ------------------To add data into column---------------- 

     INSERT INTO user1 (id, username, message,comments)
     VALUES (1, 'kk','nens sdjhfbf sjshfsj sj snsh ',ARRAY ['']);

    # -------------------To get data from database in json formate--------------
     select row_to_json(user1)from (  select id, username, message, comments from user1
    ) user1;

    # ----------------------add comments in column with id ---------------------
     update user1 set comments=ARRAY ['new thing','second comment'] where id=1


#
4)create docker image using command  docker build -t imagegename
#
5)run that image using  command docker run -p 80:8000 imagename
#
6)back running on port 8000.
#
sometimes docker doesn't start  then we can we direct python command to run backend for this we have to follow these steps--
#
1)install all required modules from requirements.txt file using command   pip install -r requirements.txt
2)run file app.py file using  command  - python app.py 
3)backend starts on port 8000
#
![image](https://user-images.githubusercontent.com/98754287/205159993-a56050b1-d7dd-4bf4-9248-0d941d6272e8.png)
![image](https://user-images.githubusercontent.com/98754287/205160071-1b8ff39f-0bcc-435f-a077-7e7483168d81.png)
![image](https://user-images.githubusercontent.com/98754287/205160121-774b61d4-0075-466d-9532-f3961595e18d.png)
![image](https://user-images.githubusercontent.com/98754287/205160169-b5cfe626-8deb-4641-815d-dc1dd071c003.png)

![image](https://user-images.githubusercontent.com/98754287/205162677-cba7b369-5886-46d0-9dc5-7ed3b0cf23a6.png)
![image](https://user-images.githubusercontent.com/98754287/205162851-433abcb0-7b89-4820-9a69-972f054d183f.png)




